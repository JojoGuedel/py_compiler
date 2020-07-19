import traceback

from Compiler.Syntax.Lexer import Lexer
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxTree import SyntaxTree


class LexerTests:
    def __init__(self):
        self._test_count = 0
        self._failed_test_count = 0

    def get_test_count(self):
        return self._test_count

    def get_failed_test_count(self):
        return self._failed_test_count

    def get_succeeded_test_count(self):
        return self._test_count - self._failed_test_count

    def lexer_lex_token(self, value, kind):
        kind_value_list = list(kind_value_list)
        token_count = len(kind_value_list)
        for i in kind_value_list:
            text = ""
            for j in range(token_count):
                text += kind_value_list[j][0][1]
            tokens = list(SyntaxTree.label_token(text))

            try:
                self._test_count += 1
                assert (len(tokens) == token_count), f"({text}) Wrong amount of tokens: {tokens}"
            except:
                self._failed_test_count += 1
                traceback.print_exc()

            for j in range(len(tokens)):
                try:
                    self._test_count += 1
                    assert (kind_value_list[j][0][0] == tokens[j].get_kind()), f"({text}) Unexpected token kind <{SyntaxKind.str(tokens[j].get_kind())}>, expected <{SyntaxKind.str(kind_value_list[j][0])}>"
                except:
                    self._failed_test_count += 1
                    traceback.print_exc()

    def test_token_kind(self):
        for i in self._get_token_test_expamples():
            yield [i]

    def test_token_kind_pairs(self):
        for i in self._get_token_test_expamples():
            for j in self._get_token_test_expamples():
                yield [i, j]

    @staticmethod
    def _get_token_test_expamples():
        return [(SyntaxKind.white_space_token, " "),
                (SyntaxKind.white_space_token, "  "),
                (SyntaxKind.white_space_token, "\r"),
                (SyntaxKind.white_space_token, "\n"),
                (SyntaxKind.white_space_token, "\r\n"),
                (SyntaxKind.int_token, "1"),
                (SyntaxKind.int_token, "123"),
                (SyntaxKind.float_token, "1.1"),
                (SyntaxKind.float_token, "123.123"),
                (SyntaxKind.string_token, "\"a\""),
                (SyntaxKind.string_token, "\"abc\""),
                (SyntaxKind.identifier_token, "a"),
                (SyntaxKind.identifier_token, "abc"),

                (SyntaxKind.char_token, "'a'"),
                (SyntaxKind.plus_token, "+"),
                (SyntaxKind.minus_token, "-"),
                (SyntaxKind.star_token, "*"),
                (SyntaxKind.slash_token, "/"),
                (SyntaxKind.double_star_token, "**"),
                (SyntaxKind.double_slash_token, "//"),
                (SyntaxKind.open_parenthesis_token, "("),
                (SyntaxKind.close_parenthesis_token, ")"),
                (SyntaxKind.bang_token, "!"),
                (SyntaxKind.double_ampersand_token, "&&"),
                (SyntaxKind.double_pipe_token, "||"),
                (SyntaxKind.double_equals_token, "=="),
                (SyntaxKind.not_equals_token, "!="),
                (SyntaxKind.less_or_equals_token, "<="),
                (SyntaxKind.greater_or_equals_token, ">="),
                (SyntaxKind.plus_equals_token, "+="),
                (SyntaxKind.minus_equals_token, "-="),
                (SyntaxKind.star_equals_token, "*="),
                (SyntaxKind.slash_equals_token, "/="),
                (SyntaxKind.less_than_token, "<"),
                (SyntaxKind.greater_than_token, ">"),
                (SyntaxKind.equals_token, "="),
                (SyntaxKind.true_keyword, "true"),
                (SyntaxKind.false_keyword, "false"),]

