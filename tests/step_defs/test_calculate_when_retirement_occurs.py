import pytest
from pytest_bdd import scenario, given, when, then
from retirementAgeCalculator import retirementAgeCalculator

@scenario('../features/calculate_when_retirement_occurs.feature', 'The program asks for year and birth month')
def test_when_retire():
    pass

@pytest.fixture
def cal():
    return retirementAgeCalculator()

@given("The calculator is open")
def cal_open():
    pass

@when("The user enters 1998 and the month 03 and hits enter")
def step_enter_params(cal):
    cal.birthYear = 1998
    cal.birthMonth = 3


@then("the program should display “This will be in March of 2065” on the second line of output")
def step_calculate(cal):
    cal.retirementCal()
    assert cal.totalMonths == 'March'
    assert cal.retirementYear == 2065