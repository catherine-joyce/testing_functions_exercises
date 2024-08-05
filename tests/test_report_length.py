from lib.report_length import *

def test_report_length_donkey():
    result = report_length("donkey")
    assert result == "This string was 6 characters long."

def test_report_length_random_character_string():
    result = report_length("&&!!@@!!@@£@@£@£!@£$%^&*()")
    assert result == "This string was 26 characters long."

def test_report_length_uppercase_donkey():
    result = report_length("DONKEY")
    assert result == "This string was 6 characters long."