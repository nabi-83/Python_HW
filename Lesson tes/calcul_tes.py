import numbers
import pytest

from calcul import Calcul

calcul = Calcul()

@pytest.mark.parametrize( "num1, num2, result", [
    (4,5,9),
    (-6, -10, -16),
    (-6, 6, 0),
    (5.61,  4.29, 9.9),
    (10, 0, 10),
    (-10.5, 1234, 1223.5)
])
def test_sum_nums(num1, num2, result):
    calcul = Calcul()
    res = calcul.sum(num1, num2)
    assert res == result


@pytest.mark.parametrize( "nums, result", [
    ([],0),
    ([1,2,3,4,5,6,7,8,9,5], 5)
] )
def test_avg_list(nums, result):
    calcul = Calcul()
    res = calcul.avg(nums)
    assert res == result

@pytest.mark.positive_test
def test_div_positive():
    calcul = Calcul()
    res = calcul.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calcul = Calcul()
    with pytest.raises(ArithmeticError):
        calcul.div(10, 0)


