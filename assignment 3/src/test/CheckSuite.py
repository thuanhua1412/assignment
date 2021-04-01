import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """
        Function: main
                   Body:
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))


    def test_Redeclare1(self):
        """Complex program"""
        input = """
        Var:x[2] = {0,1};
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: x;
            Var: x;
        EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_Redeclare2(self):
        """Complex program"""
        input = """
        Var:x[2] = {0,1};
        Function: main 
        Parameter: a,b,c,a
        Body:
        EndBody."""
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_Redeclare3(self):
        """Complex program"""
        input = """
        Var:x[2] = {0,1};
        
        Function: foo
        Body:
        EndBody.
        
        Function: main 
        Parameter: a,b,c
        Body:
        EndBody.
        
        Function: foo
        Body:
        EndBody."""
        expect = str(Redeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_Redeclare4(self):
        """Complex program"""
        input = """
        Var:x[2] = {0,1};
        Function: main 
        Parameter: a,b,c
        Body:
            Var: x;
            foo(1,2);
        EndBody.
        Function: foo
        Parameter: a,b
        Body:
            Var: x;
            Return ;
        EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_NoEntryPoint(self):
        """Complex program"""
        input = """
        Var:x[2] = {0,1};
        Function: men 
        Parameter: a,b,c 
                   Body:
                   EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_Undeclare1(self):
        """Complex program"""
        input = """
        Var:x[2] = {0,1};
        Function: main 
        Parameter: a,b,c 
        Body:
            i = i+1;
        EndBody."""
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_Undeclare2(self):
        input = """
        Function: main
        Body:
            Var:a;
            a = foo;
        EndBody.

        Function: foo
        Parameter: x
        Body:
            Return x+5;
        EndBody.
        """
        expect = str(Undeclared(Identifier(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_Undeclare3(self):
        input = """
        Function : printprint
        Parameter : x
        Body:
            Return;
        EndBody.

        Function: m
        Body:
            Var : value = 12345;
            Return value;
        EndBody.

        Function: main
        Parameter : x, y
        Body: 
            printprint(m); 
            Return 0;
        EndBody."""

        expect = str(Undeclared(Identifier(), "m"))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_Undeclare4(self):
        input = """
        Function: main
        Parameter : x, y
        Body: 
            saw(x); 
            Return 0;
        EndBody."""

        expect = str(Undeclared(Function(), "saw"))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_Undeclare5(self):
        input = """
        Function: main
        Parameter : x, y
        Body: 
            x = saw("string") + 1; 
            Return 0;
        EndBody.
        Function: saw
        Parameter: x
        Body:
            x = "abc";
            Return 10;
        EndBody."""

        expect = ""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_TypeMisMatchIf1(self):
        input = """
        Var:x = 10;
        Function: main 
        Parameter: a,b,c 
                   Body:
                   If 10 Then
                   EndIf.
                   EndBody."""
        expect = str(TypeMismatchInStatement(If([(IntLiteral(10),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_TypeMisMatchIf2(self):
        input = """
        Var:x = 10;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: m;
            If m Then
            EndIf.
        EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_TypeMisMatchIf3(self):
        input = """
        Var:x = 10;
        Function: main 
        Parameter: a,b,c 
        Body:
            If x Then
            EndIf.
        EndBody."""
        expect = str(TypeMismatchInStatement(If([(Id("x"),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_TypeMisMatchIf4(self):
        input = """
        Var:x = 10;
        Function: main 
        Parameter: a,b,c 
        Body:
            b = 20;
            c = b > x;
            a = (x + 2) > b;
            If c Then
                Var: x;
            ElseIf a Then
            Else 
            EndIf.
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_TypeMisMatchIf5(self):
        input = """
        Var:x = 10;
        Function: main 
        Parameter: a,b,c 
        Body:
            b = 20;
            c = b + x;
            If c Then
            EndIf.
        EndBody."""
        expect = str(TypeMismatchInStatement(If([(Id("c"), [],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_TypeMisMatchIf6(self):
        input = """
        Var:x = 10;
        Function: main 
        Parameter: a,b,c 
        Body:
            b = 20;
            c = b > x;
            If c Then
            ElseIf b Then
            Else
            EndIf.
        EndBody."""
        expect = str(TypeMismatchInStatement(If([(Id("c"),[],[]),(Id("b"),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_TypeMisMatchIf7(self):
        input = """
        Var:x = 10;
        Function: main 
        Parameter: a,b,c 
        Body:
            b = 20;
            c = b > x;
            Do
                For (x = 1, True,2) Do
                    If c Then
                    ElseIf b Then
                    Else
                    EndIf.
                EndFor.            
            While False EndDo.
        EndBody."""
        expect = str(TypeMismatchInStatement(If([(Id("c"),[],[]),(Id("b"),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,422))


    def test_TypeMisMatchFor1(self):
        input = """
        Var: x = 10;
        Function: main 
        Parameter: a,b,c 
        Body:
            If True Then
                Var: x;
                Return 10;
            ElseIf False Then
                Var: x = False;
                Return 50;
            Else
                Var: x = 1.2;
                For (x = 1, True,2) Do
                    Return 10;
                EndFor.        
            EndIf.   
        EndBody."""
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BooleanLiteral(True),IntLiteral(2),([],[Return(IntLiteral(10))]))))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_TypeMisMatchFor2(self):
        input = """
        Var:x = 2;
        Function: main 
        Parameter: a,b,c 
        Body:
            For (x = 1.5, True,2) Do
            EndFor.            
        EndBody."""
        expect = str(TypeMismatchInStatement(For(Id("x"),FloatLiteral(1.5),BooleanLiteral(True),IntLiteral(2),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_TypeMisMatchFor3(self):
        input = """
        Var:x = 2;
        Function: main 
        Parameter: a,b,c 
        Body:
            For (x = 15, 10,2) Do
            EndFor.            
        EndBody."""
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(15),IntLiteral(10),IntLiteral(2),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_TypeMisMatchFor4(self):
        input = """
        Var:x = 2;
        Function: main 
        Parameter: a,b,c 
        Body:
            For (x = 15, False,True) Do
            EndFor.            
        EndBody."""
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(15),BooleanLiteral(False),BooleanLiteral(True),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_TypeMisMatchFor5(self):
        input = """
        Var:x;
        Function: main 
        Parameter: a,b,c 
        Body:
            For (x = a, b,2) Do
            EndFor.            
        EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_TypeMisMatchFor6(self):
        input = """
        Var:x = 10;
        Function: main 
        Parameter: a,b,c 
        Body:
            If True Then
                Var: x;
                Return 10;
            ElseIf False Then
                Var: x = False;
                Return 50;
            Else
                Var: x;
                Var: y;
                Var: z;
                Var: t;
                For (x = t, y,z) Do
                    If True Then 
                        While True Do
                            Do Return 2.4; While y
                            EndDo.
                        EndWhile. 
                    EndIf.
                EndFor.         
            EndIf.   
        EndBody."""
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(2.4))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_TypeMisMatchWhile1(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: x;
            While True Do
                Var: x;
            EndWhile. 
        EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_TypeMisMatchWhile2(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            While 12 Do
            EndWhile. 
        EndBody."""
        expect = str(TypeMismatchInStatement(While(IntLiteral(12),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_TypeMisMatchWhile3(self):
        input = """
        Var:x ;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: x; 
            While a Do
                Var: x;
                Do
                    Var: x;
                While x EndDo.
            EndWhile. 
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_TypeMisMatchDoWhile1(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: x;
            Do
                Var: x;
            While False EndDo.
        EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_TypeMisMatchDoWhile2(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: x;
            Do
            **do nothing here**
            Var: x;
            While "boolean" EndDo.
        EndBody."""
        expect = str(TypeMismatchInStatement(Dowhile(([VarDecl(Id("x"),[],[])],[]),StringLiteral("boolean"))))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_TypeMisMatchAssign1(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y = True;
            x = y;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_TypeMisMatchAssign2(self):
        input = """
        Var:x[2] = {1,2},y[2] = {1.2,2.4};
        Function: main 
        Parameter: a,b,c 
        Body:
            x = y;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_TypeMisMatchAssign3(self):
        input = """
        Var:x[2] = {1,2},y[3];
        Function: main 
        Parameter: a,b,c 
        Body:
            x = y;
            Return 1;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,436))


    def test_TypeMisMatchAssign4(self):
        input = """
        Var:xx[2][3] = {{1,2,3},{1,2,3}}, y[2][3];
        Function: main 
        Parameter: a,b,c 
        Body:
            y = xx;
            Return 1;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_TypeMisMatchAssign5(self):
        input = """
        Var:x[2][3] = {{1,2,3},{1,2,3}}, y[2][4];
        Function: main 
        Parameter: a,b,c 
        Body:
            x = y;
            Return 1;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_TypeMisMatchAssign6(self):
        input = """
        Var:x[2][3] = {{1,2,3},{1,2,3}}, y[2][3];
        Function: main 
        Parameter: a,b,c 
        Body:
            y[0][1] = x[a][b];
            y = x;
            Return 1;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_undeclared_function23(self):
        """Simple program: main"""
        input = """

        Function: foo
        Body:
        Var: a[3][4];
        Return a;
        EndBody.
        Function: main
        Body:
        foo()[0][2] = True;
        foo()[1][2] = True;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('a'))))
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_TypeMisMatchAssign8(self):
        input = """
        Var:x[2][3], y[2][3];
        Function: main 
        Parameter: a,b,c 
        Body:
            y = x;
            Return 1;
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("y"),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_TypeMisMatchAssign9(self):
        input = """
        Var:x[2][3], y[2][3];
        Function: main 
        Parameter: a,b,c 
        Body:
            y[0] = {1,2};
            y = x;
            Return 1;
        EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id('y'),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,442))


    def test_undeclared_function9(self):
        """Simple program: main"""
        input = """
        Var: x = 6,y =7.5,z = True;
        Function: a
        Parameter: x,y,z
        Body:
        Var: a;
        a = {4,5,6};
        EndBody.
        Function: main
        Body: 
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('a'),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)]))))
        self.assertTrue(TestChecker.test(input,expect,443))


    def test_TypeMisMatchAssign11(self):
        input = """
        Var:x[2][3], y[2][3];
        Function: foo
        Parameter: x[3]
        Body:
            x = {1,2,3};
            Return x;
        EndBody.

        Function: main 
        Parameter: a,b,c 
        Body:
            Return 1;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_TypeMisMatchCallStmt1(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y = True;
            a = 2;
            a = b;
            call(a,b);
        EndBody.
        
        Function: call
        Parameter: a,b
        Body:
            Return ;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_TypeMisMatchCallStmt2(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y = True;
            a = 2;
            a = b;
            Do
                call(1,b,3);
            While True EndDo.
        EndBody.

        Function: call
        Parameter: a,b
        Body:
            Return ;
        EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("call"),[IntLiteral(1),Id("b"),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_TypeMisMatchCallStmt3(self):
        input = """
        Var:x = 25;
        Function: call
        Parameter: a,b
        Body:
            a = 10;
            b = "str";
            Return ;
        EndBody.
        
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y = True;
            a = 2;
            a = b;
            Do
                call(a,b);
            While True EndDo.
        EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("call"),[Id("a"),Id("b")])))
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_TypeMisMatchCallStmt4(self):
        input = """
        Var:x = 25;
        Function: call
        Parameter: a,b,c
        Body:
            a = 10;
            b = "str";
            c = False;
            Return ;
        EndBody.

        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y = True;
            a = 2;
            a = b;
            Do
                call(a,c,y);
            While True EndDo.
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_TypeMisMatchReturn1(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y = True;
            a = 2;
            a = b;
            For (x = 1, True,2) Do
                call(a,1,y);
            EndFor.            
        EndBody.
        
        Function: call
        Parameter: a,b,c
        Body:
            Return 10;
        EndBody."""
        expect = str(TypeMismatchInStatement(Return(IntLiteral(10))))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_TypeMisMatchReturn2(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y = True;
            a = 2;
            a = b;
            For (x = 1, True,2) Do
                a = call(a,1,y);
            EndFor.            
        EndBody.

        Function: call
        Parameter: a,b,c
        Body:
            Return 10;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_TypeMisMatchReturn3(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y = True;
            a = 2;
            a = b;
            For (x = 1, True,2) Do
                call(a,1,y);
            EndFor.            
        EndBody.

        Function: call
        Parameter: a,b,c
        Body:
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_TypeMisMatchReturn4(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a[2][3],b,c 
        Body:
            Var: y = True;
            a = {{1,2,3},{4,5,6}};
            b = "string";
            For (x = 1, True,2) Do
                a = call(2,1,True);
            EndFor.            
        EndBody.

        Function: call
        Parameter: a,b,c
        Body:
            Var: x[3] = {1,2,4};
            Var: y[2][3];
            y[1][1] = x[1];
            Return y;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_TypeMisMatchExprArrayIndexing1(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a[2][3],b,c 
        Body:
            For (x = 1, True,2) Do
                Var: y = True;
                a = {{1,2,3},{4,5,6}};
                c = a[1][1.]+ a[2][2];
                b = "string";
            EndFor.            
        EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"),[IntLiteral(1),FloatLiteral(1.)])))
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_TypeMisMatchExprArrayIndexing2(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a[2][3],b,c 
        Body:
            For (x = 1, True,2) Do
                Var: y = True;
                a = {{1,2,3},{4,5,6}};
                c = a[1][1][3]+ a[2][2];
                b = "string";
            EndFor.            
        EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_TypeMisMatchExprArrayIndexing3(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a[2][3][1],b,c 
        Body:
            For (x = 1, True,2) Do
                Var: y = True;
                a = {{{1},{2},{3}},{{4},{5},{6}}};
                c = a[1][1][0]+ a[2][2][1];
                a[1][2] = {1};
                b = "string";
            EndFor.            
        EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_TypeMisMatchCallExpr1(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y;
            For (x = 1, True,2) Do
                Var: y = True;
                a = foo(1,4.5) +. 2.9;
            EndFor.            
        EndBody.
        
        Function:foo
        Parameter:m,n
        Body:
            Var: x;
            Var: y;
            x  = m + 1;
            y = 10.0 >.n;
            Return 10.2;
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_TypeMisMatchCallExpr2(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y;
            For (x = 1, True,2) Do
                Var: y = True;
                a = foo(1,4.5, True) +. 2.9;
            EndFor.            
        EndBody.

        Function:foo
        Parameter:m,n
        Body:
            Var: x;
            Var: y;
            x  = m + 1;
            y = 10.0 >.n;
            Return 10.2;
        EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1),FloatLiteral(4.5),BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_TypeMisMatchCallExpr3(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y;
            For (x = 1, True,2) Do
                Var: y = True;
                a = foo(1,4.5, True) +. 2.9;
            EndFor.            
        EndBody.

        Function:foo
        Parameter:m,n,p
        Body:
            Var: x;
            Var: y;
            x  = m + 1;
            y = 10.0 >.n;
            p = "True";
            Return 10.2;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("p"),StringLiteral("True"))))
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_TypeMisMatchCallExpr4(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y;
            For (x = 1, True,2) Do
                Var: y = True;
                a = foo(1,4.5, True) +. 2.9;
            EndFor.            
        EndBody.

        Function:foo
        Parameter:m,n
        Body:
            Var: x;
            Var: y;
            x  = m + 1;
            y = 10.0 >.n;
            Return 10.2;
        EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1),FloatLiteral(4.5),BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_TypeMisMatchCallExpr5(self):
        input = """
        Var:x = 25;
        Function:foo
        Parameter:m,n
        Body:
            Var: x;
            Var: y;
            x  = m + 1;
            y = 10.0 >.n;
            Return 10.2;
        EndBody.
        
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y;
            For (x = 1, True,2) Do
                Var: y = True;
                a = foo(1,4) +. 2.9;
            EndFor.            
        EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_TypeMisMatchCallExpr6(self):
        input = """
        Var:x = 25;
        Function:fofofo
        Parameter:m,n
        Body:
            Var: x;
            Var: y;
            x  = m + 1;
            y = 10.0 >.n;
            Return 10.2;
        EndBody.

        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y;
            For (x = 1, True,2) Do
                Var: y = True;
                a = fofofo(a,b) +. 2.9;
            EndFor.            
        EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("fofofo"),[Id("a"),Id("b")])))
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_TypeCannotBeInferredAssign1(self):
        input = """
        Var:x = 25;
        Function: main 
        Parameter: a,b,c 
        Body:
            Var: y = True;
            a = b;
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_TypeCannotBeInferredAssign2(self):
        input = """
        Function: main
    Body:
        foo()[0] = 1; **1**
    EndBody.

Function: foo
    Body:
        Return 0; **2**
    EndBody."""
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_TypeCannotBeInferredAssign3(self):
        input = """
        Var:x[2],y[2];
        Function: main 
        Parameter: a,b,c 
        Body:
            x = y;
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_TypeCannotBeInferredAssign4(self):
        input = """
        Function: main
        Body:
            foo()[1][2] = 3;    
        EndBody.

        Function: foo
        Body:
            Return {{1,2,3},{4,5,6}};
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(1),IntLiteral(2)]),IntLiteral(3))))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test1(self):
        input = """
        Function: main
        Body:
            Var: x;
            x = x + foo();
        EndBody.

        Function: foo
        Body:
            Return "string";
        EndBody."""
        expect = str(TypeMismatchInStatement(Return(StringLiteral("string"))))
        self.assertTrue(TestChecker.test(input,expect,464))

    def test2(self):
        input = """
            Var:k;
            Function: foo_0
            Parameter:x,y,z
            Body:
            EndBody.
            
            Function: main
            Parameter:x,y
            Body:
                If foo_0(1,2,3)[1][2] Then
                EndIf.
            EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id("foo_0"),
                                                                 [IntLiteral(1),IntLiteral(2),IntLiteral(3)]),
                                                        [IntLiteral(1),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test3(self):
        input = """
            Var:k;
            Function: foo
            Body:
                Return {1,2,4};
            EndBody.

            Function: main
            Parameter:x,y
            Body:
                foo()[1] = 1;
            EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test4(self):
        input = """
        Function: main
        Body:
            foo()[1][2] = 3;    
        EndBody.   

        Function: foo
        Body:
            Return {{1,2,3},{4,5,6}};
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(1),IntLiteral(2)]),IntLiteral(3))))
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test5(self):
        input = """
        Var:test[2][2][3] = {{{1,2,3},{2,3,4}},{{1,2,3},{2,3,4}}},y[2][2][3] = {{{1.,2.,3.},{2.,3.,4.}},{{1.,2.,3.},{2.,3.,4.}}};
        Function: main 
        Parameter: a,b,c 
        Body:
            test = y;
            Return 1;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("test"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,468))

    def testTypeMisMatchExpr1(self):
        input = """
        Var: x,y;
        Function: main
        Parameter:a,b[2],c[3],d
        Body:
            a = x+y;
            b = c;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("b"),Id("c"))))
        self.assertTrue(TestChecker.test(input,expect,469))

    def testTypeMisMatchExpr2(self):
        input = """
        Var: x,y;
        Function: main
        Parameter:a,b[2],c[2],d
        Body:
            a = x+y;
            b = {1,2};
            c = {1,2};
            a = x+.y;
        EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test6(self):
        input = """
        Function: main
        Parameter: a,b,c
        Body:
            Var: d, e;
            e = main(b, main(d, c, a), a + d);
            e = 3.0;
            Return 3;
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("e"),
                                                 CallExpr(Id("main"),[Id("b"),CallExpr(
                                                     Id("main"),[Id("d"),Id("c"),Id("a")]),
                                                                      BinaryOp("+",Id("a"),Id("d"))]))))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test7(self):
        input = """
        Var: test;
        Function: main
        Parameter: x
        Body:
            x = test[0];
        EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("test"),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test8(self):
        input = """
        Function: main
        Body:
            Var: x, y;
            x = foo(1,2) +. x;
        EndBody.

        Function: foo
        Parameter: x,y
        Body:
            y = 1.0;
            Return 1;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("y"),FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test9(self):
        input = """
              Function: main
            Parameter: x, y ,z
            Body:
            y = x || (x>z);
            EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp(">",Id("x"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,474))

    def test10(self):
        input = """
        Function: foooo
        Parameter: x
        Body:
            x=1.1;
            Return { True };
        EndBody.
        Function: main
        Parameter: x, y
        Body:
            foooo(x)[0] = False;
        EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test11(self):
        input = """
        Var: a;
        Function: main
        Body:
            foo();
            a = 1;

        EndBody.

        Function: foo
        Body:
            a = 1.1;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('a'), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,476))


    def test13(self):
        input = """
        Function: main
        Body:
            Var: a;
            a = 1 + foo123(3.5);
        EndBody.
        
        Function: foo123
        Parameter: x
        Body:
            Return x + 5;
        EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("x"),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,478))

    def test17(self):
        input = """
        Var: a[2][2], b[2];
        Function: main
        Body:
            a = {{1,2},{3,4}};
            b = a[2];
        EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test18(self):
        input = """
        Var: a[2][2], b[2];
        Function: main
        Body:
            Var:x;
            x();
        EndBody."""
        expect = str(Undeclared(Function(),"x"))
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_TypeCannotBeInferred1(self):
        input = """
        Var: a, b[2];
        Function: main
        Body:
            Var: x,y;
            y = a + foo(x);
        EndBody.
        
        Function:foo
        Parameter: x
        Body:
        
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("y"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id('x')])))))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_TypeCannotBeInferred2(self):
        input = """
        Var: a, b[2];
        Function: main
        Body:
            Var: x,y;
            If foo(x) Then
            Else
            EndIf.
        EndBody.

        Function:foo
        Parameter: x
        Body:

        EndBody."""
        expect = str(TypeCannotBeInferred(If([(CallExpr(Id("foo"),[Id("x")]),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_TypeCannotBeInferred3(self):
        input = """
        Var: a, b[2];
        Function: main
        Body:
            Var: x,y;
            If x Then
            Else
            EndIf.
        EndBody.

        Function:foo
        Parameter: x
        Body:
            x = 10;
            Return foo(1)[1];
        EndBody."""
        expect = str(TypeCannotBeInferred(Return(ArrayCell(CallExpr(Id("foo"),[IntLiteral(1)]),[IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_TypeCannotBeInferred4(self):
        input = """
        Var: a, b[2];
        Function: main
        Body:
            Var: x,y;
            If x Then
                foo(x,y,1);
            Else
            EndIf.
        EndBody.

        Function:foo
        Parameter: x,y,z
        Body:
        EndBody."""
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x"),Id("y"),IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_TypeCannotBeInferred5(self):
        input = """
        Var: a, b[2];
        Function: main
        Body:
            Var: x,y;
            If x Then
                foo(test(1),2);
            Else
            EndIf.
        EndBody.

        Function:foo
        Parameter: x,y
        Body:
        EndBody.
        
        Function: test
        Parameter: x
        Body:
        EndBody."""
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[CallExpr(Id("test"),[IntLiteral(1)]),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_TypeCannotBeInferred6(self):
        input = """
        Var: a, b[2];
        Function: main
        Body:
            Var: x,y;
            If x Then
                a = foo(1,2);
            Else
            EndIf.
        EndBody.

        Function:foo
        Parameter: x,y
        Body:
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_TypeCannotBeInferred7(self):
        input = """
        Var: a, b[2];
        Function: main
        Body:
            Var: x[2][2],y;
            If True Then
                x = foo(1,2);
            Else
            EndIf.
        EndBody.

        Function:foo
        Parameter: x,y
        Body:
            Return {{1,2},{1,2}};
        EndBody."""

        expect = str(TypeCannotBeInferred(Assign(Id("x"),CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_TypeCannotBeInferred8(self):
        input = """
        Var: a, b[2];
        Function: main
        Body:
            Var: xyz[2][2],y;
            If True Then
                xyz = {{1.2,2.3},{3.4,3.5}};
                xyz = foo(1,2);
            Else
            EndIf.
        EndBody.

        Function:foo
        Parameter: x,y
        Body:
            Return {{1,2},{1,2}};
        EndBody."""

        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]), ArrayLiteral([IntLiteral(1),IntLiteral(2)])]))))
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test19(self):
        input = """
        Function: main
        Body:
            Var: foo = 0x12AF;
            printLn();
            print("string");
            printStrLn("string");
            foo = int_of_float(1e-5);
            foo = foo + foo();
        EndBody.
        Function: foo
        Body:
            Return True;
        EndBody."""

        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test20(self):
        input = """
        Function: main
        Parameter: x
        Body:
            Var: a[1];
            f1(f2(x))[0] = a[f2(f1(x))];
        EndBody.
        
        Function: f1
        Parameter: x
        Body:
        EndBody.
        
        Function: f2
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id("f1"),[CallExpr(Id("f2"),[Id("x")])]),[IntLiteral(0)]),
                                                 ArrayCell(Id("a"),[CallExpr(Id("f2"),[CallExpr(Id("f1"),[Id("x")])])]))))
        self.assertTrue(TestChecker.test(input,expect,493))

    def test21(self):
        input = """
            Function: foo
            Parameter: x, y
            Body:
                Var: z;
                While (True) Do
                    z = foo(1, foo(x, True));
                EndWhile.
                Return y && z;
            EndBody.
            
            Function: main
            Body:
            EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("z"), CallExpr(Id("foo"),[IntLiteral(1),CallExpr(Id("foo"),[Id("x"), BooleanLiteral(True)])]))))
        self.assertTrue(TestChecker.test(input,expect,494))

    def test22(self):
        input = """
            Function: foo
            Parameter: x, y
            Body:
                Return y;
            EndBody.

            Function: main
            Body:
                Var: x;
            EndBody."""
        expect = str(TypeCannotBeInferred(Return(Id("y"))))
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test23(self):
        input = """
            Function: foo
            Parameter: x, y
            Body:
                Return 1;
            EndBody.

            Function: main
            Body:
                Var: print;
                print();
            EndBody."""
        expect = str(Undeclared(Function(),"print"))
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test24(self):
        input = """
            Function: foo
            Parameter: x, y
            Body:
                Return 1;
            EndBody.

            Function: main
            Body:
                Var: foo;
                If True
                Then foo = foo + foo();
                EndIf.
            EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test25(self):
        #inffer for this test again
        input = """
        Function: main
        Parameter: x
        Body:
            Var: a[2],b,c,d;
            **For (a = 1, main(main(5)), c) Do EndFor.**
            If main(main(5)) Then EndIf.
            **Do While main(main(5)) EndDo.**
        EndBody."""

        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test26(self):
        #inffer for this test again
        input = """
        Function: main
        Parameter: x
        Body:
            Var: a,b,c,d;
            For (a = 1, main(main(5)), c) Do EndFor.
        EndBody."""

        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,499))

    def test27(self):
        #inffer for this test again
        input = """
        Function: main
        Parameter: x
        Body:
            Var: a[2],b,c,d;
            Do While main(main(5)) EndDo.
        EndBody."""

        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,500))

    def test28(self):
        #inffer for this test again
        input = """
        Function: main
        Parameter: x
        Body:
            Var: a,b,c,d;
            a = b +. main(main(5));
        EndBody."""

        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[IntLiteral(5)])))
        self.assertTrue(TestChecker.test(input,expect,501))