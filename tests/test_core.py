tests/test_core.py
import pytest
def test_some_function():
    from src.core import some_function
    assert some_function() == 'Hello, World!'