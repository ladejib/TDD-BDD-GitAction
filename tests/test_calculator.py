import pytest
from app.calculator import add

def test_add():
    assert add(2, 3) == 5  # This test should fail initially

