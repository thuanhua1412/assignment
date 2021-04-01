import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_quote_string(self):
        input = """"He asked me: '"Where is John?'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 100))

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_comment(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" **abc** def **ahsdj** """, """def,<EOF>""", 108))

    def test_comment1(self):
        input = """ ** *This*is*a*legal*comment*
         afs
         afsfa
         ** """
        expect = """<EOF> ajs"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))

    def test_comment2(self):
        input = """ **this is an unterminate comment"""
        expect = """Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))

    def test_comment3(self):
        input = """ **this is ** comment**"""
        expect = """comment,Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 111))

    def test_comment4(self):
        input = """ ** This is a\n"""
        input += """* multi-line\n"""
        input += """* comment.\n"""
        input += """**"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 112))

    def test_invalid_escape_quote_1(self):
        input = """ "This is another invalid ''" quote" """
        expect = """Illegal Escape In String: This is another invalid ''"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))

    def test_more_float(self):
        input = "0.0e+3 0.1e-2123 123e-2321 1e+3 1111.1e-1"
        expect = "0.0e+3,0.1e-2123,123e-2321,1e+3,1111.1e-1,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))

    def test_unterminated_comment(self):
        """test an unterminated comment block"""
        input = """**Just an unterminated comment passes by"""
        expect = """Unterminated Comment"""
        self.assertTrue((TestLexer.checkLexeme(input, expect, 115)))

    def test_illegal_single_quote(self):
        input = """ "this is wrong single quote \\' """
        expect = """Unclosed String: this is wrong single quote \\' """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))

    def test_illegal_single_quote1(self):
        input = """ "abc ' def " """
        expect = """Illegal Escape In String: abc ' """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))

    def test_illegal_escape11(self):
        input = """ "ansdkl \b" """
        expect = """ansdkl ,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))

    def test_float_literal(self):
        """ Test Real Literal """
        input = """1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3"""
        expect = """1.2,1.,.,1,1e2,1.2E-2,1.2e-2,.,1E2,9.0,12e8,0.33E-3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test_for_stmt(self):
        input = """For(i=0,i<10,i++) Do
                 writeln(i);
                 EndFor."""
        expect = """For,(,i,=,0,,,i,<,10,,,i,+,+,),Do,writeln,(,i,),;,EndFor,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))

    #Identifiers

    def test_id(self):
        input = """aBcD xyzT a_12asT"""
        expect = """aBcD,xyzT,a_12asT,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,121))

    def test_id1(self):
        input = """ABcD xyzT a_12asT"""
        expect = """Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,122))

    def test_id2(self):
        input = """aBcD _yzT a_12asT"""
        expect = """aBcD,Error Token _"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,123))

    def test_id3(self):
        input = """aBcD xyzT 1_12T"""
        expect = """aBcD,xyzT,1,Error Token _"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,124))

    def test_KeyWords(self):
        input = """Function: test\n"""
        input+= """Body:\n"""
        input+= """a = -.-.a;\n"""
        input+= """EndBody."""
        expect = """Function,:,test,Body,:,a,=,-.,-.,a,;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,125))

    def test_KeyWords2(self):
        input = """For (i = 0, i < 10, 1) Do Return;"""
        expect = """For,(,i,=,0,,,i,<,10,,,1,),Do,Return,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,126))

    def test_KeyWords3(self):
        input = """If True Then Continue;"""
        expect = """If,True,Then,Continue,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,127))

    #Operators
    def test_Operators(self):
        input = """a++123-.fbH;"""
        expect = """a,+,+,123,-.,fbH,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,128))

    def test_Operators1(self):
        input = """a =/= b / c"""
        expect = """a,=/=,b,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,129))

    def test_Operators2(self):
        input = """a =.= b / c"""
        expect = """a,=,.,=,b,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,130))

    #Separate Operators
    def test_Operators3(self):
        input = """a[2] = {1,2,3}"""
        expect = """a,[,2,],=,{,1,,,2,,,3,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,131))

    def test_Operators4(self):
        input = """Var: a[2] = {1,2,3}"""
        expect = """Var,:,a,[,2,],=,{,1,,,2,,,3,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,132))

    def test_Operators5(self):
        input = """a[2] = (a+b\c)"""
        expect = """a,[,2,],=,(,a,+,b,\,c,),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,133))

    #Literals
    """Interger Literal"""
    def test_IntLit(self):
        input = """0000123"""
        expect = """0,0,0,0,123,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,134))

    def test_IntLit1(self):
        input = """0X1AF 0xAFB 0o128 0O2344"""
        expect = """0X1AF,0xAFB,0o12,8,0O2344,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,135))

    def test_IntLit2(self):
        input = """0X1AFG 0xAFB 0o1289 0O2344"""
        expect = """0X1AF,Error Token G"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,136))

    """Float Literal"""
    def test_FloatLit(self):
        input = """12e3 012e-7 14.5 13."""
        expect = """12e3,0,12e-7,14.5,13.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,137))

    def test_FloatLit1(self):
        input = """12e3 012e-7 12.05e+4 13. .25"""
        expect = """12e3,0,12e-7,12.05e+4,13.,.,25,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,138))

    def test_BoolLit(self):
        input = """True False TrUe Fllase"""
        expect = """True,False,Error Token T"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,139))

