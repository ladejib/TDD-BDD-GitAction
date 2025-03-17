import sys
import os

# Ensure the app directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))



import pytest
from app.calculator import add

def test_add():
    assert add(2, 3) == 5  # This test should fail initially

