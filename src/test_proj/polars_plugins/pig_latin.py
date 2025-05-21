import polars as pl
from polars._typing import IntoExpr
from polars.plugins import register_plugin_function
from pathlib import Path

PLUGIN_PATH = Path(__file__).parent.parent

def pig_latinnify(expr: IntoExpr) -> pl.Expr:
    return register_plugin_function(
        args=[expr],
        plugin_path=PLUGIN_PATH,
        function_name="pig_latinnify",
        is_elementwise=True,
    )