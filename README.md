Assume Rust, Cargo, uv, and maturin are installed.

Local dev flow:

1. First, `uv sync`
2. Next, `uv run  maturin develop --uv` (by default, this will build the package in debug mode. Pass `--release` to build in release mode.)

This will place the .so file in the src/test_proj/directory where it will be accessible as a Python module named `_polars_plugins`. Note: 
We won't need to access the _polars_plugins module directly in any imports, as Polars plugins just use the `register_plugin_function` function with the plugin path set to the directory of the .so file.

3. Then, `uv run scripts/test.py` to use the plugin.

4. Also, `uv run pytest` to run the python tests.

5. Run Rust unit tests using `cd rust && cargo test`