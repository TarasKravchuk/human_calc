import pytest
from main import calc, validator, space_killer

def test_calc_3_m46 ():
    assert calc([3, '*', -46]) == 'three multiplication minus forty-six equally minus one hundred and thirty-eight'

def test_calc_5_div_6 ():
    assert calc([6, '/', 5]) == 'six division five equally one point two'

def test_calc_999_pl_2 ():
    assert calc([999, '+', 2]) == 'nine hundred and ninety-nine plus two equally one thousand and one'

def test_calc_10_min_0 ():
    assert calc([10, '-', 0]) == 'ten minus zero equally ten'

def test_space_killer_work ():
    assert space_killer(['   -1', '-    ', '          2        3     ']) == (['-1', '-', '23'])

def test_validator_work ():
    assert validator(['999', '-', '9']) == [999, '-', 9]

def test_validator_work_1():
    assert validator(['0', 'foo', '1']) is None

def test_validator_work_2():
    assert validator(['1.1', '-', '1']) is None

def test_validator_work_3():
    assert validator(['0', '/', '0.1']) is None
