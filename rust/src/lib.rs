pub mod expressions;

use pyo3::prelude::*;

/// Python module implemented in Rust
#[pymodule]
fn _polars_plugins(_py: Python<'_>, _m: &Bound<'_, PyModule>) -> PyResult<()> {
    Ok(())
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_simple_addition() {
        assert_eq!(1 + 1, 2);
    }
}