#String Literal
    #Error Char
    def test_StringLit(self):
        input = """a_bc?a"""
        expect = """a_bc,Error Token ?"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,140))

    #Unclosed String
    def test_StringLit1(self):
        input = """ "This is an Unclosed String"""
        expect = """Unclosed String: This is an Unclosed String"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,141))

    def test_StringLit2(self):
        input = """ "This is another Unclosed String\n"""""
        expect = """Unclosed String: This is another Unclosed String"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,142))

    def test_StringLit3(self):
        input = """ "And another one Unclosed String\r"""""
        expect = """Unclosed String: And another one Unclosed String"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,143))

    #Illegal Escape
    def test_StringLit4(self):
        input = """ "This is an illegal escape: \\e"""
        expect = """Illegal Escape In String: This is an illegal escape: \e"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,144))

    def test_StringLit5(self):
        input = """ "Here some legal escape: \\b \\r \\t \\' \\\\" """
        expect = """Here some legal escape: \\b \\r \\t \\' \\\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,145))

    def test_StringLit6(self):
        input = """ "Dog: '"Gau Gau!!'"" """
        expect = """Dog: '"Gau Gau!!'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,146))

    def test_StringLit7(self):
        input = """ "Cat: '"Meow Meow!!'"" """
        expect = """Cat: '"Meow Meow!!'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,147))


    #Array Literal

    def test_token_while_stmt(self):
        input = """While (i < 5)
                 a[i] = b +. 1.0;
                 i = i + 1;
                EndWhile."""
        expect = """While,(,i,<,5,),a,[,i,],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test_token_return_stmt(self):
        """test token recognizer in a return stmt"""
        input = """Return n * fact(n-1);"""
        expect = """Return,n,*,fact,(,n,-,1,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_float_operator(self):
        """test some float operator"""
        input = "-. +. *. >. <. >=. <=. =/="
        expect = "-.,+.,*.,>.,<.,>=.,<=.,=/=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    def test_quote_string(self):
        input = """"He asked me: '"Where is John?'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))

    def test_boolean(self):
        input = "|| &&"
        expect = "||,&&,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))

    def test_wrong_identifier(self):
        input = "Uppercase"
        expect = "Error Token U"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

    def test_case_sensitivity(self):
        input = """writeln wRilent wrIteln"""
        expect = """writeln,wRilent,wrIteln,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))

    def test_illegal_char(self):
        input = "a = @1"
        expect = "a,=,Error Token @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))

    def test_string_with_escaped_double_quote(self):
        input = """ "Hi,My name is '"Lan'"" """
        expect = """Hi,My name is '"Lan'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

    def test_string_with_escaped_single_quote(self):
        input = """ "His name has an \\'A\\' character" """
        expect = """His name has an \\'A\\' character,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    def test_float_literal1(self):
        """ Test Real Literal """
        input = """1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3"""
        expect = """1.2,1.,.,1,1e2,1.2E-2,1.2e-2,.,1E2,9.0,12e8,0.33E-3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test_int_literal(self):
        input = " 0 12 123 1234  12345 123456"
        expect = "0,12,123,1234,12345,123456,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))

    def test_unclosed_string_eof(self):
        input = """s = "asdf"""
        expect = """s,=,Unclosed String: asdf"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    def test_illegal_escape12(self):
        input = """ "14 + 12 + 17+ 05 = \\o'\"123" """
        expect = "Illegal Escape In String: 14 + 12 + 17+ 05 = \\o"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test_unclosed_string(self):
        input = """ **cMt** "stR;" "STr" "StR" "Something forget"""
        expect = """stR;,STr,StR,Unclosed String: Something forget"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

    def test_bool_stmt(self):
        input = """If bool_of_string ("True") Then EndIf."""
        expect = """If,bool_of_string,(,True,),Then,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))

    def test_continue_stmt(self):
        input = "Continue;"
        expect = "Continue,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

    def test_break_stmt(self):
        input = "Break;"
        expect = "Break,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test_0_leaded_number(self):
        input = "01234"
        expect = "0,1234,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

    def test_function(self):
        input = "foo(2);"
        expect = "foo,(,2,),;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

    def test_function1(self):
        input = """Function:main
                     Body:
                     x = "This string is not terminated
                     y = 12
                     fact(x)
                     Endbody."""
        expect = """Function,:,main,Body,:,x,=,Unclosed String: This string is not terminated"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

    def test_function2(self):
        input = """Function: main
                   Body:
                   x = "This is a terminated string";
                   fact (x);
                   EndBody."""
        expect = """Function,:,main,Body,:,x,=,This is a terminated string,;,fact,(,x,),;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

    def test_escape_formfeed(self):
        input = """ "This is a formfeed \\f" """
        expect = """This is a formfeed \\f,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

    def test_escape_back_slash(self):
        input = """ "This is a backslash \\a asd" """
        expect = """Illegal Escape In String: This is a backslash \\a"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

    def test_escape_tab(self):
        input = """ "This is a tab \t" """
        expect = """This is a tab \t,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test_empty_comment(self):
        input = "****"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test_empty_string(self):
        input = """ "" """
        expect = """,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test_unclosed_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Unclosed" "String""","""Unclosed,Unclosed String: String""",175))

    def test_cmt_nested_string(self):
        input = """"Just a string with '"quoted **comment**'" inside" """
        expect = """Just a string with '"quoted **comment**'" inside,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_all_keyword(self):
        input = "Body Break Continue Do Else ElseIf EndBody EndIf EndFor EndWhile For Function If Parameter Return Then Var While True False EndDo"
        expect = "Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,If,Parameter,Return,Then,Var,While,True,False,EndDo,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

    def test_keyword_in_comment(self):
        input = """**Var: i=0**"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_string_with_quote(self):
        input = """ "'"Where is Mr.Thuan?'"" """
        expect = """'"Where is Mr.Thuan?'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_weird_float(self):
        self.assertTrue(TestLexer.checkLexeme("0.0 0.0e1 0.0e-123", "0.0,0.0e1,0.0e-123,<EOF>", 179))

    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme("0.e123 1.e12 4.12 0.1e1", "0.e123,1.e12,4.12,0.1e1,<EOF>", 180))

    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("12345. 0.3e-1 0.001e+2 12.0e45 12.0e-12",
                                              "12345.,0.3e-1,0.001e+2,12.0e45,12.0e-12,<EOF>", 181))

    def test_int_hexa(self):
        self.assertTrue(TestLexer.checkLexeme("0x4517 0xAEFCD 0XA0FCE", "0x4517,0xAEFCD,0XA0FCE,<EOF>", 182))

    def test_int_octal(self):
        self.assertTrue(TestLexer.checkLexeme("0o1754651 0O10154", "0o1754651,0O10154,<EOF>", 183))

    def test_int_octal_1(self):
        self.assertTrue(TestLexer.checkLexeme("0o01234", "0,o01234,<EOF>", 184))

    def test_decimal(self):
        self.assertTrue(TestLexer.checkLexeme("04451", "0,4451,<EOF>", 185))

    def test_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("0x145", "0x145,<EOF>", 186))

    def test_identifier1(self):
        self.assertTrue(TestLexer.checkLexeme("Var _SAD,funNNy;", "Var,Error Token _", 187))

    def test_special_character(self):
        input = ", > ; : - = ' + . / [ ] ( ) { }"
        expect = ",,>,;,:,-,=,Error Token '"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

    def test_real_declare(self):
        input = """Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                EndBody."""
        expect = """Body,:,Var,:,r,=,10.,,,v,;,v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

    def test_invalid_escape_quote(self):
        input = """ "this is invalid 'a string" """
        expect = """Illegal Escape In String: this is invalid 'a"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

    def test_token_return_stmt1(self):
        """test token recognizer in a return stmt"""
        input = """Return foo(2) * func(3);"""
        expect = """Return,foo,(,2,),*,func,(,3,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

    def test_illegal_escape8(self):
        input = """ "Hello\\World" """
        expect = """Illegal Escape In String: Hello\\W"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

    def test_illegal_escape9(self):
        input = """**this is cmt** + 1.4 "CS\\EHcMUT" """
        expect = """+,1.4,Illegal Escape In String: CS\\E"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

    def test_keyword_in_comment1(self):
        """test keyword in commnet"""
        input = """**Body:\n"""
        input += """Parameter: n\n"""
        input += """EndBody.\n"""
        input += """**"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))

    def test_double_escape_string(self):
        """test string with double escape sequence"""
        input = """ "This is a string with consecutive escape \\n\\n" """
        expect = """This is a string with consecutive escape \\n\\n,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

    def test_small_declare(self):
        input = """Var: c,d = 6,e,f"""
        expect = """Var,:,c,,,d,=,6,,,e,,,f,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

    def test_small_body(self):
        input = """Function: foo
                   Parameter: a,b
                   Body:
                        Return a+b;
                   EndBody."""
        expect = """Function,:,foo,Parameter,:,a,,,b,Body,:,Return,a,+,b,;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))


    def test_illegal_escape_comment(self):
        """test an invalid escaped sequence inside a comment"""
        self.assertTrue(TestLexer.checkLexeme("**This is a test commen \\a**", "<EOF>", 198))

    def test_underscore_indentifier(self):
        """test identifier with an underscore"""
        self.assertTrue(TestLexer.checkLexeme("_Myname", "Error Token _", 199))

    def test_underscore_indentifie1r(self):
        """test identifier with an underscore"""
        self.assertTrue(TestLexer.checkLexeme("a >. b", "a,>.,b,<EOF>", 1000))

