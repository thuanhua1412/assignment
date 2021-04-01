//Student ID: 1814226
grammar BKIT;

@lexer::header {
from lexererr import *
}



options{
	language=Python3;
}
/**2. Program Structure*/
program: var_declare* func_declare*  EOF ;

//Var declaration
var_declare: VAR COLON var_list SEMI;

var_list: variable (COMMA variable)*;

variable: ID dimen* (ASSIGN literal)?;

dimen: LSB INT_LIT RSB;


// Func Decleration
func_declare: FUNC COLON ID (PARA COLON para_list)? BODY COLON var_declare* stmts_list ENDBODY DOT;

para: ID (LSB INT_LIT RSB)* ;
para_list: para (COMMA para)*;
/**
 * 7 Statements
 */

stmt
    : if_stmt
    | while_stmt | for_stmt | do_while_stmt
    | brk_stmt | cont_stmt | ret_stmt
    | assign_stmt
    | call_stmt
    ;


/**7.1 Variable Declaration Statement*/



/**7.2 Assignment Statement*/
assign_stmt: ID index_operators* ASSIGN exp SEMI;

/**7.3 If Statement*/
if_stmt
    : IF exp_bool THEN stmts_list elseif* (ELSE stmts_list)? ENDIF DOT
    ;


elseif
    : ELSEIF exp_bool THEN stmts_list
    ;

/*
 *
 *
 Loop Statement
 *
 *
 */

/**7.4 For Statement*/
for_stmt: FOR LP ID ASSIGN exp COMMA exp_bool COMMA update_exp RP DO stmts_list ENDFOR DOT;

/**7.5 While Statement*/
while_stmt: WHILE exp_bool DO stmts_list ENDWHILE DOT;

/**7.6 Do-While Statement*/
do_while_stmt: DO stmts_list WHILE exp_bool ENDDO DOT;

/**7.7 Break Statement*/
brk_stmt: BREAK SEMI;

/**7.8 Continue Statement*/
cont_stmt: CONT SEMI;

/**7.9 Call Statement*/
call_stmt: ID LP exp_list? RP SEMI;

/**7.10 Return Statement*/
ret_stmt: RETURN exp? SEMI;


/*
 *
 *
 Expressions
 *
 *
 */
exp_bool: exp;
exp_int: exp;
exp_float: exp;
exp_str: exp;
update_exp: exp;

exp: exp1 ( EQU| NEQU | GT | LT | GTE | LTE | NEQUF | GTF | GTEF | LTF | GTEF | LTEF) exp1 | exp1;

exp1: exp1 (AND | OR) exp2 | exp2;

exp2: exp2 (ADD | ADDFLOAT | SUB | SUBFLOAT) exp3 | exp3 ;

exp3: exp3 ( DIV | MUL | DIVFLOAT | MULFLOAT | MOD ) exp4 | exp4;

exp4: NOT exp4 | exp5;

exp5: (SUB| SUBFLOAT) exp5 | operands;

operands
    : literal
    | ID
    | ID index_operators*
    | call_exp
    | LP exp RP
    ;

index_operators: LSB exp RSB;

call_exp: ID LP exp_list? RP;






ids_list: ID (COMMA ID)* ;

stmts_list: var_declare* stmt*;





/*
 * Utilities
 */
exp_list: exp (COMMA exp)*;

literal
    : INT_LIT
    | FLOAT_LIT
    | STRING_LIT
    | bool_lit
    | array_lit
    ;


/** Lexer Declaration */



/**
 Keyword in BKIT
 *
 */

BODY: 'Body';

BREAK: 'Break';

CONT: 'Continue';

DO: 'Do';

ELSE: 'Else';

ELSEIF: 'ElseIf';

ENDBODY: 'EndBody';

ENDIF: 'EndIf';

ENDFOR: 'EndFor';

ENDWHILE: 'EndWhile';

FOR: 'For';

FUNC: 'Function';

IF: 'If';

PARA: 'Parameter';

RETURN: 'Return';

THEN: 'Then';

VAR: 'Var';

WHILE: 'While';

TRUE: 'True';

FALSE: 'False';

ENDDO: 'EndDo';





// operator

ASSIGN: '=';

//INT TYPE
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '\\';
MOD: '%';

LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

EQU: '==';
NEQU: '!=';

//FLOAT TYPE
ADDFLOAT: '+.';
SUBFLOAT: '-.';
MULFLOAT: '*.';
DIVFLOAT: '\\.';

LTF: '<.';
GTF: '>.';
LTEF: '<=.';
GTEF: '>=.';

NEQUF: '=/=';

AND: '&&';
OR: '||';
NOT: '!';
/*
 *
 *
 *
 */

//Separators
LP: '(';// Left Parenthesis
RP: ')';// Right Parenthesis
LCB: '{';// Left Curly Bracket
RCB: '}';// Right Curly Bracket
LSB: '[';// Left Square Bracket
RSB: ']';// Right Square Bracket

SEMI: ';' ;// Semicolon
COLON: ':' ;//Colon
COMMA: ',';//Comma
DOT: '.';

bool_lit: TRUE | FALSE;

STRING_LIT: '"' STR_CHAR* '"'
	{
		y = str(self.text)
		self.text = y[1:-1]
	}
	;

/*
ARRAY_LIT
    : LCB INT_LIT (COMMA INT_LIT)* RCB
    | LCB FLOAT_LIT (COMMA FLOAT_LIT)* RCB
    | LCB '"'STRING_LIT'"' (COMMA '"'STRING_LIT'"')* RCB
    | LCB ARRAY_LIT (COMMA ARRAY_LIT)* RCB
    | LCB ('True' | 'False') (COMMA ('True' | 'False'))* RCB
    ;
*/
FLOAT_LIT
    : INT_DEC DECIMAL_PART EXPONENT? // 1.5(e-4) | 1. | 1.5 | 0.2
	| INT_DEC DECIMAL_PART? EXPONENT // 12e-5 | 14.e-1
	;
fragment DECIMAL_PART: DOT DIGIT*;

INT_LIT: INT_DEC | INT_HEX | INT_OCT;

fragment INT_DEC: [1-9]DIGIT* | '0' ;//DECIMAL
fragment INT_HEX:'0'[xX][1-9A-F][0-9A-F]* ;//HEXADECIMAL
fragment INT_OCT:'0'[oO][1-7][0-7]* ;//OCTAl

array_lit: LCB literal (COMMA literal)* RCB;

fragment EXPONENT: [eE] ('+' | '-')? DIGIT+ ;
fragment DIGIT: [0-9] ;


ID: [a-z][_a-zA-Z0-9]* ;

fragment CMT_CHAR: ~[*];
//CMT: '**'([*]?CMT_CHAR+)*'**' -> skip;
CMT: '**'.*?'**' -> skip;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines



/*UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = ['\r','\n']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;
	*/
UNCLOSE_STRING:'"' STR_CHAR* ([\n\r] | EOF)?
    {
        y = str(self.text)
        error_sequence =['\r','\n']
        if(y[-1] in error_sequence):
            raise UncloseString(y[1:-1])
        else:
            raise UncloseString(y[1:])
    }
    ;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;

ERROR_CHAR: .
    {
		raise ErrorToken(self.text)
	}
	;
UNTERMINATED_COMMENT: '**'([*]?CMT_CHAR+)*
    {
        raise UnterminatedComment()
    }
    ;

fragment STR_CHAR:~[\n\r"'\\] | ESC_SEQ;
fragment ESC_SEQ: '\\'[btnfr\\'] | '\'"';
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\'' ~'"' ;