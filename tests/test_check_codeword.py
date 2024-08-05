from lib.check_codeword import *

def test_codeword_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."


def test_codeword_house():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_codeword_donkey():
    result = check_codeword("donkey")
    assert result == "WRONG!"