from lib.greet import *

def test_greet_Catherine():
    result = greet("Catherine")
    assert result == "Hello, Catherine!"