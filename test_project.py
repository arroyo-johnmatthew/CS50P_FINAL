import pytest
from project import(
    calculate_withholding_tax, 
    get_taxable_income, 
    get_overall_deductions,
    sss_deduction,
    philhealth_deduction,
    pagibig_deduction)

def test_get_taxable_income():
    assert get_taxable_income(18000.00, 900.00, 450.00, 200.00) == pytest.approx(16450.00)
    assert get_taxable_income(30000.00, 1500.00, 750.00, 200.00) == pytest.approx(27550.00)
    assert get_taxable_income(50000.00, 1750.00, 1250.00, 200.00) == pytest.approx(46800.00)
    assert get_taxable_income(100000.00, 1750.00, 2500.00, 200.00) == pytest.approx(95550.00)
    assert get_taxable_income(120000.00, 1750.00, 2500.00, 200.00) == pytest.approx(115550.00)

def test_get_overall_deductions():
    assert get_overall_deductions(250.00, 250.00, 160.00, 0.00) == pytest.approx(660.00)
    assert get_overall_deductions(900.00, 450.00, 200.00, 0.00) == pytest.approx(1550.00)
    assert get_overall_deductions(1500.00, 750.00, 200.00, 1007.55) == pytest.approx(3457.55)
    assert get_overall_deductions(1750.00, 1250.00, 200.00, 4568.40) == pytest.approx(7768.40)
    assert get_overall_deductions(1750.00, 2500.00, 200.00, 15762.55) == pytest.approx(20212.55)
    assert get_overall_deductions(1750.00, 2500.00, 200.00, 20762.55) == pytest.approx(25212.55)

def test_sss_deduction():
    assert sss_deduction(4000.00) == pytest.approx(250.00)
    assert sss_deduction(5000.00) == pytest.approx(250.00)
    assert sss_deduction(18000.00) == pytest.approx(900.00)
    assert sss_deduction(35000.00) == pytest.approx(1750.00)
    assert sss_deduction(50000.00) == pytest.approx(1750.00)

def test_philhealth_deduction():
    assert philhealth_deduction(8000.00) == pytest.approx(250.00)
    assert philhealth_deduction(10000.00) == pytest.approx(250.00)
    assert philhealth_deduction(50000.00) == pytest.approx(1250.00)
    assert philhealth_deduction(100000.00) == pytest.approx(2500.00)
    assert philhealth_deduction(120000.00) == pytest.approx(2500.00)

def test_pagibig_deduction():
    assert pagibig_deduction(1000.00) == pytest.approx(10.00)
    assert pagibig_deduction(1500.00) == pytest.approx(15.00)
    assert pagibig_deduction(8000.00) == pytest.approx(160.00)
    assert pagibig_deduction(10000.00) == pytest.approx(200.00)
    assert pagibig_deduction(50000.00) == pytest.approx(200.00)

def test_calculate_withholding_tax():
    assert calculate_withholding_tax(50000.00) == pytest.approx(5208.40, abs=0.01)
    assert calculate_withholding_tax(800000.00) == pytest.approx(230208.35, abs=0.01)
    assert calculate_withholding_tax(18000.00) == pytest.approx(0.00, abs=0.01)
    assert calculate_withholding_tax(100000.00) == pytest.approx(16875.05, abs=0.01)
    assert calculate_withholding_tax(200000.00) == pytest.approx(43541.70, abs=0.01)