from Concatenate import concatenate_str, sum_numbers
import pytest

def test1_concatenate():
    assert concatenate_str("123", "456") == "123 456"

def test2_concatenate():
    assert concatenate_str("abc,", "cba") == "abc, cba"

def test1_sum_numbers():
    assert sum_numbers(1, 1) == 2

def test2_sum_numbers():
    assert sum_numbers(-1, -1) == -2

def test2_sum_numbers():
    assert sum_numbers("1", 1) == -1

def test2_sum_numbers():
    assert sum_numbers(1, "-1") == -1
