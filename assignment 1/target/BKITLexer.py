# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0214\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\79\u0174\n9\f9\169\u0177\139\39\39\39\3:\3:\3:\5")
        buf.write(":\u017f\n:\3:\3:\5:\u0183\n:\3:\3:\5:\u0187\n:\3;\3;\7")
        buf.write(";\u018b\n;\f;\16;\u018e\13;\3<\3<\3<\5<\u0193\n<\3=\3")
        buf.write("=\7=\u0197\n=\f=\16=\u019a\13=\3=\5=\u019d\n=\3>\3>\3")
        buf.write(">\3>\7>\u01a3\n>\f>\16>\u01a6\13>\3?\3?\3?\3?\7?\u01ac")
        buf.write("\n?\f?\16?\u01af\13?\3@\3@\5@\u01b3\n@\3@\6@\u01b6\n@")
        buf.write("\r@\16@\u01b7\3A\3A\3B\3B\7B\u01be\nB\fB\16B\u01c1\13")
        buf.write("B\3C\3C\3D\3D\3D\3D\7D\u01c9\nD\fD\16D\u01cc\13D\3D\3")
        buf.write("D\3D\3D\3D\3E\6E\u01d4\nE\rE\16E\u01d5\3E\3E\3F\3F\7F")
        buf.write("\u01dc\nF\fF\16F\u01df\13F\3F\5F\u01e2\nF\3F\3F\3G\3G")
        buf.write("\7G\u01e8\nG\fG\16G\u01eb\13G\3G\3G\3G\3H\3H\3H\3I\3I")
        buf.write("\3I\3I\5I\u01f7\nI\3I\6I\u01fa\nI\rI\16I\u01fb\7I\u01fe")
        buf.write("\nI\fI\16I\u0201\13I\3I\3I\3J\3J\5J\u0207\nJ\3K\3K\3K")
        buf.write("\3K\5K\u020d\nK\3L\3L\3L\3L\5L\u0213\nL\3\u01ca\2M\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2")
        buf.write("w<y\2{\2}\2\177\2\u0081\2\u0083=\u0085\2\u0087>\u0089")
        buf.write("?\u008b@\u008dA\u008fB\u0091C\u0093\2\u0095\2\u0097\2")
        buf.write("\3\2\24\3\2\63;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3")
        buf.write("\2\639\3\2\629\4\2GGgg\4\2--//\3\2\62;\3\2c|\6\2\62;C")
        buf.write("\\aac|\3\2,,\5\2\13\f\17\17\"\"\4\3\f\f\17\17\7\2\f\f")
        buf.write("\17\17$$))^^\t\2))^^ddhhppttvv\3\2$$\2\u0222\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2w\3\2\2\2\2\u0083\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\3\u0099\3\2\2\2\5\u009e\3\2\2")
        buf.write("\2\7\u00a4\3\2\2\2\t\u00ad\3\2\2\2\13\u00b0\3\2\2\2\r")
        buf.write("\u00b5\3\2\2\2\17\u00bc\3\2\2\2\21\u00c4\3\2\2\2\23\u00ca")
        buf.write("\3\2\2\2\25\u00d1\3\2\2\2\27\u00da\3\2\2\2\31\u00de\3")
        buf.write("\2\2\2\33\u00e7\3\2\2\2\35\u00ea\3\2\2\2\37\u00f4\3\2")
        buf.write("\2\2!\u00fb\3\2\2\2#\u0100\3\2\2\2%\u0104\3\2\2\2\'\u010a")
        buf.write("\3\2\2\2)\u010f\3\2\2\2+\u0115\3\2\2\2-\u011b\3\2\2\2")
        buf.write("/\u011d\3\2\2\2\61\u011f\3\2\2\2\63\u0121\3\2\2\2\65\u0123")
        buf.write("\3\2\2\2\67\u0125\3\2\2\29\u0127\3\2\2\2;\u0129\3\2\2")
        buf.write("\2=\u012b\3\2\2\2?\u012e\3\2\2\2A\u0131\3\2\2\2C\u0134")
        buf.write("\3\2\2\2E\u0137\3\2\2\2G\u013a\3\2\2\2I\u013d\3\2\2\2")
        buf.write("K\u0140\3\2\2\2M\u0143\3\2\2\2O\u0146\3\2\2\2Q\u0149\3")
        buf.write("\2\2\2S\u014d\3\2\2\2U\u0151\3\2\2\2W\u0155\3\2\2\2Y\u0158")
        buf.write("\3\2\2\2[\u015b\3\2\2\2]\u015d\3\2\2\2_\u015f\3\2\2\2")
        buf.write("a\u0161\3\2\2\2c\u0163\3\2\2\2e\u0165\3\2\2\2g\u0167\3")
        buf.write("\2\2\2i\u0169\3\2\2\2k\u016b\3\2\2\2m\u016d\3\2\2\2o\u016f")
        buf.write("\3\2\2\2q\u0171\3\2\2\2s\u0186\3\2\2\2u\u0188\3\2\2\2")
        buf.write("w\u0192\3\2\2\2y\u019c\3\2\2\2{\u019e\3\2\2\2}\u01a7\3")
        buf.write("\2\2\2\177\u01b0\3\2\2\2\u0081\u01b9\3\2\2\2\u0083\u01bb")
        buf.write("\3\2\2\2\u0085\u01c2\3\2\2\2\u0087\u01c4\3\2\2\2\u0089")
        buf.write("\u01d3\3\2\2\2\u008b\u01d9\3\2\2\2\u008d\u01e5\3\2\2\2")
        buf.write("\u008f\u01ef\3\2\2\2\u0091\u01f2\3\2\2\2\u0093\u0206\3")
        buf.write("\2\2\2\u0095\u020c\3\2\2\2\u0097\u0212\3\2\2\2\u0099\u009a")
        buf.write("\7D\2\2\u009a\u009b\7q\2\2\u009b\u009c\7f\2\2\u009c\u009d")
        buf.write("\7{\2\2\u009d\4\3\2\2\2\u009e\u009f\7D\2\2\u009f\u00a0")
        buf.write("\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3")
        buf.write("\7m\2\2\u00a3\6\3\2\2\2\u00a4\u00a5\7E\2\2\u00a5\u00a6")
        buf.write("\7q\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9")
        buf.write("\7k\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7w\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\b\3\2\2\2\u00ad\u00ae\7F\2\2\u00ae\u00af")
        buf.write("\7q\2\2\u00af\n\3\2\2\2\u00b0\u00b1\7G\2\2\u00b1\u00b2")
        buf.write("\7n\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4\7g\2\2\u00b4\f")
        buf.write("\3\2\2\2\u00b5\u00b6\7G\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8")
        buf.write("\7u\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7K\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\16\3\2\2\2\u00bc\u00bd\7G\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7f\2\2\u00bf\u00c0\7D\2\2\u00c0\u00c1")
        buf.write("\7q\2\2\u00c1\u00c2\7f\2\2\u00c2\u00c3\7{\2\2\u00c3\20")
        buf.write("\3\2\2\2\u00c4\u00c5\7G\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7")
        buf.write("\7f\2\2\u00c7\u00c8\7K\2\2\u00c8\u00c9\7h\2\2\u00c9\22")
        buf.write("\3\2\2\2\u00ca\u00cb\7G\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7f\2\2\u00cd\u00ce\7H\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\24\3\2\2\2\u00d1\u00d2\7G\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7f\2\2\u00d4\u00d5\7Y\2\2\u00d5\u00d6")
        buf.write("\7j\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\26\3\2\2\2\u00da\u00db\7H\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\u00dd\7t\2\2\u00dd\30\3\2\2\2\u00de\u00df")
        buf.write("\7H\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7e\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7p\2\2\u00e6\32\3\2\2\2\u00e7\u00e8")
        buf.write("\7K\2\2\u00e8\u00e9\7h\2\2\u00e9\34\3\2\2\2\u00ea\u00eb")
        buf.write("\7R\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee")
        buf.write("\7c\2\2\u00ee\u00ef\7o\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7t\2\2\u00f3\36")
        buf.write("\3\2\2\2\u00f4\u00f5\7T\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa \3\2\2\2\u00fb\u00fc\7V\2\2\u00fc\u00fd")
        buf.write("\7j\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7p\2\2\u00ff\"")
        buf.write("\3\2\2\2\u0100\u0101\7X\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103$\3\2\2\2\u0104\u0105\7Y\2\2\u0105\u0106")
        buf.write("\7j\2\2\u0106\u0107\7k\2\2\u0107\u0108\7n\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109&\3\2\2\2\u010a\u010b\7V\2\2\u010b\u010c")
        buf.write("\7t\2\2\u010c\u010d\7w\2\2\u010d\u010e\7g\2\2\u010e(\3")
        buf.write("\2\2\2\u010f\u0110\7H\2\2\u0110\u0111\7c\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114\7g\2\2\u0114*\3")
        buf.write("\2\2\2\u0115\u0116\7G\2\2\u0116\u0117\7p\2\2\u0117\u0118")
        buf.write("\7f\2\2\u0118\u0119\7F\2\2\u0119\u011a\7q\2\2\u011a,\3")
        buf.write("\2\2\2\u011b\u011c\7?\2\2\u011c.\3\2\2\2\u011d\u011e\7")
        buf.write("-\2\2\u011e\60\3\2\2\2\u011f\u0120\7/\2\2\u0120\62\3\2")
        buf.write("\2\2\u0121\u0122\7,\2\2\u0122\64\3\2\2\2\u0123\u0124\7")
        buf.write("^\2\2\u0124\66\3\2\2\2\u0125\u0126\7\'\2\2\u01268\3\2")
        buf.write("\2\2\u0127\u0128\7>\2\2\u0128:\3\2\2\2\u0129\u012a\7@")
        buf.write("\2\2\u012a<\3\2\2\2\u012b\u012c\7>\2\2\u012c\u012d\7?")
        buf.write("\2\2\u012d>\3\2\2\2\u012e\u012f\7@\2\2\u012f\u0130\7?")
        buf.write("\2\2\u0130@\3\2\2\2\u0131\u0132\7?\2\2\u0132\u0133\7?")
        buf.write("\2\2\u0133B\3\2\2\2\u0134\u0135\7#\2\2\u0135\u0136\7?")
        buf.write("\2\2\u0136D\3\2\2\2\u0137\u0138\7-\2\2\u0138\u0139\7\60")
        buf.write("\2\2\u0139F\3\2\2\2\u013a\u013b\7/\2\2\u013b\u013c\7\60")
        buf.write("\2\2\u013cH\3\2\2\2\u013d\u013e\7,\2\2\u013e\u013f\7\60")
        buf.write("\2\2\u013fJ\3\2\2\2\u0140\u0141\7^\2\2\u0141\u0142\7\60")
        buf.write("\2\2\u0142L\3\2\2\2\u0143\u0144\7>\2\2\u0144\u0145\7\60")
        buf.write("\2\2\u0145N\3\2\2\2\u0146\u0147\7@\2\2\u0147\u0148\7\60")
        buf.write("\2\2\u0148P\3\2\2\2\u0149\u014a\7>\2\2\u014a\u014b\7?")
        buf.write("\2\2\u014b\u014c\7\60\2\2\u014cR\3\2\2\2\u014d\u014e\7")
        buf.write("@\2\2\u014e\u014f\7?\2\2\u014f\u0150\7\60\2\2\u0150T\3")
        buf.write("\2\2\2\u0151\u0152\7?\2\2\u0152\u0153\7\61\2\2\u0153\u0154")
        buf.write("\7?\2\2\u0154V\3\2\2\2\u0155\u0156\7(\2\2\u0156\u0157")
        buf.write("\7(\2\2\u0157X\3\2\2\2\u0158\u0159\7~\2\2\u0159\u015a")
        buf.write("\7~\2\2\u015aZ\3\2\2\2\u015b\u015c\7#\2\2\u015c\\\3\2")
        buf.write("\2\2\u015d\u015e\7*\2\2\u015e^\3\2\2\2\u015f\u0160\7+")
        buf.write("\2\2\u0160`\3\2\2\2\u0161\u0162\7}\2\2\u0162b\3\2\2\2")
        buf.write("\u0163\u0164\7\177\2\2\u0164d\3\2\2\2\u0165\u0166\7]\2")
        buf.write("\2\u0166f\3\2\2\2\u0167\u0168\7_\2\2\u0168h\3\2\2\2\u0169")
        buf.write("\u016a\7=\2\2\u016aj\3\2\2\2\u016b\u016c\7<\2\2\u016c")
        buf.write("l\3\2\2\2\u016d\u016e\7.\2\2\u016en\3\2\2\2\u016f\u0170")
        buf.write("\7\60\2\2\u0170p\3\2\2\2\u0171\u0175\7$\2\2\u0172\u0174")
        buf.write("\5\u0093J\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2")
        buf.write("\u0177\u0175\3\2\2\2\u0178\u0179\7$\2\2\u0179\u017a\b")
        buf.write("9\2\2\u017ar\3\2\2\2\u017b\u017c\5y=\2\u017c\u017e\5u")
        buf.write(";\2\u017d\u017f\5\177@\2\u017e\u017d\3\2\2\2\u017e\u017f")
        buf.write("\3\2\2\2\u017f\u0187\3\2\2\2\u0180\u0182\5y=\2\u0181\u0183")
        buf.write("\5u;\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0185\5\177@\2\u0185\u0187\3\2\2\2\u0186")
        buf.write("\u017b\3\2\2\2\u0186\u0180\3\2\2\2\u0187t\3\2\2\2\u0188")
        buf.write("\u018c\5o8\2\u0189\u018b\5\u0081A\2\u018a\u0189\3\2\2")
        buf.write("\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018dv\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0193")
        buf.write("\5y=\2\u0190\u0193\5{>\2\u0191\u0193\5}?\2\u0192\u018f")
        buf.write("\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("x\3\2\2\2\u0194\u0198\t\2\2\2\u0195\u0197\5\u0081A\2\u0196")
        buf.write("\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199\u019d\3\2\2\2\u019a\u0198\3")
        buf.write("\2\2\2\u019b\u019d\7\62\2\2\u019c\u0194\3\2\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019dz\3\2\2\2\u019e\u019f\7\62\2\2\u019f")
        buf.write("\u01a0\t\3\2\2\u01a0\u01a4\t\4\2\2\u01a1\u01a3\t\5\2\2")
        buf.write("\u01a2\u01a1\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3")
        buf.write("\2\2\2\u01a4\u01a5\3\2\2\2\u01a5|\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a7\u01a8\7\62\2\2\u01a8\u01a9\t\6\2\2\u01a9")
        buf.write("\u01ad\t\7\2\2\u01aa\u01ac\t\b\2\2\u01ab\u01aa\3\2\2\2")
        buf.write("\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3")
        buf.write("\2\2\2\u01ae~\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b2")
        buf.write("\t\t\2\2\u01b1\u01b3\t\n\2\2\u01b2\u01b1\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b6\5\u0081")
        buf.write("A\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u0080\3\2\2\2\u01b9")
        buf.write("\u01ba\t\13\2\2\u01ba\u0082\3\2\2\2\u01bb\u01bf\t\f\2")
        buf.write("\2\u01bc\u01be\t\r\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u0084\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\n\16\2")
        buf.write("\2\u01c3\u0086\3\2\2\2\u01c4\u01c5\7,\2\2\u01c5\u01c6")
        buf.write("\7,\2\2\u01c6\u01ca\3\2\2\2\u01c7\u01c9\13\2\2\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01cb\3\2\2\2")
        buf.write("\u01ca\u01c8\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3")
        buf.write("\2\2\2\u01cd\u01ce\7,\2\2\u01ce\u01cf\7,\2\2\u01cf\u01d0")
        buf.write("\3\2\2\2\u01d0\u01d1\bD\3\2\u01d1\u0088\3\2\2\2\u01d2")
        buf.write("\u01d4\t\17\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d5\3\2\2")
        buf.write("\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d8\bE\3\2\u01d8\u008a\3\2\2\2\u01d9")
        buf.write("\u01dd\7$\2\2\u01da\u01dc\5\u0093J\2\u01db\u01da\3\2\2")
        buf.write("\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0")
        buf.write("\u01e2\t\20\2\2\u01e1\u01e0\3\2\2\2\u01e1\u01e2\3\2\2")
        buf.write("\2\u01e2\u01e3\3\2\2\2\u01e3\u01e4\bF\4\2\u01e4\u008c")
        buf.write("\3\2\2\2\u01e5\u01e9\7$\2\2\u01e6\u01e8\5\u0093J\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2")
        buf.write("\u01e9\u01ea\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01ec\u01ed\5\u0097L\2\u01ed\u01ee\bG\5\2\u01ee")
        buf.write("\u008e\3\2\2\2\u01ef\u01f0\13\2\2\2\u01f0\u01f1\bH\6\2")
        buf.write("\u01f1\u0090\3\2\2\2\u01f2\u01f3\7,\2\2\u01f3\u01f4\7")
        buf.write(",\2\2\u01f4\u01ff\3\2\2\2\u01f5\u01f7\t\16\2\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8")
        buf.write("\u01fa\5\u0085C\2\u01f9\u01f8\3\2\2\2\u01fa\u01fb\3\2")
        buf.write("\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fe")
        buf.write("\3\2\2\2\u01fd\u01f6\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0202\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0202\u0203\bI\7\2\u0203\u0092\3")
        buf.write("\2\2\2\u0204\u0207\n\21\2\2\u0205\u0207\5\u0095K\2\u0206")
        buf.write("\u0204\3\2\2\2\u0206\u0205\3\2\2\2\u0207\u0094\3\2\2\2")
        buf.write("\u0208\u0209\7^\2\2\u0209\u020d\t\22\2\2\u020a\u020b\7")
        buf.write(")\2\2\u020b\u020d\7$\2\2\u020c\u0208\3\2\2\2\u020c\u020a")
        buf.write("\3\2\2\2\u020d\u0096\3\2\2\2\u020e\u020f\7^\2\2\u020f")
        buf.write("\u0213\n\22\2\2\u0210\u0211\7)\2\2\u0211\u0213\n\23\2")
        buf.write("\2\u0212\u020e\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0098")
        buf.write("\3\2\2\2\33\2\u0175\u017e\u0182\u0186\u018c\u0192\u0198")
        buf.write("\u019c\u01a4\u01ad\u01b2\u01b7\u01bf\u01ca\u01d5\u01dd")
        buf.write("\u01e1\u01e9\u01f6\u01fb\u01ff\u0206\u020c\u0212\b\39")
        buf.write("\2\b\2\2\3F\3\3G\4\3H\5\3I\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BODY = 1
    BREAK = 2
    CONT = 3
    DO = 4
    ELSE = 5
    ELSEIF = 6
    ENDBODY = 7
    ENDIF = 8
    ENDFOR = 9
    ENDWHILE = 10
    FOR = 11
    FUNC = 12
    IF = 13
    PARA = 14
    RETURN = 15
    THEN = 16
    VAR = 17
    WHILE = 18
    TRUE = 19
    FALSE = 20
    ENDDO = 21
    ASSIGN = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    LT = 28
    GT = 29
    LTE = 30
    GTE = 31
    EQU = 32
    NEQU = 33
    ADDFLOAT = 34
    SUBFLOAT = 35
    MULFLOAT = 36
    DIVFLOAT = 37
    LTF = 38
    GTF = 39
    LTEF = 40
    GTEF = 41
    NEQUF = 42
    AND = 43
    OR = 44
    NOT = 45
    LP = 46
    RP = 47
    LCB = 48
    RCB = 49
    LSB = 50
    RSB = 51
    SEMI = 52
    COLON = 53
    COMMA = 54
    DOT = 55
    STRING_LIT = 56
    FLOAT_LIT = 57
    INT_LIT = 58
    ID = 59
    CMT = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64
    UNTERMINATED_COMMENT = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'='", "'+'", "'-'", "'*'", 
            "'\\'", "'%'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
            "'+.'", "'-.'", "'*.'", "'\\.'", "'<.'", "'>.'", "'<=.'", "'>=.'", 
            "'=/='", "'&&'", "'||'", "'!'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BODY", "BREAK", "CONT", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNC", "IF", "PARA", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "LT", "GT", "LTE", 
            "GTE", "EQU", "NEQU", "ADDFLOAT", "SUBFLOAT", "MULFLOAT", "DIVFLOAT", 
            "LTF", "GTF", "LTEF", "GTEF", "NEQUF", "AND", "OR", "NOT", "LP", 
            "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COLON", "COMMA", 
            "DOT", "STRING_LIT", "FLOAT_LIT", "INT_LIT", "ID", "CMT", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "BODY", "BREAK", "CONT", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                  "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNC", "IF", "PARA", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "LT", "GT", 
                  "LTE", "GTE", "EQU", "NEQU", "ADDFLOAT", "SUBFLOAT", "MULFLOAT", 
                  "DIVFLOAT", "LTF", "GTF", "LTEF", "GTEF", "NEQUF", "AND", 
                  "OR", "NOT", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
                  "COLON", "COMMA", "DOT", "STRING_LIT", "FLOAT_LIT", "DECIMAL_PART", 
                  "INT_LIT", "INT_DEC", "INT_HEX", "INT_OCT", "EXPONENT", 
                  "DIGIT", "ID", "CMT_CHAR", "CMT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[55] = self.STRING_LIT_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    y = str(self.text)
                    error_sequence =['\r','\n']
                    if(y[-1] in error_sequence):
                        raise UncloseString(y[1:-1])
                    else:
                        raise UncloseString(y[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise ErrorToken(self.text)
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise UnterminatedComment()
                
     


