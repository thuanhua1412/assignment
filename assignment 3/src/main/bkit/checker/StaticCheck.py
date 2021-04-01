# Student ID: 1814226        Name: Hua Phuoc Thuan
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class IntType(Prim):
    pass


class FloatType(Prim):
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass


class VoidType(Type):
    pass


class Unknown(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type


@dataclass
class MType(Type):
    intype: List[Type]
    restype: Type


@dataclass
class Symbol:
    name: str
    mtype: MType
    kind:Kind

class Utils():
    def lookup(self, name, lst: List[List[Symbol]]):
        for scope in lst:
            for x in scope:
                if name == x.name:
                    return x
        return None



class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.built_in = [
            Symbol("int_of_float", MType([FloatType()], IntType()), Function()),
            Symbol("float_to_int", MType([IntType()], FloatType()), Function()),
            Symbol("int_of_string", MType([StringType()], IntType()), Function()),
            Symbol("string_of_int", MType([IntType()], StringType()), Function()),
            Symbol("float_of_string", MType([StringType()], FloatType()), Function()),
            Symbol("string_of_float", MType([FloatType()], StringType()), Function()),
            Symbol("bool_of_string", MType([StringType()], BoolType()), Function()),
            Symbol("string_of_bool", MType([BoolType()], StringType()), Function()),
            Symbol("read", MType([], StringType()), Function()),
            Symbol("printLn", MType([], VoidType()), Function()),
            Symbol("print", MType([StringType()], VoidType()), Function()),
            Symbol("printStrLn", MType([StringType()], VoidType()), Function())
        ]
        self.global_envi = [self.built_in[:]]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast: Program, c):
        for declare in ast.decl:
            if isinstance(declare, VarDecl):
                self.visit(declare, c)

        for declare in ast.decl:
            if isinstance(declare,FuncDecl):
                var = self.lookup(declare.name.name, [c[0]])
                if var is not None:
                    raise Redeclared(Function(), declare.name.name)

                c[0].append(Symbol(declare.name.name, MType([], Unknown()),Function()))
                [c[0][-1].mtype.intype.append(Unknown()) for parameter in declare.param]

        for declare in ast.decl:
            if isinstance(declare, FuncDecl):
                self.visit(declare, c)

        entry = self.lookup("main", c)
        if entry is None:
            raise NoEntryPoint()

    def visitVarDecl(self, ast: VarDecl, param):
        var = self.lookup(ast.variable.name, [param[0]])
        if var is not None:
            raise Redeclared(Variable(), ast.variable.name)

        if ast.varDimen:
            if ast.varInit:
                if type(ast.varInit) is ArrayLiteral:
                    param[0].append(
                        Symbol(ast.variable.name, MType([], self.visit(ast.varInit, param)), Variable()))
                    #print(param[0][-1])
                else:
                    pass
            else:
                arr_type = Unknown()
                for i in range(len(ast.varDimen)):
                    arr_type = ArrayType(ast.varDimen[(len(ast.varDimen) - 1 - i):], arr_type)

                param[0].append(Symbol(ast.variable.name, MType([], arr_type), Variable()))
                #print(param[0][-1])
        else:
            if ast.varInit:
                param[0].append(Symbol(ast.variable.name, MType([], self.visit(ast.varInit, param)), Variable()))
            else:
                param[0].append(Symbol(ast.variable.name, MType([], Unknown()), Variable()))

    def ReturnStatement(self, Stmts, func: Symbol, param):
        if isinstance(Stmts, Return):
            stmt_type = self.visit(Stmts, param)
            if isinstance(func.mtype.restype, Unknown):
                if isinstance(stmt_type, Unknown):
                    raise TypeCannotBeInferred(Stmts)
                if isinstance(stmt_type, ArrayType):
                    while True:
                        if isinstance(stmt_type, Unknown):
                            raise TypeCannotBeInferred(Stmts)
                        if not isinstance(stmt_type, ArrayType):
                            break
                        stmt_type = stmt_type.eletype

            stmt_type = self.visit(Stmts, param)
            if isinstance(func.mtype.restype, Unknown):
                func.mtype.restype = stmt_type

            if not isinstance(self.visit(Stmts, param), ArrayType) or not isinstance(func.mtype.restype, ArrayType):
                if type(self.visit(Stmts, param)) != type(func.mtype.restype):
                    raise TypeMismatchInStatement(Stmts)
            else:
                stmt_type = self.visit(Stmts, param)
                ret_type = func.mtype.restype
                while True:
                    if type(ret_type) != type(stmt_type):
                        raise TypeMismatchInStatement(Stmts)
                    if not isinstance(ret_type, ArrayType) and not isinstance(stmt_type, ArrayType):
                        break
                    ret_type = ret_type.eletype
                    stmt_type = stmt_type.eletype

    def visitFuncDecl(self, ast: FuncDecl, param):
        local = [[]]
        func = self.lookup(ast.name.name, param)
        for i in range(len(ast.param)):
            parameter = self.lookup(ast.param[i].variable.name, [local[0]])
            if parameter is not None:
                raise Redeclared(Parameter(), parameter.name)
            self.visit(ast.param[i], local)
            if isinstance(local[0][-1].mtype.restype, Unknown):
                local[0][-1].mtype.restype = func.mtype.intype[i]

        total = local + param + [[func]]
        [self.visit(varDecl, total) for varDecl in ast.body[0]]
        for Stmts in ast.body[1]:
            self.visit(Stmts, total)
            self.ReturnStatement(Stmts, func, total)


        if isinstance(func.mtype.restype, Unknown):
            func.mtype.restype = VoidType()

        for i in range(len(ast.param)):
            parameter = self.lookup(ast.param[i].variable.name, total)
            if not isinstance(parameter.mtype.restype,Unknown):
                func = self.lookup(ast.name.name,param)
                func.mtype.intype[i] = parameter.mtype.restype
        #print(var.name,var.mtype.intype)

    def visitBinaryOp(self, ast: BinaryOp, param):
        op = ast.op
        left = self.visit(ast.left,param)
        right = self.visit(ast.right,param)

        if "TypeCannotBeInferred" in [left, right]:
            return "TypeCannotBeInferred"
        #print(left,right)
        if op in ['+','-','*',"\\","%"]:
            if isinstance(left,(Unknown,IntType)) and isinstance(right,(Unknown,IntType)):
                if isinstance(left,Unknown):
                    var = self.lookup(ast.left.name,param) if isinstance(ast.left,Id) \
                        else self.lookup(ast.left.method.name,param)
                    var.mtype.restype = IntType()

                if isinstance(right,Unknown):
                    var = self.lookup(ast.right.name,param) if isinstance(ast.right,Id) \
                        else self.lookup(ast.right.method.name,param)
                    var.mtype.restype = IntType()
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)

        if op in ['+.','-.','*.','\\.']:
            if isinstance(left,(Unknown,FloatType)) and isinstance(right,(Unknown,FloatType)):
                if isinstance(left,Unknown):
                    var = self.lookup(ast.left.name,param) if isinstance(ast.left,Id) \
                        else self.lookup(ast.left.method.name,param)
                    var.mtype.restype = FloatType()

                if isinstance(right,Unknown):
                    var = self.lookup(ast.right.name,param) if isinstance(ast.right,Id) \
                        else self.lookup(ast.right.method.name,param)
                    var.mtype.restype = FloatType()

                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)

        if op in ["==","!=","<",">","<=",">="]:
            if isinstance(left,(Unknown,IntType)) and isinstance(right,(Unknown,IntType)):
                if isinstance(left,Unknown):
                    var = self.lookup(ast.left.name,param) if isinstance(ast.left,Id) \
                        else self.lookup(ast.left.method.name,param)
                    var.mtype.restype = IntType()

                if isinstance(right,Unknown):
                    var = self.lookup(ast.right.name,param) if isinstance(ast.right,Id) \
                        else self.lookup(ast.right.method.name,param)
                    var.mtype.restype = IntType()
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        if op in ["=/=","<.",">.","<=.",">=."]:
            if isinstance(left,(Unknown,FloatType)) and isinstance(right,(Unknown,FloatType)):
                if isinstance(left,Unknown):
                    var = self.lookup(ast.left.name,param) if isinstance(ast.left,Id) \
                        else self.lookup(ast.left.method.name,param)
                    var.mtype.restype = FloatType()

                if isinstance(right,Unknown):
                    var = self.lookup(ast.right.name,param) if isinstance(ast.right,Id) \
                        else self.lookup(ast.right.method.name,param)
                    var.mtype.restype = FloatType()
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        if op in ["||","&&"]:
            if isinstance(left,(Unknown,BoolType)) and isinstance(right,(Unknown,BoolType)):
                if isinstance(left,Unknown):
                    var = self.lookup(ast.left.name,param) if isinstance(ast.left,Id) \
                        else self.lookup(ast.left.method.name,param)
                    var.mtype.restype = BoolType()

                if isinstance(right,Unknown):
                    var = self.lookup(ast.right.name,param) if isinstance(ast.right,Id) \
                        else self.lookup(ast.right.method.name,param)
                    var.mtype.restype = BoolType()
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)


    def visitUnaryOp(self, ast: UnaryOp, param):
        op = ast.op
        operand = self.visit(ast.body,param)

        if operand == "TypeCannotBeInferred":
            return "TypeCannotBeInferred"
        if op == "-":
            if isinstance(operand,(Unknown,IntType)):
                if isinstance(operand,Unknown):
                    var = self.lookup(ast.body.name,param) if isinstance(ast.body,Id) \
                        else self.lookup(ast.body.method.name,param)
                    var.mtype.restype = IntType()

                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        if op == "-.":
            if isinstance(operand,(Unknown,FloatType)):
                if isinstance(operand,Unknown):
                    var = self.lookup(ast.body.name,param) if isinstance(ast.body,Id) \
                        else self.lookup(ast.body.method.name,param)
                    var.mtype.restype = FloatType()

                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)

        if op == "!":
            if isinstance(operand,(Unknown,BoolType)):
                if isinstance(operand,Unknown):
                    var = self.lookup(ast.body.name,param) if isinstance(ast.body,Id) \
                        else self.lookup(ast.body.method.name,param)
                    var.mtype.restype = BoolType()

                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)


    def visitCallExpr(self, ast: CallExpr, param):
        var = self.lookup(ast.method.name, param)
        if var is not None:
            if not isinstance(var.kind, Function):
                raise Undeclared(Function(),ast.method.name)
            if len(var.mtype.intype) != len(ast.param):
                raise TypeMismatchInExpression(ast)

            if var.mtype.intype:
                for i in range(len(ast.param)):
                    parameter = self.lookup(ast.param[i].name, param) if isinstance(ast.param[i], Id) \
                        else self.lookup(ast.param[i].method.name, param) if isinstance(ast.param[i], CallExpr) else ""
                    param_type = parameter.mtype.restype if isinstance(parameter, Symbol) else self.visit(ast.param[i], param)

                    if (isinstance(param_type, Unknown) and isinstance(var.mtype.intype[i], Unknown)) or param_type == "TypeCannotBeInferred":
                        return "TypeCannotBeInferred"
                    if isinstance(param_type, Unknown):
                        parameter.mtype.restype = var.mtype.intype[i]

                    if isinstance(var.mtype.intype[i], Unknown):
                        var.mtype.intype[i] = param_type

                    param_type = parameter.mtype.restype if isinstance(parameter, Symbol) else self.visit(ast.param[i], param)
                    if type(var.mtype.intype[i]) != type(param_type):
                        raise TypeMismatchInExpression(ast)
                    self.visit(ast.param[i],param)
        else:
            raise Undeclared(Function(), ast.method.name)
        #print(var.mtype.restype)
        return var.mtype.restype

    def visitId(self, ast: Id, param):
        var = self.lookup(ast.name, param)
        if var is not None:
            if not isinstance(var.kind, Variable):
                raise Undeclared(Identifier(),ast.name)
            return var.mtype.restype
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast: ArrayCell, param):
        id_type = self.visit(ast.arr, param)
        ACell = self.lookup(ast.arr.name, param) if isinstance(ast.arr, Id) else self.lookup(ast.arr.method.name, param)
        #print(ast.arr, id_type)
        if id_type == "TypeCannotBeInferred" or (isinstance(id_type,Unknown) and isinstance(ast.arr,CallExpr)):  # id is a CallExpr but cannot inferred the parameter type
            return "TypeCannotBeInferred"
        #print(ast.arr)

        if not isinstance(id_type, ArrayType):
            raise TypeMismatchInExpression(ast)
        else:
            if len(ACell.mtype.restype.dimen) != len(ast.idx):
                raise TypeMismatchInExpression(ast)

        for expr in ast.idx:
            expr_type = self.visit(expr, param)
            if expr_type == "TypeCannotBeInferred":
                return "TypeCannotBeInferred"
            if isinstance(expr_type, Unknown):
                var = self.lookup(expr.name, param) if isinstance(expr, Id) else self.lookup(expr.method.name, param)
                var.mtype.restype = IntType()

            expr_type = self.visit(expr, param)
            if not isinstance(expr_type, IntType):
                raise TypeMismatchInExpression(ast)

        for x in range(len(ast.idx)):
            if not isinstance(id_type,ArrayType):
                raise TypeMismatchInExpression(ast)
            id_type = id_type.eletype
        return id_type

    def visitAssign(self, ast: Assign, param):
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)
        #print(ast.lhs,lhs,rhs)
        if (isinstance(lhs, Unknown) and isinstance(rhs, Unknown)) or ("TypeCannotBeInferred" in [lhs, rhs]):
            # both lhs and rhs is Unknown Type or (rhs or lhs is CallExpr and can't be inffered)
            raise TypeCannotBeInferred(ast)
        if isinstance(lhs, VoidType) or isinstance(rhs, VoidType):
            raise TypeMismatchInStatement(ast)
        # print(self.visit(ast.lhs,param),self.visit(ast.rhs,param))
        if isinstance(lhs, Unknown):
            if isinstance(ast.lhs, Id):
                var = self.lookup(ast.lhs.name, param)
                if isinstance(self.visit(ast.rhs, param), ArrayType):
                    raise TypeMismatchInStatement(ast)
                var.mtype.restype = self.visit(ast.rhs, param)
            elif isinstance(ast.lhs, CallExpr):
                var = self.lookup(ast.lhs.method.name,param)
                var.mtype.restype = self.visit(ast.rhs, param)
            else:
                if isinstance(ast.lhs.arr, Id):
                    var = self.lookup(ast.lhs.arr.name,param)
                else:
                    var = self.lookup(ast.lhs.arr.method.name, param)
                eletype = var.mtype.restype
                while True:
                    if isinstance(eletype.eletype, Unknown):
                        eletype.eletype = self.visit(ast.rhs, param)
                        break
                    eletype = eletype.eletype

        if isinstance(rhs, Unknown):
            if isinstance(ast.rhs, Id):
                var = self.lookup(ast.rhs.name, param)
                if isinstance(self.visit(ast.rhs, param), ArrayType):
                    raise TypeMismatchInStatement(ast)

                var.mtype.restype = self.visit(ast.lhs, param)
            elif isinstance(ast.rhs, CallExpr):
                var = self.lookup(ast.rhs.method.name,param)
                var.mtype.restype = self.visit(ast.lhs, param)
            else:
                if isinstance(ast.rhs.arr, Id):
                    var = self.lookup(ast.rhs.arr.name,param)
                else:
                    var = self.lookup(ast.rhs.arr.method.name, param)
                eletype = var.mtype.restype
                while True:
                    if isinstance(eletype.eletype, Unknown):
                        eletype.eletype = self.visit(ast.lhs, param)
                        break
                    eletype = eletype.eletype
        #print(self.visit(ast.lhs,param),self.visit(ast.rhs,param))
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)
        #print(type(lhs),type(rhs))

        if isinstance(lhs,ArrayType) and isinstance(rhs,ArrayType):
            if lhs.dimen != rhs.dimen:
                raise TypeMismatchInStatement(ast)
            lhs_eletype = lhs.eletype
            rhs_eletype = rhs.eletype
            while True:
                if isinstance(lhs_eletype, Unknown):
                    if isinstance(ast.lhs, Id):
                        var = self.lookup(ast.lhs.name, param)
                    elif isinstance(ast.lhs, CallExpr):
                        var = self.lookup(ast.lhs.method.name, param)
                    else:
                        if isinstance(ast.lhs.arr, Id):
                            var = self.lookup(ast.lhs.arr.name, param)
                        else:
                            var = self.lookup(ast.lhs.arr.method.name, param)

                    eletype = var.mtype.restype
                    while True:
                        if isinstance(eletype.eletype,Unknown):
                            eletype.eletype = rhs_eletype
                            break
                        eletype = eletype.eletype
                    break

                if isinstance(rhs_eletype, Unknown):
                    if isinstance(ast.rhs, Id):
                        var = self.lookup(ast.rhs.name, param)
                    elif isinstance(ast.rhs, CallExpr):
                        var = self.lookup(ast.rhs.method.name, param)
                    else:
                        if isinstance(ast.rhs.arr, Id):
                            var = self.lookup(ast.rhs.arr.name, param)
                        else:
                            var = self.lookup(ast.rhs.arr.method.name, param)

                    eletype = var.mtype.restype
                    while True:
                        if isinstance(eletype.eletype,Unknown):
                            eletype.eletype = lhs_eletype
                            break
                        eletype = eletype.eletype
                    break

                if not isinstance(lhs_eletype,ArrayType) and not isinstance(rhs_eletype,ArrayType):
                    break

                if isinstance(lhs_eletype,ArrayType):
                    lhs_eletype = lhs_eletype.eletype

                if isinstance(rhs_eletype,ArrayType):
                    rhs_eletype = rhs_eletype.eletype


            if isinstance(lhs_eletype,Unknown) and isinstance(rhs_eletype,Unknown):
                raise TypeCannotBeInferred(ast)

            lhs_eletype = self.visit(ast.lhs, param)
            rhs_eletype = self.visit(ast.rhs, param)
            while True:
                if type(lhs_eletype) != type(rhs_eletype):
                    raise TypeMismatchInStatement(ast)

                if isinstance(lhs_eletype, ArrayType):
                    lhs_eletype = lhs_eletype.eletype
                else:
                    break

                if isinstance(rhs_eletype, ArrayType):
                    rhs_eletype = rhs_eletype.eletype
                else:
                    break

        if type(self.visit(ast.lhs,param)) is not type(self.visit(ast.rhs,param)):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast: If, param):
        func = param[-1][0]
        for ifthenStmt in ast.ifthenStmt:
            var = self.lookup(ifthenStmt[0].name, param) if isinstance(ifthenStmt[0], Id) \
                else self.lookup(ifthenStmt[0].method.name, param) if isinstance(ifthenStmt[0],CallExpr) else ""
            exp_type = var.mtype.restype if isinstance(var,Symbol) else self.visit(ifthenStmt[0], param)
            if exp_type == "TypeCannotBeInferred":
                raise TypeCannotBeInferred(ast)

            if isinstance(exp_type, Unknown):
                var.mtype.restype = BoolType()

            exp_type = self.visit(ifthenStmt[0], param)
            if exp_type == "TypeCannotBeInferred":
                raise TypeCannotBeInferred(ast)

            if not isinstance(exp_type, BoolType):
                raise TypeMismatchInStatement(ast)

            local = [[]]
            for VarDecl in ifthenStmt[1]:
                self.visit(VarDecl, local)
            total = local + param
            for Stmts in ifthenStmt[2]:
                self.visit(Stmts, total)
                self.ReturnStatement(Stmts, func, param)

        else_stmt = ast.elseStmt
        local = [[]]
        for VarDecl in else_stmt[0]:
            self.visit(VarDecl, local)
        total = local + param
        for Stmts in else_stmt[1]:
            self.visit(Stmts, total)
            self.ReturnStatement(Stmts, func, param)

    def visitFor(self, ast: For, param):
        func = param[-1][0]
        idx1 = self.lookup(ast.idx1.name, param)

        if isinstance(idx1.mtype.restype, Unknown):
            idx1.mtype.restype = IntType()

        var = self.lookup(ast.expr1.name, param) if isinstance(ast.expr1, Id) \
                else self.lookup(ast.expr1.method.name, param) if isinstance(ast.expr1, CallExpr) else ""
        expr1 = var.mtype.restype if isinstance(var, Symbol) else self.visit(ast.expr1, param)
        if isinstance(expr1, Unknown):
            var.mtype.restype = IntType()

        var = self.lookup(ast.expr2.name, param) if isinstance(ast.expr2, Id) \
                else self.lookup(ast.expr2.method.name, param) if isinstance(ast.expr2, CallExpr) else ""
        expr2 = var.mtype.restype if isinstance(var, Symbol) else self.visit(ast.expr2, param)
        if isinstance(expr2, Unknown):
            var.mtype.restype = BoolType()

        var = self.lookup(ast.expr3.name, param) if isinstance(ast.expr3, Id) \
                else self.lookup(ast.expr3.method.name, param) if isinstance(ast.expr3, CallExpr) else ""
        expr3 = var.mtype.restype if isinstance(var, Symbol) else self.visit(ast.expr3, param)
        if isinstance(expr3, Unknown):
            var.mtype.restype = IntType()

        idx1 = self.visit(ast.idx1, param)
        expr1 = self.visit(ast.expr1, param)
        expr2 = self.visit(ast.expr2, param)
        expr3 = self.visit(ast.expr3, param)
        if "TypeCannotBeInferred" in [expr1, expr2, expr3]:
            raise TypeCannotBeInferred(ast)

        iType = [isinstance(idx1, IntType), isinstance(expr1, IntType), isinstance(expr3, IntType)]
        # print(iType)
        if False in iType:
            raise TypeMismatchInStatement(ast)

        # if type(self.visit(ast.expr2,param)) is not type(BoolType()):
        if not isinstance(expr2, BoolType):
            raise TypeMismatchInStatement(ast)

        local = [[]]
        for VarDecl in ast.loop[0]:
            self.visit(VarDecl, local)
        total = local + param
        for Stmts in ast.loop[1]:
            self.visit(Stmts, total)
            self.ReturnStatement(Stmts, func, param)

    def visitContinue(self, ast: Continue, param):
        pass

    def visitBreak(self, ast: Break, param):
        pass

    def visitReturn(self, ast: Return, param):
        if ast.expr:
            expr_type = self.visit(ast.expr, param)
            if expr_type == "TypeCannotBeInferred" or isinstance(expr_type, Unknown):
                raise TypeCannotBeInferred(ast)
            return self.visit(ast.expr, param)
        else:
            return VoidType()

    def visitDowhile(self, ast: Dowhile, param):
        local = [[]]
        func = param[-1][0]
        for VarDecl in ast.sl[0]:
            self.visit(VarDecl, local)
        total = local + param
        for Stmts in ast.sl[1]:
            self.visit(Stmts, total)
            self.ReturnStatement(Stmts, func, param)


        var = self.lookup(ast.exp.name, param) if isinstance(ast.exp, Id) \
                else self.lookup(ast.exp.method.name, param) if isinstance(ast.exp, CallExpr) else ""
        exp_type = var.mtype.restype if isinstance(var, Symbol) else self.visit(ast.exp, param)

        if isinstance(exp_type, Unknown):
            var.mtype.restype = BoolType()

        exp_type = self.visit(ast.exp, param)
        if exp_type == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)

        if not isinstance(exp_type, BoolType):
            raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast: While, param):
        func = param[-1][0]

        var = self.lookup(ast.exp.name, param) if isinstance(ast.exp, Id) \
                else self.lookup(ast.exp.method.name, param) if isinstance(ast.exp, CallExpr) else ""
        exp_type = var.mtype.restype if isinstance(var, Symbol) else self.visit(ast.exp, param)
        if isinstance(exp_type, Unknown):
            var.mtype.restype = BoolType()


        exp_type = self.visit(ast.exp, param)
        if exp_type == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)

        if not isinstance(exp_type, BoolType):
            raise TypeMismatchInStatement(ast)
        local = [[]]
        for VarDecl in ast.sl[0]:
            self.visit(VarDecl, local)
        total = local + param
        for Stmts in ast.sl[1]:
            self.visit(Stmts, total)
            self.ReturnStatement(Stmts, func, param)

    def visitCallStmt(self, ast: CallStmt, param):
        var = self.lookup(ast.method.name, param)
        if var is not None:
            if not isinstance(var.kind, Function):
                raise Undeclared(Function(),ast.method.name)

            if len(var.mtype.intype) != len(ast.param):
                raise TypeMismatchInStatement(ast)

            if isinstance(var.mtype.restype,Unknown):
                var.mtype.restype = VoidType()

            if not isinstance(var.mtype.restype, VoidType):
                raise TypeMismatchInStatement(ast)

            if var.mtype.intype:
                for i in range(len(ast.param)):
                    param_type = self.visit(ast.param[i], param)
                    if param_type == "TypeCannotBeInferred":
                        raise TypeCannotBeInferred(ast)
                    if isinstance(param_type, Unknown) and isinstance(var.mtype.intype[i], Unknown):
                        raise TypeCannotBeInferred(ast)

                    if isinstance(param_type, Unknown):
                        parameter = self.lookup(ast.param[i].name, param) if isinstance(ast.param[i], Id) \
                            else self.lookup(ast.param[i].method.name, param)
                        parameter.mtype.restype = var.mtype.intype[i]

                    if isinstance(var.mtype.intype[i], Unknown):
                        var.mtype.intype[i] = param_type

                    param_type = self.visit(ast.param[i], param)
                    #print(param_type, var.mtype.intype[i])
                    if type(var.mtype.intype[i]) != type(param_type):
                        raise TypeMismatchInStatement(ast)
        else:
            raise Undeclared(Function(), ast.method.name)

    def visitIntLiteral(self, ast: IntLiteral, param):
        return IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, param):
        return FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, param):
        return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        listdimen = [len(ast.value)]
        for value in ast.value:
            x = self.visit(value,param)
        t = self.visit(ast.value[0],param)
        if isinstance(t,ArrayType):
            listdimen.extend(t.dimen)

        return ArrayType(listdimen,self.visit(ast.value[0],param))
