from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    """def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program([VarDecl(Id(ctx.ID().getText()),[],None)])"""
    #program: var_declare* func_declare*  EOF ;
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        declList = []
        if ctx.var_declare():
            for x in ctx.var_declare():
                declList.extend(self.visitVar_declare(x))
        if ctx.func_declare():
            for x in ctx.func_declare():
                declList.extend(self.visitFunc_declare(x))

        return Program(declList)

    #var_declare: VAR COLON var_list SEMI;
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        varDecl = self.visit(ctx.var_list())
        return [VarDecl(variable, varDimen, varInit) for (variable, varDimen, varInit) in varDecl]

    #var_list: variable (COMMA variable)*;
    def visitVar_list(self, ctx: BKITParser.Var_listContext):
        varList = []
        for x in ctx.variable():
            varList.extend(self.visitVariable(x))

        return varList

    #variable: ID dimen* (ASSIGN literal)?;
    def visitVariable(self, ctx:BKITParser.VariableContext):
        varDimen = []
        varInit = self.visit(ctx.literal()) if ctx.literal() else None
        variable = Id(ctx.ID().getText())
        if ctx.dimen():
            for x in ctx.dimen():
                varDimen.append(self.visitDimen(x))


        return [(variable, varDimen, varInit)]

    #dimen: LSB INT_LIT RSB;
    def visitDimen(self, ctx:BKITParser.DimenContext):
        return int(ctx.INT_LIT().getText(),0)

    #func_declare: FUNC COLON ID (PARA COLON para_list)? BODY COLON  stmts_list ENDBODY DOT;
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.para_list()) if ctx.para_list() else []


        body = self.visit(ctx.stmts_list())

        return [FuncDecl(name, param, body)]

    #para_list: para (COMMA para)*;
    def visitPara_list(self, ctx:BKITParser.Para_listContext):
        paraList = []

        for x in ctx.para():
            paraList.append(self.visitPara(x))

        return paraList


    #para: ID dimen* ;
    def visitPara(self, ctx:BKITParser.ParaContext):
        name = Id(ctx.ID().getText())
        varDimen = []

        if ctx.dimen():
            for x in ctx.dimen():
                varDimen.append(self.visitDimen(x))

        return VarDecl(name, varDimen, None)


    #stmt
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)

    #assign_stmt: (ID | element_expression) ASSIGN exp SEMI;
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        lhs = None
        rhs = self.visit(ctx.exp()) if ctx.exp() else None
        if ctx.element_expression():
            lhs = self.visit(ctx.element_expression())

        if ctx.ID():
            lhs = Id(ctx.ID().getText())

        return Assign(lhs, rhs)


    #if_stmt: IF exp_bool THEN stmts_list elseif* (ELSE stmts_list)? ENDIF DOT;
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        stmtListIf = self.visit(ctx.stmts_list(0))
        stmtListElse = self.visit(ctx.stmts_list(1)) if ctx.stmts_list(1) else []
        ifthenStmt = [(self.visit(ctx.exp_bool()), stmtListIf[0], stmtListIf[1])]
        elseStmt = (stmtListElse[0], stmtListElse[1]) if ctx.stmts_list(1) else ([],[])

        if ctx.elseif():
            for x in ctx.elseif():
                ifthenStmt.extend(self.visitElseif(x))

        return If(ifthenStmt, elseStmt)

    #elseif: ELSEIF exp_bool THEN stmts_list;
    def visitElseif(self, ctx:BKITParser.ElseifContext):
        stmtList = self.visit(ctx.stmts_list())

        return [(self.visit(ctx.exp_bool()), stmtList[0], stmtList[1])]


    #for_stmt: FOR LP ID ASSIGN exp COMMA exp_bool COMMA update_exp RP DO stmts_list ENDFOR DOT;
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        idx = Id(ctx.ID().getText())
        exp1 = self.visit(ctx.exp())
        exp2 = self.visit(ctx.exp_bool())
        exp3 = self.visit(ctx.update_exp())
        loop = self.visit(ctx.stmts_list()) if ctx.stmts_list() else ([],[])

        return For(idx, exp1, exp2, exp3, loop)


    #while_stmt: WHILE exp_bool DO stmts_list ENDWHILE DOT;
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        exp = self.visit(ctx.exp_bool())
        sl = self.visit(ctx.stmts_list())

        return While(exp, sl)


    #do_while_stmt: DO stmts_list WHILE exp_bool ENDDO DOT;
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        sl = self.visit(ctx.stmts_list()) if ctx.stmts_list() else ([],[])
        exp = self.visit(ctx.exp_bool()) if ctx.exp_bool() else None

        return Dowhile(sl,exp)

    #brk_stmt: BREAK SEMI;
    def visitBrk_stmt(self, ctx:BKITParser.Brk_stmtContext):
        return Break()


    #cont_stmt: CONT SEMI;
    def visitCont_stmt(self, ctx:BKITParser.Cont_stmtContext):
        return Continue()


    #call_stmt: ID LP exp_list? RP SEMI;
    def visitCall_stmt(self,ctx:BKITParser.Call_stmtContext):
        method = Id(ctx.ID().getText())
        para: list
        if ctx.exp_list():
            para = self.visit(ctx.exp_list())
        else:
            para = []

        return CallStmt(method, para)

    #ret_stmt: RETURN exp? SEMI;
    def visitRet_stmt(self, ctx:BKITParser.Ret_stmtContext):
        exp = self.visit(ctx.exp()) if ctx.exp() else None
        return Return(exp)

    def visitExp_bool(self, ctx:BKITParser.Exp_boolContext):
        return self.visitChildren(ctx)

    def visitExp_int(self, ctx:BKITParser.Exp_intContext):
        return self.visitChildren(ctx)

    def visitExp_float(self, ctx:BKITParser.Exp_floatContext):
        return self.visitChildren(ctx)

    def visitExp_str(self, ctx:BKITParser.Exp_strContext):
        return self.visitChildren(ctx)

    def visitUpdate_exp(self, ctx:BKITParser.Update_expContext):
        return self.visitChildren(ctx)


    #exp: exp1 ( EQU| NEQU | GT | LT | GTE | LTE | NEQUF | GTF | GTEF | LTF | GTEF | LTEF) exp1 | exp1;
    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.getChildCount() == 1: #exp1
            return self.visit(ctx.exp1(0)) if ctx.exp1() else None
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.exp1(0)) if ctx.exp1() else None
        right = self.visit(ctx.exp1(1)) if ctx.exp1() else None

        return BinaryOp(op, left, right)

    #exp1: exp1 (AND | OR) exp2 | exp2;
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())

        op = ctx.getChild(1).getText()
        left = self.visit(ctx.exp1())
        right = self.visit(ctx.exp2())

        return BinaryOp(op, left, right)

    #exp2: exp2 (ADD | ADDFLOAT | SUB | SUBFLOAT) exp3 | exp3 ;
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())

        op = ctx.getChild(1).getText()
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())

        return BinaryOp(op, left, right)

    #exp3: exp3 ( DIV | MUL | DIVFLOAT | MULFLOAT | MOD ) exp4 | exp4;
    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())

        op = ctx.getChild(1).getText()
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())

        return BinaryOp(op, left, right)

    #exp4: NOT exp4 | exp5;
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())

        op = ctx.NOT().getText()
        body = self.visit(ctx.exp4())

        return UnaryOp(op, body)

    #exp5: (SUB| SUBFLOAT) exp5 | operands;
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())

        op = ctx.getChild(0).getText()
        body = self.visit(ctx.exp5())

        return UnaryOp(op, body)

    #operands: literal | ID | element_expression | call_exp | LP exp RP;
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        else:
            if ctx.ID():
                return Id(ctx.ID().getText())
            else:
                return self.visitChildren(ctx)

    #index_operators: LSB exp RSB index_operators | LSB exp RSB;
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        idx = []
        if ctx.getChildCount() == 3:
            #idx.append(self.visit(ctx.exp()))
            exp = self.visit(ctx.exp())
            if isinstance(exp, list):
                idx.extend(exp if exp else [])
            else:
                idx.append(exp)
        else:
            #idx.append(self.visit(ctx.exp()))
            exp = self.visit(ctx.exp())
            if isinstance(exp, list):
                idx.extend(exp if exp else [])
            else:
                idx.append(exp)
            idx.extend(self.visit(ctx.index_operators()))

        return idx

    #element_expression: (ID | call_exp) index_operators;
    def visitElement_expression(self,ctx:BKITParser.Element_expressionContext):
        arr = Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.call_exp())
        idx = self.visit(ctx.index_operators())

        return ArrayCell(arr, idx)

    #call_exp: ID LP exp_list? RP;
    def visitCall_exp(self,ctx:BKITParser.Call_stmtContext):
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.exp_list()) if ctx.exp_list() else []
        return CallExpr(method, param)


    #stmts_list: var_declare* stmt*;
    def visitStmts_list(self, ctx:BKITParser.Stmts_listContext):
        varDecl = []
        stmt = []
        if ctx.var_declare():
            for x in ctx.var_declare():
                varDecl.extend(self.visitVar_declare(x))

        if ctx.stmt():
            for x in ctx.stmt():
                stmt.append(self.visitStmt(x))

        return (varDecl, stmt)


    #exp_list: exp (COMMA exp)*;
    def visitExp_list(self, ctx:BKITParser.Exp_listContext):
        return [self.visitExp(x) for x in ctx.exp()]




    #literal: INT_LIT | FLOAT_LIT | STRING_LIT | bool_lit | array_lit;
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText(),0))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(str(ctx.STRING_LIT().getText()))
        if ctx.bool_lit():
            return self.visit(ctx.bool_lit())
        if ctx.array_lit():
            return self.visit(ctx.array_lit())

    #bool_lit: TRUE | FALSE;
    def visitBool_lit(self, ctx:BKITParser.Bool_litContext):
        val = True if ctx.TRUE() else False
        return BooleanLiteral(val)

    #array_lit: LCB literal (COMMA literal)* RCB;
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        value = []
        if ctx.literal():
            for x in ctx.literal():
                value.append(self.visitLiteral(x))

        return ArrayLiteral(value)


