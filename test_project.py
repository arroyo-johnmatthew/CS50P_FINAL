import pytest
from project import calculate_withholding_tax

def test_calculate_withholding_tax():
    assert calculate_withholding_tax(50000.00) == pytest.approx(5208.40, abs=0.01)
    assert calculate_withholding_tax(800000.00) == pytest.approx(230208.35, abs=0.01)
    assert calculate_withholding_tax(18000.00) == pytest.approx(0.00, abs=0.01)
    assert calculate_withholding_tax(100000.00) == pytest.approx(16875.05, abs=0.01)
    assert calculate_withholding_tax(200000.00) == pytest.approx(43541.70, abs=0.01)