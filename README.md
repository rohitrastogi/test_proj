Assume Rust, Cargo, uv are installed.

Local dev flow:

1. First, `uv sync --dev`. The --dev flag will install dependencies from the dev dependency group (maturin, pytest)

2. Next, `uv run maturin develop --uv` (by default, this will build the package in debug mode. Pass `--release` to build in release mode.)
This compiles the Rust code, creates a whl, and immediately installs the whl in the current environment. This is an editable install, useful for running tests.
Here, we are using uv to invoke maturin (as we installed maturin through uv). We also use the --uv flag, so uv (and not vanilla pip) are used to resolve the dependencies in the pyproject.toml.
If we don't use the --uv flag, maturin will use pip to resolve dependencies, which is far slower than uv for complex dependencies.

This will place the .so file in the src/test_proj/ directory where it will be accessible as a Python module named `_polars_plugins` (see the [tool.maturin] section in the pyproject.toml). Note: 
We won't need to access the _polars_plugins module directly in any imports, as Polars plugins just use the `register_plugin_function` function with the plugin path set to the directory of the .so file.

3. Then, `uv run scripts/test.py` to use the plugin.

4. Also, `uv run pytest` to run the python tests.

5. Run Rust unit tests using `cd rust && cargo test`

6. If you make changes to the Rust code, you can recompile the Rust code by running `uv run maturin develop --uv` again.