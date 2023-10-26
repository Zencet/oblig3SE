import pytest
from oblig_2_main import is_leap_year

# Define a fixture for non-leap years
@pytest.fixture(params=[2001, 2003, 2022])
def non_leap_years(request):
    return request.param

# Test function that uses the non_leap_years fixture to check if it's not a leap year
def test_non_leap_years(non_leap_years):
    result = is_leap_year(non_leap_years)
    assert result is False, f"Year {non_leap_years} should not be a leap year."
