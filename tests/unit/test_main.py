"""Unit tests for main module."""

import pytest
from src.main import hello_world


def test_hello_world():
    """Test hello_world function."""
    result = hello_world()
    assert result == "Hello, Maypo!"
    assert isinstance(result, str)
