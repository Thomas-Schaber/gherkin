from pytest_bdd import scenario, parsers, given, when, then
from retirementAgeCalculator import retirementAgeCalculator
import pytest


@scenario('../features/retirement_calc_year.feature', 'Calculate retirement age using valid years', )
def test_cal():
    pass


@pytest.fixture()
def cal():
    return retirementAgeCalculator()


@given(parsers.cfparse("That user is asked for year of birth and enters a valid month {month:d}"))
def step_month(cal, month):
    cal.set_birth_month(birthMonth=month)


@when(parsers.cfparse("The user types {year:d} and presses enter"))
def step_year(cal, year):
    cal.set_birth_year(year)

@then(parsers.cfparse("The program should calculate the retirement age of {retirementAge:d} years and {retirementM:d} months"))
def step_calculate(cal, retirementAge, retirementM):
    #print(cal.birthMonth)
    cal.retirementCal()
    assert cal.totalYears == retirementAge
    assert cal.retirementMonth == retirementM




