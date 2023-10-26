import pytest
from oblig_2_main import is_leap_year

# Define a list of leap years to be tested
leap_years_to_test = [2000, 2004, 2028]

# Parametrize the test function to run for each year in the list
@pytest.mark.parametrize("year", leap_years_to_test)
def test_leap_years(year):
    result = is_leap_year(year)
    assert result is True, f"Year {year} should be a leap year."

# Entry point of the script: if this script is run directly, execute the tests using pytest
if __name__ == "__main__":
    pytest.main()
