pub mod expressions;

use pyo3::prelude::*;

/// Python module implemented in Rust
#[pymodule]
fn _polars_plugins(_py: Python<'_>, _m: &Bound<'_, PyModule>) -> PyResult<()> {
    Ok(())
}