import polars as pl
import test_proj.polars_plugins.pig_latin # noqa: F401 — needed for plugin registration

def test_piglatin():
    df = pl.DataFrame({
        "a": [1, 2, 3],
        "b": ["foo", "bar", "baz"],
    })
    result = df.select(pl.col("b").pig_latin.do_pig_latin())
    assert result.to_series().to_list() == ["oofay", "arbay", "azbay"]
