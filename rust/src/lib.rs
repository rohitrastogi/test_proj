pub mod expressions;

use pyo3::prelude::*;

#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// Python module implemented in Rust
#[pymodule]
fn _polars_plugins(_py: Python<'_>, _m: &Bound<'_, PyModule>) -> PyResult<()> {
    _m.add_function(wrap_pyfunction!(sum_as_string, _m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_simple_addition() {
        assert_eq!(1 + 1, 2);
    }
}