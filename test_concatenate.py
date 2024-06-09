from Concatenate import concatenate_str, sum_numbers, devide_nums
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

def test3_sum_numbers():
    assert sum_numbers(1, "-1") == -1

def test1_devide_nums():
    assert devide_nums(10, 5) == 2

def test2_devide_nums():
    assert devide_nums(4, 5) == 0
 
def test3_devide_nums():
    assert devide_nums(10, 0) == -1

def test3_devide_nums():
    assert devide_nums(10, "0") == -1