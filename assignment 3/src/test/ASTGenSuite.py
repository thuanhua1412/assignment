import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_1(self):
        input = """Var:x,y,z;"""
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_2(self):
        input = """Var: x[2][3]= {{2,3,4},{4,5,6}};"""
        expect = Program([VarDecl(Id("x"), [2, 3], ArrayLiteral(
            [ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]),
             ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_3(self):
        input = """Var:x; Var:y;"""
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_4(self):
        input = """Var:x=10;"""
        expect = Program([VarDecl(Id("x"), [], IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_5(self):
        input = """Var: x[2]= 5;"""
        expect = Program([VarDecl(Id("x"), [2], IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_var_declare_06(self):
        input = """Var: a[5] = {1,4,3,2,0};
                Var: b[2][3]={{1,2,3},{4,5,6}};
                """
        expect = Program([VarDecl(Id("a"), [5], ArrayLiteral(
            [IntLiteral(1), IntLiteral(4), IntLiteral(3), IntLiteral(2), IntLiteral(0)])), VarDecl(Id("b"), [2, 3],
                                                                                                   ArrayLiteral([
                                                                                                                    ArrayLiteral(
                                                                                                                        [
                                                                                                                            IntLiteral(
                                                                                                                                1),
                                                                                                                            IntLiteral(
                                                                                                                                2),
                                                                                                                            IntLiteral(
                                                                                                                                3)]),
                                                                                                                    ArrayLiteral(
                                                                                                                        [
                                                                                                                            IntLiteral(
                                                                                                                                4),
                                                                                                                            IntLiteral(
                                                                                                                                5),
                                                                                                                            IntLiteral(
                                                                                                                                6)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_var_declare_07(self):
        input = """Var: m[10][10][10] = {"abc",123};"""
        expect = Program([VarDecl(Id("m"), [10, 10, 10], ArrayLiteral([StringLiteral("abc"), IntLiteral(123)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_var_declare_08(self):
        input = """Var: a = 0x15, b = 0X16, c = 0o17, d = 0O20;"""
        expect = Program([VarDecl(Id("a"), [], IntLiteral(21)), VarDecl(Id("b"), [], IntLiteral(22)),
                          VarDecl(Id("c"), [], IntLiteral(15)), VarDecl(Id("d"), [], IntLiteral(16))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_var_declare_09(self):
        input = """Var: m = 5, m = 6, m = 7;"""
        expect = Program([VarDecl(Id("m"), [], IntLiteral(5)), VarDecl(Id("m"), [], IntLiteral(6)),
                          VarDecl(Id("m"), [], IntLiteral(7))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_var_declare_10(self):
        input = """Var: x = {1, 2.0, True, "3", {4, 5, {6, 7}}};"""
        expect = Program([VarDecl(Id("x"), [], ArrayLiteral(
            [IntLiteral(1), FloatLiteral(2.0), BooleanLiteral(True), StringLiteral("3"),
             ArrayLiteral([IntLiteral(4), IntLiteral(5), ArrayLiteral([IntLiteral(6), IntLiteral(7)])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))


    def test_function_declare_01(self):
        input = """Function: fact
                Body:
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_funcDeclar2(self):
        input = """Var: x = 5;
                Function: main
                Body:
                Var: x,y;
                x=x+1;
                y=y+2;
                EndBody.
                """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[],([VarDecl(Id(x)),VarDecl(Id(y))][Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1))),Assign(Id(y),BinaryOp(+,Id(y),IntLiteral(2)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_funcDeclar3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [VarDecl(Id("a"), [5, 9, 3], []), VarDecl(Id("b"), [7], [])], ([], []))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_funcDeclar4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [VarDecl(Id("a"), [5, 9, 3], []), VarDecl(Id("b"), [7], [])],
                     ([VarDecl(Id("m"), [], [])], []))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_funcDeclar5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m = 10;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [VarDecl(Id("a"), [5, 9, 3], []), VarDecl(Id("b"), [7], [])],
                     ([VarDecl(Id("m"), [], IntLiteral(10))], []))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_funcDeclar6(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m[10][8] = {10.0,10.2};
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[5,9,3]),VarDecl(Id(b),[7])],([VarDecl(Id(m),[10,8],ArrayLiteral(FloatLiteral(10.0),FloatLiteral(10.2)))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_funcDeclar7(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m[10][8] = {10.0};
        Var: a = 1;
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[5,9,3]),VarDecl(Id(b),[7])],([VarDecl(Id(m),[10,8],ArrayLiteral(FloatLiteral(10.0))),VarDecl(Id(a),IntLiteral(1))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_expression_03(self):
        input = """Function: fact
                Body:
                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Assign(Id("v"), BinaryOp("*.", BinaryOp("*.", BinaryOp("*.",
                                                                                                                BinaryOp(
                                                                                                                    "*.",
                                                                                                                    BinaryOp(
                                                                                                                        "\.",
                                                                                                                        FloatLiteral(
                                                                                                                            4.0),
                                                                                                                        FloatLiteral(
                                                                                                                            3.0)),
                                                                                                                    FloatLiteral(
                                                                                                                        3.14)),
                                                                                                                Id(
                                                                                                                    "r")),
                                                                                                 Id("r")),
                                                                                  Id("r")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_expression_04(self):
        input = """Function: fact
                Body:
                    v = -foo(2) * 5 - 3;
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Assign(Id("v"), BinaryOp("-", BinaryOp("*", UnaryOp("-",
                                                                                                             CallExpr(
                                                                                                                 Id(
                                                                                                                     "foo"),
                                                                                                                 [
                                                                                                                     IntLiteral(
                                                                                                                         2)])),
                                                                                                IntLiteral(5)),
                                                                                  IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_expression_05(self):
        input = """Function: fact
                Body:
                    v = func()[5];
                EndBody.
                """
        expect = Program(
            [FuncDecl(Id("fact"), [], ([], [Assign(Id("v"), ArrayCell(CallExpr(Id("func"), []), [IntLiteral(5)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_expression_06(self):
        input = """Function: fact
                Body:
                    v = 5 + func();
                EndBody.
                """
        expect = Program(
            [FuncDecl(Id("fact"), [], ([], [Assign(Id("v"), BinaryOp("+", IntLiteral(5), CallExpr(Id("func"), [])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_expression_07(self):
        input = """Function: fact
                Body:
                    v = func() + a[5][6];
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Assign(Id("v"), BinaryOp("+", CallExpr(Id("func"), []),
                                                                                  ArrayCell(Id("a"), [IntLiteral(5),
                                                                                                      IntLiteral(
                                                                                                          6)])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_expression_08(self):
        input = """Function: fact
                Body:
                    v = 5 * 3 - 8 -. 5 \. 6;
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Assign(Id("v"), BinaryOp("-.", BinaryOp("-", BinaryOp("*",
                                                                                                               IntLiteral(
                                                                                                                   5),
                                                                                                               IntLiteral(
                                                                                                                   3)),
                                                                                                 IntLiteral(8)),
                                                                                  BinaryOp("\.", IntLiteral(5),
                                                                                           IntLiteral(6))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_expression_09(self):
        input = """Function: fact
                Body:
                    v = a[8 + 3 * b];
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Assign(Id("v"), ArrayCell(Id("a"), [
            BinaryOp("+", IntLiteral(8), BinaryOp("*", IntLiteral(3), Id("b")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_25(self):
        input = """
            Function: main
            Body:
            a={ {1},{2,3}, 4. ,"Hello", True};
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [Assign(Id('a'), ArrayLiteral(
                            [ArrayLiteral([IntLiteral(1)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)]),
                             FloatLiteral(4.), StringLiteral("Hello"), BooleanLiteral(True)]))])
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_26(self):
        input = """
            Function: main
            Body:
                For (a=2 ,i,i) Do
                EndFor.
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [For(Id('a'), IntLiteral(2), Id('i'), Id('i'), ([], []))]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_27(self):
        input = """
            Function: main
    Body:
    Do
    While 1
    EndDo.
    EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [Dowhile(([], []), IntLiteral(1))]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_28(self):
        input = """
            Function: main
    Body:

    While 1
    Do
    EndWhile.
    EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [While(IntLiteral(1), ([], []))]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_29(self):
        input = """
            Function: main
    Body:
    Do
    While (a < b) Do
    EndWhile.
    While 1
    EndDo.
    EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [Dowhile(([], [While(BinaryOp('<', Id('a'), Id('b')), ([], []))]), IntLiteral(1))]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_30(self):
        input = """
            Function: main
    Body:
    Do
    Break;
    Continue;
    While 1
    EndDo.
    EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [Dowhile(([], [Break(), Continue()]), IntLiteral(1))]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_expression_16(self):
        input = """Function: fact
                Body:
                    a = 5 + 6 + 7 || 8 || 9;
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Assign(Id("a"), BinaryOp("||", BinaryOp("||", BinaryOp("+",
                                                                                                                BinaryOp(
                                                                                                                    "+",
                                                                                                                    IntLiteral(
                                                                                                                        5),
                                                                                                                    IntLiteral(
                                                                                                                        6)),
                                                                                                                IntLiteral(
                                                                                                                    7)),
                                                                                                 IntLiteral(8)),
                                                                                  IntLiteral(9)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_ifStmtInFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1;
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If(
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        )
                    ],
                    ([],[]))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))





    def test_expression_18(self):
        input = """Function: fact
                Body:
                    v = -a - b + c || 7.0 % 89;
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Assign(Id("v"), BinaryOp("||", BinaryOp("+", BinaryOp("-",
                                                                                                               UnaryOp(
                                                                                                                   "-",
                                                                                                                   Id(
                                                                                                                       "a")),
                                                                                                               Id("b")),
                                                                                                 Id("c")),
                                                                                  BinaryOp("%", FloatLiteral(7.0),
                                                                                           IntLiteral(89))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_expression_19(self):
        input = """Function: fact
                Body:
                    v = func(func(func(func(7.123E-5))));
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Assign(Id("v"), CallExpr(Id("func"), [
            CallExpr(Id("func"), [CallExpr(Id("func"), [CallExpr(Id("func"), [FloatLiteral(7.123e-05)])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))



    def test_ifStmtInFunc_5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1;
        ElseIf x > y Then
        ElseIf x < y Then
        Else
            If y > 10 Then y = y \ 2;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [If(
                             [
                                 (BinaryOp("==", Id("x"), Id("y")),
                                  [],
                                  [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                                  ),
                                 (
                                     BinaryOp(">", Id("x"), Id("y")),
                                     [],
                                     []
                                 ),
                                 (
                                     BinaryOp("<", Id("x"), Id("y")),
                                     [],
                                     []
                                 )
                             ],
                             (
                                 [],
                                 [
                                     If(
                                         [
                                             (
                                                 BinaryOp(">", Id("y"), IntLiteral(10)),
                                                 [],
                                                 [Assign(Id("y"), BinaryOp("\\", Id("y"), IntLiteral(2)))]
                                             )
                                         ],
                                         (
                                             [],
                                             []
                                         )
                                     )
                                 ]
                             ))
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_ifStmtInFunc_6(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1;
        ElseIf x > y Then x = voo(1.2);
        ElseIf x < y Then y = b[goo(x)];
        Else foo();
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [If(
                             [
                                 (BinaryOp("==", Id("x"), Id("y")),
                                  [],
                                  [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                                  ),
                                 (
                                     BinaryOp(">", Id("x"), Id("y")),
                                     [],
                                     [Assign(Id("x"), CallExpr(Id("voo"), [FloatLiteral(1.2)]))]
                                 ),
                                 (
                                     BinaryOp("<", Id("x"), Id("y")),
                                     [],
                                     [Assign(Id("y"), ArrayCell(Id("b"), [CallExpr(Id("goo"), [Id("x")])]))]
                                 )
                             ],
                             ([], [CallStmt(Id("foo"), [])])
                         )
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_ifStmtInFunc_7(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1;
        ElseIf x > y Then Var: a = 1;
        ElseIf x < y Then Var: b = 2;
        Else
            If y > 10 Then y = y \ 2;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [If(
                             [
                                 (BinaryOp("==", Id("x"), Id("y")),
                                  [],
                                  [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                                  ),
                                 (
                                     BinaryOp(">", Id("x"), Id("y")),
                                     [VarDecl(Id("a"), [], IntLiteral(1))],
                                     []
                                 ),
                                 (
                                     BinaryOp("<", Id("x"), Id("y")),
                                     [VarDecl(Id("b"), [], IntLiteral(2))],
                                     []
                                 )
                             ],
                             (
                                 [],
                                 [
                                     If(
                                         [
                                             (
                                                 BinaryOp(">", Id("y"), IntLiteral(10)),
                                                 [],
                                                 [Assign(Id("y"), BinaryOp("\\", Id("y"), IntLiteral(2)))]
                                             )
                                         ],
                                         (
                                             [],
                                             []
                                         )
                                     )
                                 ]
                             ))
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_ifStmtInFunc_8(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1;
        ElseIf x > y Then Var: a = 1; x = a * 10.5;
        ElseIf x < y Then Var: b = 2; y = b + foo();
        Else
            If y > 10 Then y = y \ 2; Return 1;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [If(
                             [
                                 (BinaryOp("==", Id("x"), Id("y")),
                                  [],
                                  [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                                  ),
                                 (
                                     BinaryOp(">", Id("x"), Id("y")),
                                     [VarDecl(Id("a"), [], IntLiteral(1))],
                                     [Assign(Id("x"), BinaryOp("*", Id("a"), FloatLiteral(10.5)))]
                                 ),
                                 (
                                     BinaryOp("<", Id("x"), Id("y")),
                                     [VarDecl(Id("b"), [], IntLiteral(2))],
                                     [Assign(Id("y"), BinaryOp("+", Id("b"), CallExpr(Id("foo"), [])))]
                                 )
                             ],
                             (
                                 [],
                                 [
                                     If(
                                         [
                                             (
                                                 BinaryOp(">", Id("y"), IntLiteral(10)),
                                                 [],
                                                 [Assign(Id("y"), BinaryOp("\\", Id("y"), IntLiteral(2))),
                                                  Return(IntLiteral(1))]
                                             )
                                         ],
                                         (
                                             [],
                                             []
                                         )
                                     )
                                 ]
                             ))
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_39(self):
        input = """
            Var:
      n,tong=0, i;
      Function:main
    Body:
      clrscr(); write("Nhap so nguyen duong n:");
      readln(n);
      tong = 0;
      For (i=1,i<=n%2,i+1) Do
        If (n % i == 0) Then
          tong = tong + i;
        EndIf.
      EndFor.
      If (tong == n) Then
        writeln(n, " la so hoan hao");
      Else
        writeln(n, "khong la so hoan hao");
      EndIf.
      ***Kiem tra so hoan hao**
    EndBody.
            """
        expect = Program(
                [
                    VarDecl(Id("n"), [], None),
                    VarDecl(Id("tong"), [], IntLiteral(0)),
                    VarDecl(Id("i"), [], None),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            CallStmt(Id('clrscr'), []),
                            CallStmt(Id('write'), [StringLiteral("Nhap so nguyen duong n:")]),
                            CallStmt(Id('readln'), [Id('n')]),
                            Assign(Id('tong'), IntLiteral(0)),
                            For(
                                Id('i'),
                                IntLiteral(1),
                                BinaryOp('<=', Id('i'), BinaryOp('%', Id('n'), IntLiteral(2))),
                                BinaryOp('+', Id('i'), IntLiteral(1)),
                                ([], [If([(
                                    BinaryOp('==', BinaryOp('%', Id('n'), Id('i')), IntLiteral(0)),
                                    [],
                                    [Assign(Id('tong'), BinaryOp('+', Id('tong'), Id('i')))]
                                )],
                                    ([], []))])
                            ),
                            If([(
                                BinaryOp('==', Id('tong'), Id('n')),
                                [],
                                [CallStmt(Id('writeln'), [Id('n'), StringLiteral(" la so hoan hao")]), ]
                            )],
                                ([], [CallStmt(Id('writeln'), [Id('n'), StringLiteral("khong la so hoan hao")]), ]))
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_40(self):
        input = """
            Var:
      n, i;
    Function: main
    Body:
      clrscr();
      write("Nhap so nguyen duong n: ");
      readln(n);
      If (n < 2) Then
        writeln(n, " khong la so nguyen to");
      Else
        i = 2;
        While ((i <= trunc(sqrt(n))) && (n % i != 0)) Do
          i = i + 1;
          EndWhile.
        If i > trunc(sqrt(n)) Then
          writeln(n, " la so nguyen to");
        Else
          writeln(n, " khong la so nguyen to");
        EndIf.
      EndIf.
    EndBody.
            """
        expect = Program(
                [
                    VarDecl(Id("n"), [], None),
                    VarDecl(Id("i"), [], None),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            CallStmt(Id('clrscr'), []),
                            CallStmt(Id('write'), [StringLiteral("Nhap so nguyen duong n: ")]),
                            CallStmt(Id('readln'), [Id('n')]),
                            If([(
                                BinaryOp('<', Id('n'), IntLiteral(2)),
                                [],
                                [CallStmt(Id('writeln'), [Id('n'), StringLiteral(" khong la so nguyen to")]), ]
                            )],
                                ([], [
                                    Assign(Id('i'), IntLiteral(2)),
                                    While(
                                        BinaryOp("&&", BinaryOp("<=", Id("i"), CallExpr(Id("trunc"), [
                                            CallExpr(Id("sqrt"), [Id("n")])])),
                                                 BinaryOp("!=", BinaryOp("%", Id("n"), Id("i")),
                                                          IntLiteral(0))),
                                        ([], [Assign(Id('i'), BinaryOp('+', Id('i'), IntLiteral(1)))])
                                    ),
                                    If([(
                                        BinaryOp(">", Id("i"),
                                                 CallExpr(Id("trunc"), [CallExpr(Id("sqrt"), [Id("n")])])),
                                        [],
                                        [CallStmt(Id('writeln'), [Id('n'), StringLiteral(" la so nguyen to")]), ]
                                    )],
                                        ([], [CallStmt(Id('writeln'),
                                                       [Id('n'), StringLiteral(" khong la so nguyen to")]), ])),

                                ]))
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_41(self):
        input = """
           Function: main
            Body:
            p = rho*r*t + (b_0*r*t-a_0-((c_0) \ (t*t))+((e_0) \ (mathPow(t, 4))))*rho*rho +
        (b*r*t-a-((d) \ (t)))*mathpow(rho, 3) +
        alpha*(a+((d) \ (t)))*mathpow(rho, 6) +
        ((c*mathPow(rho, 3)) \ (t*t))*(1+gamma*rho*rho)*mathExp(-gamma*rho*rho);
        EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            Assign(Id('p'), BinaryOp("+", BinaryOp("+", BinaryOp("+", BinaryOp("+", BinaryOp("*",
                                                                                                             BinaryOp(
                                                                                                                 "*",
                                                                                                                 Id(
                                                                                                                     "rho"),
                                                                                                                 Id(
                                                                                                                     "r")),
                                                                                                             Id("t")),
                                                                                               BinaryOp("*",
                                                                                                        BinaryOp("*",
                                                                                                                 BinaryOp(
                                                                                                                     "+",
                                                                                                                     BinaryOp(
                                                                                                                         "-",
                                                                                                                         BinaryOp(
                                                                                                                             "-",
                                                                                                                             BinaryOp(
                                                                                                                                 "*",
                                                                                                                                 BinaryOp(
                                                                                                                                     "*",
                                                                                                                                     Id(
                                                                                                                                         "b_0"),
                                                                                                                                     Id(
                                                                                                                                         "r")),
                                                                                                                                 Id(
                                                                                                                                     "t")),
                                                                                                                             Id(
                                                                                                                                 "a_0")),
                                                                                                                         BinaryOp(
                                                                                                                             "\\",
                                                                                                                             Id(
                                                                                                                                 "c_0"),
                                                                                                                             BinaryOp(
                                                                                                                                 "*",
                                                                                                                                 Id(
                                                                                                                                     "t"),
                                                                                                                                 Id(
                                                                                                                                     "t")))),
                                                                                                                     BinaryOp(
                                                                                                                         "\\",
                                                                                                                         Id(
                                                                                                                             "e_0"),
                                                                                                                         CallExpr(
                                                                                                                             Id(
                                                                                                                                 "mathPow"),
                                                                                                                             [
                                                                                                                                 Id(
                                                                                                                                     "t"),
                                                                                                                                 IntLiteral(
                                                                                                                                     4)]))),
                                                                                                                 Id(
                                                                                                                     "rho")),
                                                                                                        Id("rho"))),
                                                                                 BinaryOp("*", BinaryOp("-",
                                                                                                        BinaryOp("-",
                                                                                                                 BinaryOp(
                                                                                                                     "*",
                                                                                                                     BinaryOp(
                                                                                                                         "*",
                                                                                                                         Id(
                                                                                                                             "b"),
                                                                                                                         Id(
                                                                                                                             "r")),
                                                                                                                     Id(
                                                                                                                         "t")),
                                                                                                                 Id(
                                                                                                                     "a")),
                                                                                                        BinaryOp("\\",
                                                                                                                 Id(
                                                                                                                     "d"),
                                                                                                                 Id(
                                                                                                                     "t"))),
                                                                                          CallExpr(Id("mathpow"),
                                                                                                   [Id("rho"),
                                                                                                    IntLiteral(3)]))),
                                                                   BinaryOp("*", BinaryOp("*", Id("alpha"),
                                                                                          BinaryOp("+", Id("a"),
                                                                                                   BinaryOp("\\",
                                                                                                            Id("d"),
                                                                                                            Id("t")))),
                                                                            CallExpr(Id("mathpow"),
                                                                                     [Id("rho"), IntLiteral(6)]))),
                                                     BinaryOp("*", BinaryOp("*",
                                                                            BinaryOp("\\", BinaryOp("*", Id("c"),
                                                                                                    CallExpr(
                                                                                                        Id("mathPow"),
                                                                                                        [Id("rho"),
                                                                                                         IntLiteral(
                                                                                                             3)])),
                                                                                     BinaryOp("*", Id("t"), Id("t"))),
                                                                            BinaryOp("+", IntLiteral(1), BinaryOp("*",
                                                                                                                  BinaryOp(
                                                                                                                      "*",
                                                                                                                      Id(
                                                                                                                          "gamma"),
                                                                                                                      Id(
                                                                                                                          "rho")),
                                                                                                                  Id(
                                                                                                                      "rho")))),
                                                              CallExpr(Id("mathExp"),
                                                                       [BinaryOp("*", BinaryOp("*", UnaryOp("-", Id(
                                                                           "gamma")), Id("rho")), Id("rho"))])))),
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_42(self):
        input = """
            Function: main
            Body:
            d=a[b[2][4] + foo(2)][goo(123)]+1;
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            Assign(Id('d'),
                                   BinaryOp("+", ArrayCell(Id("a"), [
                                       BinaryOp("+", ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(4)]),
                                                CallExpr(Id("foo"),
                                                         [IntLiteral(2)])), CallExpr(Id("goo"), [IntLiteral(123)])]),
                                            IntLiteral(1))
                                   )
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_43(self):
        input = """
            Function: main
            Body: b=-foo(3,4,-func(b[59][20][40]))||1||a[1]||foo(1,2); EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            Assign(Id('b'),
                                   BinaryOp("||", BinaryOp("||", BinaryOp("||", UnaryOp("-", CallExpr(Id("foo"),
                                                                                                      [IntLiteral(3),
                                                                                                       IntLiteral(4),
                                                                                                       UnaryOp("-",
                                                                                                               CallExpr(
                                                                                                                   Id(
                                                                                                                       "func"),
                                                                                                                   [
                                                                                                                       ArrayCell(
                                                                                                                           Id(
                                                                                                                               "b"),
                                                                                                                           [
                                                                                                                               IntLiteral(
                                                                                                                                   59),
                                                                                                                               IntLiteral(
                                                                                                                                   20),
                                                                                                                               IntLiteral(
                                                                                                                                   40)])]))])),
                                                                          IntLiteral(1)),
                                                           ArrayCell(Id("a"), [IntLiteral(1)])),
                                            CallExpr(Id("foo"), [IntLiteral(1), IntLiteral(2)])),
                                   )
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_44(self):
        input = """
            Function: main
            Body:
            a=-foo(3,4,-func(b[59][20][40]))+1+a[1]+foo(1,2);
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [Assign(Id("a"), BinaryOp("+", BinaryOp("+", BinaryOp("+", UnaryOp("-",
                                                                                                CallExpr(Id("foo"),
                                                                                                         [IntLiteral(3),
                                                                                                          IntLiteral(4),
                                                                                                          UnaryOp("-",
                                                                                                                  CallExpr(
                                                                                                                      Id(
                                                                                                                          "func"),
                                                                                                                      [
                                                                                                                          ArrayCell(
                                                                                                                              Id(
                                                                                                                                  "b"),
                                                                                                                              [
                                                                                                                                  IntLiteral(
                                                                                                                                      59),
                                                                                                                                  IntLiteral(
                                                                                                                                      20),
                                                                                                                                  IntLiteral(
                                                                                                                                      40)])]))])),
                                                                                   IntLiteral(1)),
                                                                     ArrayCell(Id("a"), [IntLiteral(1)])),
                                                       CallExpr(Id("foo"), [IntLiteral(1), IntLiteral(2)])))]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_45(self):
        input = """
            Function: main
            Body:
            a=foo(3,4)+1+a[1]+foo(1,2); EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [Assign(Id("a"), BinaryOp("+", BinaryOp("+", BinaryOp("+", CallExpr(Id("foo"),
                                                                                                 [IntLiteral(3),
                                                                                                  IntLiteral(4)]),
                                                                                   IntLiteral(1)),
                                                                     ArrayCell(Id("a"), [IntLiteral(1)])),
                                                       CallExpr(Id("foo"), [IntLiteral(1), IntLiteral(2)])))]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_46(self):
        input = """
            Function: main
            Body:
            sqrt(pow(b,2) - 4*a*c);
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [CallStmt(Id("sqrt"), [BinaryOp("-", CallExpr(Id("pow"), [Id("b"), IntLiteral(2)]),
                                                             BinaryOp("*", BinaryOp("*", IntLiteral(4), Id("a")),
                                                                      Id("c")))])]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_if_statement_02(self):
        input = """Function: fact
                Body:
                    If a == b Then a = a + 1; 
                    Else a = a + 2;
                    EndIf.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [
            If([(BinaryOp("==", Id("a"), Id("b")), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))])],
               ([], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_if_statement_03(self):
        input = """Function: fact
                Body:
                    If a == b Then 
                        Var: z[1][2] = {{1,2}};
                        a = a + 1; 
                    ElseIf a > 3 Then 
                        Var: x = 6, y;
                        a = a + 3;
                    EndIf.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [If([(BinaryOp("==", Id("a"), Id("b")), [
            VarDecl(Id("z"), [1, 2], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])]))],
                                                              [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))]),
                                                             (BinaryOp(">", Id("a"), IntLiteral(3)),
                                                              [VarDecl(Id("x"), [], IntLiteral(6)),
                                                               VarDecl(Id("y"), [], None)], [Assign(Id("a"),
                                                                                                    BinaryOp("+",
                                                                                                             Id("a"),
                                                                                                             IntLiteral(
                                                                                                                 3)))])],
                                                            ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_if_statement_04(self):
        input = """Function: fact
                Body:
                    If a == b Then a = a + 1; 
                    ElseIf a > 3 Then a = a + 3;
                    Else a = a + 4 ;
                    EndIf.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [If(
            [(BinaryOp("==", Id("a"), Id("b")), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))]),
             (BinaryOp(">", Id("a"), IntLiteral(3)), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(3)))])],
            ([], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(4)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_if_statement_05(self):
        input = input = """Function: fact
                Body:
                    If a == b Then a = a + 1; 
                    ElseIf True Then a = a + 2;
                    ElseIf a > 3 Then a = a + 3;
                    Else a = a + 4 ;
                    EndIf.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [If(
            [(BinaryOp("==", Id("a"), Id("b")), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))]),
             (BooleanLiteral(True), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(2)))]),
             (BinaryOp(">", Id("a"), IntLiteral(3)), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(3)))])],
            ([], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(4)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_if_statement_06(self):
        input = input = """Function: fact
                Body:
                    If a == b Then 
                        If b == c Then b = 5;
                        EndIf.
                    ElseIf True Then a = a + 2;
                    Else a = a + 3 ;
                    EndIf.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [If([(BinaryOp("==", Id("a"), Id("b")), [], [
            If([(BinaryOp("==", Id("b"), Id("c")), [], [Assign(Id("b"), IntLiteral(5))])], ([], []))]), (
                                                             BooleanLiteral(True), [],
                                                             [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(2)))])],
                                                            ([], [Assign(Id("a"),
                                                                         BinaryOp("+", Id("a"), IntLiteral(3)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_if_statement_07(self):
        input = input = """Function: fact
                Body:
                    If a == b Then a = a + 1; 
                    EndIf.
                    If True Then b = 6;
                    ElseIf False Then a = a + 2;
                    ElseIf a > 3 Then a = a + 3;
                    Else a = a + 4 ;
                    EndIf.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [
            If([(BinaryOp("==", Id("a"), Id("b")), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))])],
               ([], [])), If([(BooleanLiteral(True), [], [Assign(Id("b"), IntLiteral(6))]),
                              (BooleanLiteral(False), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(2)))]), (
                              BinaryOp(">", Id("a"), IntLiteral(3)), [],
                              [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(3)))])],
                             ([], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(4)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_if_statement_08(self):
        input = input = """Function: fact
                Body:
                    If a == b Then a = a + 1; 
                    ElseIf True Then a = a + 2;
                    ElseIf a > 3 Then a = a + 3;
                    Else a = a + 4 ;
                    EndIf.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [If(
            [(BinaryOp("==", Id("a"), Id("b")), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))]),
             (BooleanLiteral(True), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(2)))]),
             (BinaryOp(">", Id("a"), IntLiteral(3)), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(3)))])],
            ([], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(4)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_if_statement_09(self):
        input = input = """Function: fact
                Body:
                    If False Then 
                    ElseIf True Then a = a + 2;
                    ElseIf a > 3 Then a = a + 3;
                    Else a = a + 4 ;
                    EndIf.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [If([(BooleanLiteral(False), [], []), (
        BooleanLiteral(True), [], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(2)))]), (
                                                             BinaryOp(">", Id("a"), IntLiteral(3)), [],
                                                             [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(3)))])],
                                                            ([], [Assign(Id("a"),
                                                                         BinaryOp("+", Id("a"), IntLiteral(4)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_whileFunc_5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do
                x = x + 1;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [
                             While(BinaryOp("<", Id("x"), FloatLiteral(10.5)),
                                   (
                                       [],
                                       [
                                           Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))),
                                           While(BinaryOp("==", Id("y"), IntLiteral(1)),
                                                 (
                                                     [],
                                                     [Assign(Id("dd"), Id("nn")),
                                                      Assign(ArrayCell(Id("y"), [Id("i")]),
                                                             ArrayCell(Id("x"), [BinaryOp("+", Id("y"), Id("i"))])),
                                                      Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9))
                                                      ]
                                                 ))
                                       ]
                                   ))
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_whileFunc_6(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do
                x = x + 1;
                Continue;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                    Return x + y;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [
                             While(BinaryOp("<", Id("x"), FloatLiteral(10.5)),
                                   (
                                       [],
                                       [
                                           Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))),
                                           Continue(),
                                           While(BinaryOp("==", Id("y"), IntLiteral(1)),
                                                 (
                                                     [],
                                                     [Assign(Id("dd"), Id("nn")),
                                                      Assign(ArrayCell(Id("y"), [Id("i")]),
                                                             ArrayCell(Id("x"), [BinaryOp("+", Id("y"), Id("i"))])),
                                                      Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9)),
                                                      Return(BinaryOp("+", Id("x"), Id("y")))
                                                      ]
                                                 ))
                                       ]
                                   ))
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_whileFunc_7(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do
                x = x + 1;
                Continue;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                    Return x + y;
                EndWhile.
                Return 10;
            EndWhile.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [
                             While(BinaryOp("<", Id("x"), FloatLiteral(10.5)),
                                   (
                                       [],
                                       [
                                           Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))),
                                           Continue(),
                                           While(BinaryOp("==", Id("y"), IntLiteral(1)),
                                                 (
                                                     [],
                                                     [Assign(Id("dd"), Id("nn")),
                                                      Assign(ArrayCell(Id("y"), [Id("i")]),
                                                             ArrayCell(Id("x"), [BinaryOp("+", Id("y"), Id("i"))])),
                                                      Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9)),
                                                      Return(BinaryOp("+", Id("x"), Id("y")))
                                                      ]
                                                 )),
                                           Return(IntLiteral(10))
                                       ]
                                   ))
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_whileFunc_8(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do
                x = x + 1;
                Continue;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                    Return x + y;
                EndWhile.
                Return 10;
            EndWhile.
            Return dd;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [
                             While(BinaryOp("<", Id("x"), FloatLiteral(10.5)),
                                   (
                                       [],
                                       [
                                           Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))),
                                           Continue(),
                                           While(BinaryOp("==", Id("y"), IntLiteral(1)),
                                                 (
                                                     [],
                                                     [Assign(Id("dd"), Id("nn")),
                                                      Assign(ArrayCell(Id("y"), [Id("i")]),
                                                             ArrayCell(Id("x"), [BinaryOp("+", Id("y"), Id("i"))])),
                                                      Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9)),
                                                      Return(BinaryOp("+", Id("x"), Id("y")))
                                                      ]
                                                 )),
                                           Return(IntLiteral(10))
                                       ]
                                   )), Return(Id("dd"))
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_whileFunc_9(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do
                Var: mm = 10;
                x = x + 1;
                Continue;
                While y == 1 Do
                    Var: nn, qq;
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                    Return x + y;
                EndWhile.
                Return 10;
            EndWhile.
            Return dd;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [
                             While(BinaryOp("<", Id("x"), FloatLiteral(10.5)),
                                   (
                                       [VarDecl(Id("mm"), [], IntLiteral(10))],
                                       [
                                           Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))),
                                           Continue(),
                                           While(BinaryOp("==", Id("y"), IntLiteral(1)),
                                                 (
                                                     [VarDecl(Id("nn"), [], None), VarDecl(Id("qq"), [], None)],

                                                     [Assign(Id("dd"), Id("nn")),
                                                      Assign(ArrayCell(Id("y"), [Id("i")]),
                                                             ArrayCell(Id("x"), [BinaryOp("+", Id("y"), Id("i"))])),
                                                      Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9)),
                                                      Return(BinaryOp("+", Id("x"), Id("y")))
                                                      ]
                                                 )),
                                           Return(IntLiteral(10))
                                       ]
                                   )), Return(Id("dd"))
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_60(self):
        input = """
             Function: main
    Body:
    For (a=2 ,i,i) Do
    Do
    While 1
    EndDo.
    EndFor.
    EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            For(Id('a'), IntLiteral(2), Id('i'), Id('i'), ([], [
                                Dowhile(([], []), IntLiteral(1))
                            ]))
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_61(self):
        input = """
            Function: main
    Body:
    For (a=2 ,i,i) Do
    While (a < b) Do
    EndWhile.
    EndFor.
    EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            For(Id('a'), IntLiteral(2), Id('i'), Id('i'), ([], [
                                While(BinaryOp('<', Id('a'), Id('b')), ([], []))
                            ]))
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_62(self):
        input = """
            Function: main
    Body:
    If (x==0) Then 
    b=1;
    Do
    While 1
    EndDo.
    Else  EndIf.
    EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            If([(BinaryOp('==', Id('x'), IntLiteral(0)), [], [
                                Assign(Id('b'), IntLiteral(1)),
                                Dowhile(([], []), IntLiteral(1))
                            ]),
                                ],
                               ([], []))
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_63(self):
        input = """
            Function: main
    Body:
    If (x==0) Then 
    Else  
    Do
    While 1
    EndDo.
    EndIf.
    EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            If([(BinaryOp('==', Id('x'), IntLiteral(0)), [], []),
                                ],
                               ([], [
                                   Dowhile(([], []), IntLiteral(1))
                               ]))
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_64(self):
        input = """
            Function: main
            Body:
            p = f * (r \ (pow(1 + r, n) - 1)) * (1 \ (1 + r));
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [Assign(Id("p"), BinaryOp("*", BinaryOp("*", Id("f"), BinaryOp("\\", Id("r"), BinaryOp("-",
                                                                                                                    CallExpr(
                                                                                                                        Id(
                                                                                                                            "pow"),
                                                                                                                        [
                                                                                                                            BinaryOp(
                                                                                                                                "+",
                                                                                                                                IntLiteral(
                                                                                                                                    1),
                                                                                                                                Id(
                                                                                                                                    "r")),
                                                                                                                            Id(
                                                                                                                                "n")]),
                                                                                                                    IntLiteral(
                                                                                                                        1)))),
                                                       BinaryOp("\\", IntLiteral(1),
                                                                BinaryOp("+", IntLiteral(1), Id("r")))))]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_65(self):
        input = """
            Function: main
            Body:
            a=a+b*(c||d-e)&&(f+g*h)-i;
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([], [
                            Assign(Id("a"), BinaryOp("&&", BinaryOp("+", Id("a"), BinaryOp("*", Id("b"),
                                                                                           BinaryOp("||", Id("c"),
                                                                                                    BinaryOp("-",
                                                                                                             Id("d"),
                                                                                                             Id(
                                                                                                                 "e"))))),
                                                     BinaryOp("-",
                                                              BinaryOp("+", Id("f"), BinaryOp("*", Id("g"), Id("h"))),
                                                              Id("i"))))
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_do_while_statement_01(self):
        input = """Function: fact
                Body:
                    Do
                        i = i - 1 ;
                    While 
                        i > 0
                    EndDo.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [
            Dowhile(([], [Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1)))]),
                    BinaryOp(">", Id("i"), IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_do_while_statement_02(self):
        input = """Function: fact
                Body:
                    Do
                        i = i - 1 ;
                    While 
                        isPrime(i)
                    EndDo.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [
            Dowhile(([], [Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1)))]),
                    CallExpr(Id("isPrime"), [Id("i")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_do_while_statement_03(self):
        input = """Function: fact
                Body:
                    Do
                        i = i - 1 ;
                    While 
                        (i > 0) && (i < 6)
                    EndDo.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [
            Dowhile(([], [Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1)))]),
                    BinaryOp("&&", BinaryOp(">", Id("i"), IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(6))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_do_while_statement_04(self):
        input = """Function: fact
                Body:
                    Do
                    While 
                        i > 0
                    EndDo.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Dowhile(([], []), BinaryOp(">", Id("i"), IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_do_while_statement_05(self):
        input = """Function: fact
                Body:
                    Do
                        Var: x = 0x16, y = 100;
                        Var: abc = "abc";
                        i = i - 1 ;
                    While 
                        i
                    EndDo.
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Dowhile(([VarDecl(Id("x"), [], IntLiteral(22)),
                                                                   VarDecl(Id("y"), [], IntLiteral(100)),
                                                                   VarDecl(Id("abc"), [], StringLiteral("abc"))], [
                                                                      Assign(Id("i"),
                                                                             BinaryOp("-", Id("i"), IntLiteral(1)))]),
                                                                 Id("i"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))


    def test_call_statement_01(self):
        input = """Function: fact
                Body:
                    foo(5 * 6, 7) ;
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], (
        [], [CallStmt(Id("foo"), [BinaryOp("*", IntLiteral(5), IntLiteral(6)), IntLiteral(7)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_call_statement_02(self):
        input = """Function: fact
                Body:
                    foo(); 
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], ([], [CallStmt(Id("foo"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_call_statement_03(self):
        input = """Function: fact
                Body:
                    foo(i, foo(i - 1)) ;
                EndBody.
                """
        expect = Program([FuncDecl(Id("fact"), [], (
        [], [CallStmt(Id("foo"), [Id("i"), CallExpr(Id("foo"), [BinaryOp("-", Id("i"), IntLiteral(1))])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_all_374(self):
        input = """Var: x = 5;
             Function: main
             Body:
                 x = 10;
                 printLn(x);
                 Continue;
                 Break;
                 Return;
             EndBody.
             """
        expect = str(Program([
                             VarDecl(Id("x"),[],IntLiteral(5)),
                FuncDecl(Id("main"), [], ([], [
                    Assign(Id("x"), IntLiteral(10)),
                    CallStmt(Id("printLn"), [Id("x")]),
                    Continue(),
                    Break(),
                    Return(None)
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_all_375(self):
        input = """Var: x = 5;
             Function: main
             Body:
                 x = 10;
                 printLn(x);
                 Continue;
                 Break;
                 Return;
                 foo();
             EndBody.
             """
        expect = str(Program([
                VarDecl(Id("x"), [], IntLiteral(5)),
                FuncDecl(Id("main"), [], ([], [
                    Assign(Id("x"), IntLiteral(10)),
                    CallStmt(Id("printLn"), [Id("x")]),
                    Continue(),
                    Break(),
                    Return(None),
                    CallStmt(Id("foo"), [])
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_all_376(self):
        input = """Var: x = 5;
         Function: main
         Body:
             x = 10;
             printLn(x);
             Continue;
             Break;
             Return;
             foo();
             Return foo(10);
         EndBody.
         """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")]),
                Continue(),
                Break(),
                Return(None),
                CallStmt(Id("foo"), []),
                Return(CallExpr(Id("foo"), [IntLiteral(10)]))
            ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_all_377(self):
        input = """Var: x = 5;
         Function: main
         Body:
             x = 10;
             printLn(x);
             Continue;
             Break;
             Return;
             foo();
             Return foo(10);
         EndBody.
         Function: cont
             Body:
         EndBody.
         """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")]),
                Continue(),
                Break(),
                Return(None),
                CallStmt(Id("foo"), []),
                Return(CallExpr(Id("foo"), [IntLiteral(10)]))
            ])),
            FuncDecl(Id("cont"), [], ([], []))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_all_378(self):
        input = """Var: x = 5;
         Function: main
         Body:
             Var: x = 5;
             x = 10;
             printLn(x);
             Continue;
             Break;
             Return;
             foo();
             Return foo(10);
         EndBody.
         Function: cont
         Body:
             Var: x = 5;
         EndBody.
         """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(5))], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")]),
                Continue(),
                Break(),
                Return(None),
                CallStmt(Id("foo"), []),
                Return(CallExpr(Id("foo"), [IntLiteral(10)]))
            ])),
            FuncDecl(Id("cont"), [], ([VarDecl(Id("x"), [], IntLiteral(5))], []))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_all_379(self):
        input = """Var: x = 5;
         Function: main
         Body:
             Var: aa[0xDD];
             x = 10;
             printLn(x);
         EndBody.
         """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([VarDecl(Id("aa"), [221], None)], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_all_380(self):
        input = """Var: x = 5;
         Function: main
         Body:
             Var: aa[0xDD] = 0xAA;
             x = 10;
             printLn(x);
         EndBody.
         """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([VarDecl(Id("aa"), [221], IntLiteral(170))], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_all_381(self):
        input = """Var: x = 5;
         Function: main
         Body:
             Var: aa[0XDD];
             x = 10;
             printLn(x);
         EndBody.
         """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([VarDecl(Id("aa"), [221], None)], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_all_382(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: aa[0XDD] = 0xAA;
            x = 10;
            printLn(x);
       EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([VarDecl(Id("aa"), [221], IntLiteral(170))], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_all_383(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: aa[0o77];
            x = 10;
            printLn(x);
       EndBody.
       """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([VarDecl(Id("aa"), [63], None)], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_all_384(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: aa[0o77] = 0O11;
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([VarDecl(Id("aa"), [63], IntLiteral(9))], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_all_385(self):
        input = """Var: x = 1.;
        """
        expect = str(Program([
            VarDecl(Id("x"), [], FloatLiteral(1.))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_all_386(self):
        input = """Var: x = 1.0;
        """
        expect = str(Program([
            VarDecl(Id("x"), [], FloatLiteral(1.0))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_87(self):
        input = """
            Function: main
            Body:
            Var: x =0o567;
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([
                             VarDecl(Id("x"), [], IntLiteral(375)),
                         ], []),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_88(self):
        input = """
            Function: main
            Body:
            Var: x=0xFF;
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([
                             VarDecl(Id("x"), [], IntLiteral(255)),
                         ], []),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_89(self):
        input = """
            Function: main
            Body:
            Var: x =0O77;
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([
                             VarDecl(Id("x"), [], IntLiteral(63)),
                         ], []),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_90(self):
        input = """
            Function: main
            Body:
            Var:a[0x33][0x11]=0x1;
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [],
                        ([
                             VarDecl(Id("a"), [51, 17], IntLiteral(1)),
                         ], []),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_91(self):
        input = """
            Function: main
            Parameter: a[0xA][0o1][0][0O11][0X11]
            Body:
            a=foo[0xA+0O1];
            a=foo()[0xA + 0O1];
            a= f[0xA];
            a= f[-0xA];
            EndBody.
            """
        expect = Program(
                [
                    FuncDecl(
                        Id("main"),
                        [
                            VarDecl(Id("a"), [10, 1, 0, 9, 17], None),
                        ],
                        ([], [
                            Assign(Id('a'), ArrayCell(Id('foo'), [BinaryOp('+', IntLiteral(10), IntLiteral(1))])),
                            Assign(Id('a'),
                                   ArrayCell(CallExpr(Id('foo'), []), [BinaryOp('+', IntLiteral(10), IntLiteral(1))])),
                            Assign(Id('a'), ArrayCell(Id('f'), [IntLiteral(10)])),
                            Assign(Id('a'), ArrayCell(Id('f'), [UnaryOp('-', IntLiteral(10))])),
                        ]),
                    )
                ]
            )

        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_simple_program_12(self):
        input = """Function: sum
                Parameter: num[100], n
                Body:
                    Var: avg, sum = 0 ;
                    For (i = 0, i < n, 1) Do
                        sum = sum + num[i];
                    EndFor.
                    avg = sum \ n;
                    Return avg;
                EndBody.
                """
        expect = Program([FuncDecl(Id("sum"), [VarDecl(Id("num"), [100], None), VarDecl(Id("n"), [], None)], (
        [VarDecl(Id("avg"), [], None), VarDecl(Id("sum"), [], IntLiteral(0))], [
            For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("n")), IntLiteral(1),
                ([], [Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("num"), [Id("i")])))])),
            Assign(Id("avg"), BinaryOp("\\", Id("sum"), Id("n"))), Return(Id("avg"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_simple_program_13(self):
        input = """Function: lagestElement
                Parameter: arr[100], n
                Body:
                    Var: res;
                    res = arr[0];
                    For (i = 1, i < n, 1) Do
                        If arr[i] > res Then
                            res = arr[i];
                        EndIf.
                    EndFor.
                    Return res;
                EndBody.
                """
        expect = Program([FuncDecl(Id("lagestElement"), [VarDecl(Id("arr"), [100], None), VarDecl(Id("n"), [], None)], (
        [VarDecl(Id("res"), [], None)], [Assign(Id("res"), ArrayCell(Id("arr"), [IntLiteral(0)])),
                                         For(Id("i"), IntLiteral(1), BinaryOp("<", Id("i"), Id("n")), IntLiteral(1), (
                                         [], [If([(BinaryOp(">", ArrayCell(Id("arr"), [Id("i")]), Id("res")), [],
                                                   [Assign(Id("res"), ArrayCell(Id("arr"), [Id("i")]))])], ([], []))])),
                                         Return(Id("res"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_simple_program_14(self):
        input = """Function: calculateSD
                Parameter: data[10]
                Body:
                    Var: sum = 0.0, mean, sd = 0.0;
                    Var: i;
                    For (i = 0, i < 10, 1) Do
                        sum = sum + data[i];
                    EndFor.
                    mean = sum \ 10;
                    For (i = 0, i < 10, 1) Do
                        sd = sd + pow(data[i]- mean, 2);
                    EndFor.
                    Return sqrt(sd \ 10);
                EndBody.
                """
        expect = Program([FuncDecl(Id("calculateSD"), [VarDecl(Id("data"), [10], None)], (
        [VarDecl(Id("sum"), [], FloatLiteral(0.0)), VarDecl(Id("mean"), [], None),
         VarDecl(Id("sd"), [], FloatLiteral(0.0)), VarDecl(Id("i"), [], None)], [
            For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1),
                ([], [Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("data"), [Id("i")])))])),
            Assign(Id("mean"), BinaryOp("\\", Id("sum"), IntLiteral(10))),
            For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1), ([], [Assign(Id("sd"),
                                                                                                            BinaryOp(
                                                                                                                "+", Id(
                                                                                                                    "sd"),
                                                                                                                CallExpr(
                                                                                                                    Id(
                                                                                                                        "pow"),
                                                                                                                    [
                                                                                                                        BinaryOp(
                                                                                                                            "-",
                                                                                                                            ArrayCell(
                                                                                                                                Id(
                                                                                                                                    "data"),
                                                                                                                                [
                                                                                                                                    Id(
                                                                                                                                        "i")]),
                                                                                                                            Id(
                                                                                                                                "mean")),
                                                                                                                        IntLiteral(
                                                                                                                            2)])))])),
            Return(CallExpr(Id("sqrt"), [BinaryOp("\\", Id("sd"), IntLiteral(10))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_simple_program_15(self):
        input = """Function: length
                Parameter: s[1000]
                Body:
                    Var: cnt = 0;
                    For (i = 0, s[i] != "0", 1) Do
                        cnt = cnt + 1;
                    EndFor.
                    Return cnt;
                EndBody.
                """
        expect = Program([FuncDecl(Id("length"), [VarDecl(Id("s"), [1000], None)], (
        [VarDecl(Id("cnt"), [], IntLiteral(0))], [
            For(Id("i"), IntLiteral(0), BinaryOp("!=", ArrayCell(Id("s"), [Id("i")]), StringLiteral("0")),
                IntLiteral(1), ([], [Assign(Id("cnt"), BinaryOp("+", Id("cnt"), IntLiteral(1)))])),
            Return(Id("cnt"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    """-----------------------------------------------------------------------------------------------------------------------------------------------------------"""

    def test_complex_program_01(self):
        input = """Function: tranposeOfMatrix
                Parameter: a[10][10], tranpose[10][10], r, c
                Body:
                    For (i = 0, i < r, 1) Do
                        For (j = 0, j < c, 1) Do
                            transpose[j][i] = a[i][j];
                        EndFor.
                    EndFor.
                    Return transpose;
                EndBody.
                """
        expect = Program([FuncDecl(Id("tranposeOfMatrix"),
                                   [VarDecl(Id("a"), [10, 10], None), VarDecl(Id("tranpose"), [10, 10], None),
                                    VarDecl(Id("r"), [], None), VarDecl(Id("c"), [], None)], ([], [
                For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("r")), IntLiteral(1), ([], [
                    For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), Id("c")), IntLiteral(1), ([], [
                        Assign(ArrayCell(Id("transpose"), [Id("j"), Id("i")]),
                               ArrayCell(Id("a"), [Id("i"), Id("j")]))]))])), Return(Id("transpose"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_complex_program_02(self):
        input = """Function: countSort
                Parameter: arr[100], n, exp
                Body:
                    Var: output[100];
                    Var: i, count[10] = {0};
                    For (i = 0, i < n, 1) Do
                        count[(arr[i] \ exp) % 10] = count[(arr[i] \ exp) % 10] + 1;
                    EndFor.

                    For (i = 1, i < 10, 1) Do
                        count[i] = count[i] + count[i-1];
                    EndFor.

                    For (i = n-1, i >= 0, -1) Do
                        output[count[(arr[i] \ exp)%10] - 1] = arr[i];
                        count[(arr[i] \ exp) % 10] = count[(arr[i] \ exp) % 10] - 1;
                    EndFor.

                    For (i = 0, i < n, 1) Do
                        arr[i] = count[i];
                    EndFor.

                EndBody.
                """
        expect = Program([FuncDecl(Id("countSort"), [VarDecl(Id("arr"), [100], None), VarDecl(Id("n"), [], None),
                                                     VarDecl(Id("exp"), [], None)], (
                                   [VarDecl(Id("output"), [100], None), VarDecl(Id("i"), [], None),
                                    VarDecl(Id("count"), [10], ArrayLiteral([IntLiteral(0)]))], [
                                       For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("n")), IntLiteral(1), ([],
                                                                                                                    [
                                                                                                                        Assign(
                                                                                                                            ArrayCell(
                                                                                                                                Id(
                                                                                                                                    "count"),
                                                                                                                                [
                                                                                                                                    BinaryOp(
                                                                                                                                        "%",
                                                                                                                                        BinaryOp(
                                                                                                                                            "\\",
                                                                                                                                            ArrayCell(
                                                                                                                                                Id(
                                                                                                                                                    "arr"),
                                                                                                                                                [
                                                                                                                                                    Id(
                                                                                                                                                        "i")]),
                                                                                                                                            Id(
                                                                                                                                                "exp")),
                                                                                                                                        IntLiteral(
                                                                                                                                            10))]),
                                                                                                                            BinaryOp(
                                                                                                                                "+",
                                                                                                                                ArrayCell(
                                                                                                                                    Id(
                                                                                                                                        "count"),
                                                                                                                                    [
                                                                                                                                        BinaryOp(
                                                                                                                                            "%",
                                                                                                                                            BinaryOp(
                                                                                                                                                "\\",
                                                                                                                                                ArrayCell(
                                                                                                                                                    Id(
                                                                                                                                                        "arr"),
                                                                                                                                                    [
                                                                                                                                                        Id(
                                                                                                                                                            "i")]),
                                                                                                                                                Id(
                                                                                                                                                    "exp")),
                                                                                                                                            IntLiteral(
                                                                                                                                                10))]),
                                                                                                                                IntLiteral(
                                                                                                                                    1)))])),
                                       For(Id("i"), IntLiteral(1), BinaryOp("<", Id("i"), IntLiteral(10)),
                                           IntLiteral(1), ([], [Assign(ArrayCell(Id("count"), [Id("i")]),
                                                                       BinaryOp("+", ArrayCell(Id("count"), [Id("i")]),
                                                                                ArrayCell(Id("count"), [
                                                                                    BinaryOp("-", Id("i"),
                                                                                             IntLiteral(1))])))])),
                                       For(Id("i"), BinaryOp("-", Id("n"), IntLiteral(1)),
                                           BinaryOp(">=", Id("i"), IntLiteral(0)), UnaryOp("-", IntLiteral(1)), ([], [
                                               Assign(ArrayCell(Id("output"), [BinaryOp("-", ArrayCell(Id("count"), [
                                                   BinaryOp("%",
                                                            BinaryOp("\\", ArrayCell(Id("arr"), [Id("i")]), Id("exp")),
                                                            IntLiteral(10))]), IntLiteral(1))]),
                                                      ArrayCell(Id("arr"), [Id("i")])), Assign(ArrayCell(Id("count"), [
                                                   BinaryOp("%",
                                                            BinaryOp("\\", ArrayCell(Id("arr"), [Id("i")]), Id("exp")),
                                                            IntLiteral(10))]), BinaryOp("-", ArrayCell(Id("count"), [
                                                   BinaryOp("%",
                                                            BinaryOp("\\", ArrayCell(Id("arr"), [Id("i")]), Id("exp")),
                                                            IntLiteral(10))]), IntLiteral(1)))])),
                                       For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("n")), IntLiteral(1), ([],
                                                                                                                    [
                                                                                                                        Assign(
                                                                                                                            ArrayCell(
                                                                                                                                Id(
                                                                                                                                    "arr"),
                                                                                                                                [
                                                                                                                                    Id(
                                                                                                                                        "i")]),
                                                                                                                            ArrayCell(
                                                                                                                                Id(
                                                                                                                                    "count"),
                                                                                                                                [
                                                                                                                                    Id(
                                                                                                                                        "i")]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_complex_program_03(self):
        input = """Function: partition
                Parameter: start, end
                Body:
                    Var: size, i, j;
                    Var: p;
                    size = end - start;
                    i = 1;
                    j = size - 1;
                    p = start[0];
                    While True Do
                        While start[i] < p Do
                            If i == size - 1 Then
                                Break;
                            EndIf.
                        EndWhile.

                        While start[j] > p Do
                            If j == 0 Then
                                Break;
                            EndIf.
                        EndWhile.

                        If i >= j Then
                            Break;
                        EndIf.

                        swap(start[i], start[j]);
                    EndWhile.
                    swap(start[0], start[j]);
                    Return start[j];

                EndBody.
                """
        expect = Program([FuncDecl(Id("partition"), [VarDecl(Id("start"), [], None), VarDecl(Id("end"), [], None)], (
        [VarDecl(Id("size"), [], None), VarDecl(Id("i"), [], None), VarDecl(Id("j"), [], None),
         VarDecl(Id("p"), [], None)],
        [Assign(Id("size"), BinaryOp("-", Id("end"), Id("start"))), Assign(Id("i"), IntLiteral(1)),
         Assign(Id("j"), BinaryOp("-", Id("size"), IntLiteral(1))),
         Assign(Id("p"), ArrayCell(Id("start"), [IntLiteral(0)])), While(BooleanLiteral(True), ([], [
            While(BinaryOp("<", ArrayCell(Id("start"), [Id("i")]), Id("p")), (
            [], [If([(BinaryOp("==", Id("i"), BinaryOp("-", Id("size"), IntLiteral(1))), [], [Break()])], ([], []))])),
            While(BinaryOp(">", ArrayCell(Id("start"), [Id("j")]), Id("p")),
                  ([], [If([(BinaryOp("==", Id("j"), IntLiteral(0)), [], [Break()])], ([], []))])),
            If([(BinaryOp(">=", Id("i"), Id("j")), [], [Break()])], ([], [])),
            CallStmt(Id("swap"), [ArrayCell(Id("start"), [Id("i")]), ArrayCell(Id("start"), [Id("j")])])])),
         CallStmt(Id("swap"), [ArrayCell(Id("start"), [IntLiteral(0)]), ArrayCell(Id("start"), [Id("j")])]),
         Return(ArrayCell(Id("start"), [Id("j")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_all_399(self):
        input = """
                    Function: main
                    Body:
                    Var: r = 10;
                    EndBody.
                """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("r"), [], IntLiteral(10))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_funcDeclar_all(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
        EndBody.
        """
        expect = Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("x"), IntLiteral(10)),
            ]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))


    def test_random_01(self):
        input = """Var: x, y, z[100][0x4][0o12];
                Function: func1
                Parameter: x, y, z[100][0x4][0o12]
                Body:
                    print("\\n");
                    Return;
                EndBody.
                Function: func2
                Parameter: abc
                Body:
                EndBody.
                """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [100, 0x4, 0o12], None),
                          FuncDecl(Id("func1"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None),
                                                 VarDecl(Id("z"), [100, 4, 10], None)],
                                   ([], [CallStmt(Id("print"), [StringLiteral("\\n")]), Return(None)])),
                          FuncDecl(Id("func2"), [VarDecl(Id("abc"), [], None)], ([], []))])

        #expect = Program([VarDecl(Id(x)),VarDecl(Id(y)),VarDecl(Id(z),[100,4,10]),FuncDecl(Id(func1)[VarDecl(Id(x)),VarDecl(Id(y)),VarDecl(Id(z),[100,4,10])],([][CallStmt(Id(print),[StringLiteral(\n)]),Return()])),FuncDecl(Id(func2)[VarDecl(Id(abc))],([][]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 500))


    def test_ifStmtInFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1;
        ElseIf x > y Then
        ElseIf x < y Then
        Else
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [VarDecl(Id("a"), [83], [])],
                     (
                         [],
                         [If(
                             [
                                 (BinaryOp("==", Id("x"), Id("y")),
                                  [],
                                  [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                                  ),
                                 (
                                     BinaryOp(">", Id("x"), Id("y")),
                                     [],
                                     []
                                 ),
                                 (
                                     BinaryOp("<", Id("x"), Id("y")),
                                     [],
                                     []
                                 )
                             ],
                             ([], []))
                         ]
                     ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 501))



    def testttast(self):
        input = """Var: x[10] ;"""
        #expect = "Program([VarDecl(Id(x),[10])])"
        expect = Program([VarDecl(Id("x"),[10],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,502))