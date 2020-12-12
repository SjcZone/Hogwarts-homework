import pytest
from mycode.calculator import Calculator


class TestDemo:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
    def test_add(self, a, b, expected):
        assert self.cal.myadd(a, b) == expected

    @pytest.mark.parametrize("a,b,expected", [(1, 2, -1), (8, 3, 5), (10, 4, 6)])
    def test_minus(self, a, b, expected):
        assert self.cal.myminus(a, b) == expected

    @pytest.mark.parametrize("a,b,expected", [(1, 2, 0.5), (3, 3, 1), (8, 4, 2)])
    def test_divide(self, a, b, expected):
        assert self.cal.mydivide(a, b) == expected

    @pytest.mark.parametrize("a,b,expected", [(0, 2, 0), (2, 3, 6), (3, 4, 12)])
    def test_multiply(self, a, b, expected):
        assert self.cal.mymultiply(a, b) == expected
