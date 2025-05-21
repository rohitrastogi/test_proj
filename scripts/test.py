import polars as pl
import test_proj.polars_plugins.pig_latin # noqa: F401 — needed for plugin registration


df = pl.DataFrame(
    {
        "english": ["this", "is", "not", "pig", "latin"],
    }
)
result = df.with_columns(pig_latin=pl.col("english").pig_latin.do_pig_latin())
print(result)
print("yoooo")