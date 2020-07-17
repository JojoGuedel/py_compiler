from Compiler.Binding.Binder import Binder
from Compiler.EvaluationResult import EvaluationResult
from Compiler.Evaluator import Evaluator
from Compiler.Syntax.SyntaxTree import SyntaxTree


class Compilation:
    def __init__(self, syntax_tree: SyntaxTree = None):
        self._syntax_tree = syntax_tree

    def set_syntax_tree(self, syntax_tree: SyntaxTree):
        self._syntax_tree = syntax_tree

    def evaluate(self):
        binder = Binder()
        binder.set_syntax_tree(self._syntax_tree)
        self._syntax_tree.print()
        bound_expression = binder.bind()

        diagnostics = self._syntax_tree.get_diagnostics()
        if len(diagnostics.get_diagnostic()) != 0:
            return EvaluationResult(diagnostics, None)

        evaluator = Evaluator(bound_expression)
        value = evaluator.evaluate()

        return EvaluationResult(diagnostics, value)
