import sys
import os

# Ensure the app directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from behave import given, when, then
from app.calculator import add

@given("I have a calculator API")
def step_given_calculator(context):
    pass  # No setup needed

@when("I add {a:d} and {b:d}")
def step_when_add(context, a, b):
    context.result = add(a, b)

@then("the result should be {expected:d}")
def step_then_result(context, expected):
    assert context.result == expected

