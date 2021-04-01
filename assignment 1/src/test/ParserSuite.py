import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x,y;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_simple_function11(self):
        input = """Function:test_func\n"""
        input+= """Body:\n"""
        input += """If bool_of_string ("True") Then\n"""
        input+= """a = int_of_string (read ());\n"""
        input+= """b = float_of_int (a) +. 2.0;\n"""
        input+= """EndIf.\n"""
        input+= """EndBody.\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_simple_function10(self):
        input = """Function:thinh\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Function:thinhthinh\n"""
        input += """Body:\n"""
        input += """y = a +2 *4 + a[1][2][23][1] +"string";\n"""
        input += """EndBody.\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_simple_function9(self):
        input = """Function:thinh\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        input += """Function:thinhthinh\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_simple_function8(self):
        input = """Function:meow\n"""
        input += """Body:\n"""
        input += """For(i = 4,i<1,i++) Do\n"""
        input += """i=i-1\n"""
        input += """EndFor.\n"""
        input += """EndBody.\n"""
        expect = """Error on line 3 col 16: +"""
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_simple_function7(self):
        input = """Function:woof\n"""
        input += """Body:\n"""
        input += """If a == 1 Then !b;\n"""
        input += """EndBody.\n"""
        expect = """Error on line 3 col 15: !"""
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_simple_function6(self):
        input = """Function:wooof\n"""
        input += """Body:\n"""
        input += """If a == 3 Then b=b-1;\n"""
        input += """Else b=c;\n"""
        input += """EndBody.\n"""
        expect = """Error on line 5 col 0: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_simple_function5(self):
        input = """Function:wOOF\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_simple_function4(self):
        input = """Function:ruff\n"""
        input += """Parameter:array[3]\n"""
        input += """Body:\n"""
        input += """EndBody.\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_simple_function3(self):
        input = """Function:fact1\n"""
        input += """Body:\n"""
        input += """Var: string = "This is a string"\n"""
        input += """string= string + 2;\n"""
        input += """Return string;\n"""
        input += """EndBody.\n"""
        expect = """Error on line 4 col 0: string"""
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_simple_function2(self):
        input = """Function:fact1\n"""
        input += """Parameter: n\n"""
        input += """Body:\n"""
        input += """Return n*fact1(n-1);\n"""
        input += """EndBody.\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_simple_function(self):
        input = """Var: a,bc,d\n"""
        input += """Function: fact\n"""
        input += """Body:\n"""
        input += """a= a+2;\n"""
        input += """While a==2 Do b=b-1\n"""
        input += """EndWhile."""
        input += """EndBody."""
        expect = """Error on line 2 col 0: Function"""
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_simple_declare8(self):
        input = """Var: a,b,c,d,e=4,s"""
        expect = """Error on line 1 col 18: <EOF>"""
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_simple_declare7(self):
        input = """Var: variable,y[a[10]];"""
        expect = """Error on line 1 col 16: a"""
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_simple_declare6(self):
        input = """VaR:variable,y[100]"""
        expect = """V"""
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_simple_declare5(self):
        input = """Var:l,a[10][12]"""
        expect = """Error on line 1 col 15: <EOF>"""
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_simple_declare4(self):
        input = """Var:x,x,y[10];"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_simple_declare3(self):
        input = """Var: x=1,y=2,k[10][4];"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_simple_declare2(self):
        input = """Var: x,z,y[10];"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_Var_Declare(self):
        input = """Var: a = 0, c, d[2][3], e[2] = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def testcase_5(self):
        input = """Var: x = {{1,2,3},{4,5,6}};
        **Another global variable declaration**
        Var: y = True;
        Var: temp = 1.876 +. 78541;"""
        expect = "Error on line 4 col 26: +."
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_something(self):
        input = """
        Var: zzz;
        ** Comment 1 **
        Function: foobalu_undenied
            Parameter: a[2][5]
        Body:
        ** Comment 2 **
        If (a + b -. c == 0) Then
            x = b + c - a % 2;
        Else 
            Continue;
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_While_Loop1(self):
        input = """
            Var: parser = 1814226;
            Function: foo
                Parameter: count, x, y, z
                Body:
                While (x = 1.08765 *. 2.098 || True) Do
                    x = x +. 1;
                    y = {1,2,3} *. 985475;
                    z = "This is a string" =/= "abcdxzy";
                EndWhile.
                EndBody.
            """
        expect = "Error on line 6 col 16: While"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_For_Loop(self):
        input = """
            Var: parser = "Hua Thuan";
            Function: foo
                Parameter: count, x, y, z
                Body:
                For (x == 1.25, x < 12, 3) Do
                    x = x +. 1;
                    y = {1,2,3} *. 985475;
                    z = "This is a string" =/= "abcdxzy";
                EndFor.
                EndBody.
            """
        expect = "Error on line 6 col 23: =="
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_something2(self):
        input = """
            Function: foo
                Parameter: x, y, z
                Body:
                If (x =/= 10.098 == 0) Then
                    For(x = 0, x <. 10.098, x + 2) Do
                        While (x > 0.00) Do
                            x = x + 1;
                            print(x);
                            write(x);
                        EndWhile.
                        print(a[2]);
                    EndFor.
                Else Continue;
                EndIf.
                EndBody.
            """
        expect = "Error on line 5 col 33: =="
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_something3(self):
        input = """
            **Comment**
            Function: foo
                Parameter: x, y, z
                Body:
                If (10.098 == 0) Then
                    For(x = 0, x <. 10.098, x + 2) Do
                    ** Comment* **
                        While (x > 0.00) Do
                            x = x + 1;
                            print(x);
                            write(x);
                        EndWhile.
                ** Comment* **
                        print(a[2]);
                    EndFor.
                Else Continue;
                EndIf.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_something4(self):
        input = """
            **Comment**
            Function: main
                Parameter: x, y, z
                Body:
                    Break;
                    Continue;
                    x = foo(1) + foo(2) +. pikachu(123);
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_something5(self):
        input = """
            **Comment**
            Var: c = 5, x, y = {1,2,3};
            Function: main_foo
                Parameter: a[2][10]
                Body:
                    If (x == 0) Then 
                        Break;
                        x = x +. 1.00837;
                        y = y *. 1234;
                    ElseIf (q == 0) Then
                        Continue;
                    EndIf.
                    x = foo(1) + foo(2) +. naruto(123);
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_something6(self):
        input = """
            Var: c = 5, x, y = {1,2,3};
            Function: naruToBaCo
                Parameter: 
                Body:
                    If (x == 0) Then 
                        Break;
                    ElseIf (q == 0) Then
                        Continue;
                    EndIf.
                EndBody.
            """
        expect = "Error on line 5 col 16: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_something7(self):
        input = """
            Var: short = "Long";
            Function: main_foo
                Parameter: y
                Body:
                    If (x == 0) Then 
                        Break;
                    ElseIf (q == 0) Then
                        Continue;
                    EndIf.
                EndBody.

            Function: sub_foo
                Parameter: x
                Body:
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_Var_Declare1(self):
        input = """var: sasuKetamin;"""
        expect = "Error on line 1 col 0: var"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_Var_Declare2(self):
        input = """Var: a,b = 1,c;
        Var: a = 0x123, b = 1.1, c = 5.6, arr[123];
        Var: a = "string", bool = True, a[1][2][3]; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_Func_Declare(self):
        input = """Function: funcName
                    Parameter: a, b,c, e, array[12][34]
                        Body:
                            **Something went wrong**
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_Func_Declare1(self):
        input = """Function: funcName
                    Parameter: a, b,c, e, array[12][34]
                        Body:
                            Var: a,b,c, array[1][2];
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_Error_Var_Dec(self):
        """Error Function: Var declare"""
        input = """Function: funcName
                       Var: a = 5, 5;
                       Parameter: a, b,c, e, array[12][34]
                           Body:
                               Var: a,b,c, array[1][2];
                           EndBody.
                   """
        expect = "Error on line 2 col 23: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_Error_Var_Dec1(self):
        """Error Function: Var declare"""
        input = """Function: funcName
                    Parameter: a, b,c, e, array[12][34]
                        Body:

                        EndBody
                """
        expect = "Error on line 6 col 16: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_Function_Declare(self):
        """Function declare: Assign statement"""
        input="""Function: funcName
                    Parameter: a, b,c, e, array[12][34]
                        Body:
                            a = b + c;
                        EndBody.
                """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_Function_Declare1(self):
        """Function declare: Assign statement"""
        input = """
                Var: array[12];
                Function: funcName
                    Body:
                        v = funcName(n) + v;
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_Continue_Stmt(self):
        input = """
             Function: funcName
                 Parameter: param
                 Body:
                     Var: i, a, b, c, arr[1] = {1,2,3};
                     For (i, i < 10, i + 1) Do
                         If ( i == 1) Then
                             Continue;
                         Else Break;
                         EndIf.
                     EndFor.
                 EndBody.     
             """
        expect = "Error on line 6 col 27: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 240))


    def test_Func_Declareee(self):
        input = """
            Function: funcName
            Parameter: param
            Body:
                Var: arr[12], a, b ,c;
                For(a = 1, a <= 5, a+1) Do
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def testSomethingFunny(self):
        input = """
               Function: funcName
               Parameter: param
               Body:
                   Var: arr[12], a, b ,c;
                   For(a = 1, a <= 14, a + 17) Do
                       If (a + b <= b + c) Then
                           For(b = 12, b < 5, b + 23) Do
                               chayo = "Hua Phuoc Thuan 1814226";
                               println(chayo);
                           EndFor.
                       EndIf.    
                   EndFor.
               EndBody.
           """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def testSomeFunnyThing(self):
        input = """
            Function: funcName
            Parameter: param
            Body:
                Var: arr[14], a, b ,c;
                For(a = 17, a <= 5, a + 1) Do
                    For(b = 14, b <= 17, b + 3) Do
                        For(c = 2, c <= 10, c + 4) Do
                            For(d = 1, d <= 15, d + 5) Do
                                Return "HCMUT CSE K18";
                            EndFor.
                        EndFor.
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_arrayDeclare(self):
        input = """Var: error[];"""
        expect = "Error on line 1 col 11: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_error_var_dec(self):
        input = """Var: a,b = 1, 2 ,c;\n"""
        input += """Function: kaMeyoko\n"""
        input += """Body:\n"""
        input += """EndBody."""
        expect = "Error on line 1 col 14: 2"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def testSomething(self):
        """Simple program: int main() {} """
        input = """Var: a[1] = {2,2}, b, c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_array_declare(self):
        """Simple program: int main() {} """
        input = """Var: b[2][3] =  {{1,2,3}, {2,6,7}}; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_If_Statement(self):
        """Function declare: IF statement"""
        input = """
            Function: funcName
            Parameter: param
            Body:
                Var: a, b;
                If a > b Then println("Hello World");
                Else println("Chao the gioi");
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_Somethingggggg(self):
        input="""
                Var: array[12];
                Function: funcName
                    Body:
                        arr[12] = 3\\4\\5\\6\\7;
                    EndBody.
                """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    #Arithmetic operators

    def test_Arithmetic(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """a = -.-.a;\n"""
        input+= """EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect,250))

    def test_Arithmetic1(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """a = a*b;\n"""
        input+= """b = c % d;\n"""
        input+= """a = a\\b;\n"""
        input+= """EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_Arithmetic2(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """a = a+;\n"""
        input+= """EndBody."""
        expect = "Error on line 3 col 6: ;"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_Arithmetic3(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """a = a+b+c-d*e\\f;\n"""
        input+= """EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_Arithmetic4(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """a = a+-b\\f;\n"""
        input+= """EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_Arithmetic5(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """a = a+--------------------b\\f;\n"""
        input+= """EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_Arithmetic6(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """a = a+ +++++++++++++++++++b;\n"""
        input+= """EndBody."""
        expect = "Error on line 3 col 7: +"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_Arithmetic7(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """b = a----------+f;\n"""
        input+= """EndBody."""
        expect = "Error on line 3 col 15: +"
        self.assertTrue(TestParser.checkParser(input,expect,257))

#Bool Operators
    def test_Bool_Operators(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """b = !!a;\n"""
        input+= """EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_Bool_Operators1(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """b = && a;\n"""
        input+= """EndBody."""
        expect = "Error on line 3 col 4: &&"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_Bool_Operators2(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """b = 1 && a;\n"""
        input+= """EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_Bool_Operators3(self):
        input = """Function: haha\n"""
        input+= """Body:\n"""
        input+= """not = not!"""
        input+= """EndBody."""
        expect = """Error on line 3 col 9: !"""
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_Bool_Operators4(self):
        input = """Function: ohoho\n"""
        input += """Body:\n"""
        input += """notAnd = !not + and && and;"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_Bool_Operators5(self):
        input = """Function: ak49\n"""
        input += """Body:\n"""
        input += """notAnd = !not || !(and && and);"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_Rela_Operators(self):
        input = """Function: babyImReal\n"""
        input += """Body:\n"""
        input += """If a+5 < b Then\n"""
        input += """a = a + 1;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 264))


    def test_Rela_Operators1(self):
        input = """Function: babyImReal\n"""
        input += """Body:\n"""
        input += """If a + 5 = b Then\n"""
        input += """a = a + 1;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 3 col 9: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 265))


    def test_Rela_Operators2(self):
        input = """Function: babyImReal\n"""
        input += """Body:\n"""
        input += """If a + 5 < b || c > d Then\n"""
        input += """a = a + 1;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 3 col 18: >"""
        self.assertTrue(TestParser.checkParser(input, expect, 266))



    def test_Rela_Operators3(self):
        input = """Function: nah_nah\n"""
        input += """Body:\n"""
        input += """If a =. d Then\n"""
        input += """a = a + 1;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 3 col 5: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 267))


    def test_Index_Operators(self):
        input = """Function: babyImReal\n"""
        input += """Body:\n"""
        input += """If (a =/= b) Then\n"""
        input += """a = a + 1;\n"""
        input += """a[3 + foo(2)] = a[b[2][3]] + 4;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_Index_Operators1(self):
        input = """Function: somethingRed\n"""
        input += """Body:\n"""
        input += """If (a <= b) Then\n"""
        input += """a = a + 1 -- 5;\n"""
        input += """a[3 + foo(2) = a[b[2][3]] + 4;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 5 col 13: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 269))


    def test_Index_Operators2(self):
        input = """Function: somethingBlue\n"""
        input += """Body:\n"""
        input += """If (a + b == c + d) Then\n"""
        input += """a = a + 1;\n"""
        input += """a[3 + foo(2)] = a[b52] + 4;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 270))


    def test_Index_Operators3(self):
        input = """Function: babyGetMyGun\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """a = a + 1;\n"""
        input += """a[3 foo(2)] = a[b[2][3]] + 4;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 5 col 4: foo"""
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_Index_Operators4(self):
        input = """Function: babyGetMyGun\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """a = a + 1;\n"""
        input += """a[c = d] = a[b[2][3]] + 4;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 5 col 4: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_Function_Call(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """a = a + 1;\n"""
        input += """c = a * yolooo();\n"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_Function_Call1(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """a = a + 1;\n"""
        input += """c = a * yolooo(;\n"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 5 col 15: ;"""
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_Function_Call2(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """a = a + 1;\n"""
        input += """c = a * yolooo(b,s,);\n"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 5 col 19: )"""
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_Function_Call3(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """a = a + 1;\n"""
        input += """c = a * yolooo(foo(3));\n"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 276))


    def test_Function_Call4(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """a = a + 1;\n"""
        input += """c = a * yolooo(foo(3 + func(2) - arr[14]));\n"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 277))



    def test_Function_Call5(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """a = a + 1;\n"""
        input += """c = a * yolooo(foo(arr[func(2)]));\n"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    #Var declare statement
    def test_Statement(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """Var: r = 10., v;\n"""
        input += """c = a * yolooo(foo(arr[func(2)]));\n"""
        input += """v = (4. \. 3.) *. 3.14 *. r *. r *. r;\n"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 279))


    def test_Statement1(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """c = a * yolooo(foo(arr[func(2)]));\n"""
        input += """Var: r = 10., v;\n"""
        input += """v = (4. \. 3.) *. 3.14 *. r *. r *. r;\n"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 5 col 0: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    #Assignment Statement
    def test_Statement2(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """y = a + foo(2) + b[c[2]][func(10)];\n"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 281))


    def test_Statement3(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """y = a + foo(2) + b[c[2]][func(10)]"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 4 col 34: Return"""
        self.assertTrue(TestParser.checkParser(input, expect, 282))


    def test_Statement4(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """y = a < b;"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_Statement5(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """y + 2 = a;"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 4 col 2: +"""
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_Statement6(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a -- b < 5) Then\n"""
        input += """y = a + foo(2) + b[c[2]][func(10)]"""
        input += """Return sth;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 4 col 34: Return"""
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    #If Statement
    def test_Statement7(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a < b) Then\n"""
        input += """max = b;\n"""
        input += """ElseIf a > b Then\n"""
        input += """max = a;\n"""
        input += """Else max = 0;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 286))


    def test_Statement8(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a < b) Then\n"""
        input += """max = b;\n"""
        input += """Else a = b;\n"""
        input += """Else max = 0;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 6 col 0: Else"""
        self.assertTrue(TestParser.checkParser(input, expect, 287))


    def test_Statement9(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a < b) Then\n"""
        input += """max = b;\n"""
        input += """b = a;\n"""
        input += """Else a = b;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_Statement10(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a < b) Then\n"""
        input += """max = b;\n"""
        input += """b = a;\n"""
        input += """ElseIf a == b Then\n"""
        input += """ElseIf a == b Then\n"""
        input += """ElseIf a == b Then\n"""
        input += """ElseIf a == b Then\n"""
        input += """Else Return;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 289))


    def test_Statement11(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a < b) Then\n"""
        input += """max = b;\n"""
        input += """b = a;\n"""
        input += """ElseIf a == b Then\n"""
        input += """ElseIf a == b \n"""
        input += """ElseIf a == b Then\n"""
        input += """ElseIf a == b Then\n"""
        input += """Else Return;\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """Error on line 8 col 0: ElseIf"""
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_Statement12(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a < b) Then\n"""
        input += """EndIf.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 291))


    def test_Statement13(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """If (a < b) Then\n"""
        input += """EndBody."""
        expect = """Error on line 4 col 0: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect, 292))


    def test_Statement14(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """(a < b) Then\n"""
        input += """EndIf."""
        input += """EndBody."""
        expect = """Error on line 3 col 0: ("""
        self.assertTrue(TestParser.checkParser(input, expect, 293))


    #ForStatement
    def test_Statement15(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """For(i = 0, i < 10, 2) Do\n"""
        input += """writeln(i);\n"""
        input += """EndFor.\n"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_Statement16(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """For(i , i < 2, i+2) Do\n"""
        input += """a = b ----c;\n"""
        input += """EndFor.\n"""
        input += """EndBody."""
        expect = """Error on line 3 col 6: ,"""
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_Statement17(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """For(i = 1, i < 2, i+2) Do\n"""
        input += """a = b ----c;\n"""
        input += """EndFor\n"""
        input += """EndBody."""
        expect = """Error on line 6 col 0: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect, 296))


    #While Statement
    def test_Statement18(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """While a > b Do\n"""
        input += """a = a - 1;\n"""
        input += """EndWhile\n"""
        input += """EndBody."""
        expect = """Error on line 6 col 0: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect, 297))


    def test_Statement19(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """While a > b Do\n"""
        input += """a = a - 1;\n"""
        input += """For(i = 1, i < 2, i+2) Do\n"""
        input += """a = b ----c;\n"""
        input += """EndFor.\n"""
        input += """While b > c Do\n"""
        input += """**Do nothing**\n"""
        input += """EndWhile.\n"""
        input += """Break\n"""
        input += """EndWhile.\n"""
        input += """EndBody."""
        expect = """Error on line 12 col 0: EndWhile"""
        self.assertTrue(TestParser.checkParser(input, expect, 298))


    def test_Statement20(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """While a > b Do\n"""
        input += """a = a - 1;\n"""
        input += """For(i = 1, i < 2, i+2) Do\n"""
        input += """a = b ----c;\n"""
        input += """EndFor.\n"""
        input += """While b > c Do\n"""
        input += """**Do nothing**\n"""
        input += """EndWhile.\n"""
        input += """Break;\n"""
        input += """EndWhile.\n"""
        input += """Return 1;"""
        input += """Return;"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 299))


    def test_Statement21(self):
        input = """Function: yolooo\n"""
        input += """Body:\n"""
        input += """While a > b Do\n"""
        input += """a = a - 1;\n"""
        input += """Continue;"""
        input += """For(i = 1, i < 10 , i+2) Do\n"""
        input += """Return i;"""
        input += """EndFor.\n"""
        input += """While b > c Do\n"""
        input += """**Do nothing**\n"""
        input += """EndWhile.\n"""
        input += """Break;\n"""
        input += """EndWhile.\n"""
        input += """Return;"""
        input += """EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def testttt(self):
        input = """Function:main
        Parameter: x = 10;
        Body:
        EndBody."""
        self.assertTrue(TestParser.checkParser(input,"",301))
