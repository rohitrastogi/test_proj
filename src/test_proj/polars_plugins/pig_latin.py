import polars as pl
from polars._typing import IntoExpr
from polars.plugins import register_plugin_function
from pathlib import Path

PLUGIN_PATH = Path(__file__).parent.parent

@pl.api.register_expr_namespace("pig_latin")
class PigLatin:
    def __init__(self, expr: IntoExpr):
        self.expr = expr

    def do_pig_latin(self) -> pl.Expr:
        return register_plugin_function(
            args=[self.expr],
            plugin_path=PLUGIN_PATH,
            function_name="pig_latinnify",
            is_elementwise=True,
        )