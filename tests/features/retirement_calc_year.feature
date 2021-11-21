# Created by tommy at 11/21/2021
Feature: Retirement calculator using year
  As a user I would like to be able to enter the year I was born to calculate my retirement age

  Scenario Outline: Calculate retirement age using valid years
    Given That user is asked for year of birth and enters a valid month <month>
    When The user types <year> and presses enter
    Then The program should calculate the retirement age of <retirementAge> years and <retirementM> months

    Examples: Times
    | month | year | retirementAge |  retirementM |
    | 1     | 1800 | 0             | 0            |
    | 1     | 1900 | 65            | 0            |
    | 2     | 1938 | 65            | 2            |
    | 3     | 1939 | 65            | 4            |
    | 4     | 1940 | 65            | 6            |
    | 5     | 1941 | 66            | 8            |
    | 6     | 1942 | 66            | 10           |
    | 7     | 1950 | 66            | 0            |
    | 8     | 1955 | 66            | 2            |
    | 9     | 1956 | 67            | 4            |
    | 10    | 1957 | 67            | 6            |
    | 11    | 1958 | 67            | 8            |
    | 12    | 1959 | 67            | 10           |
    | 13    | 1900 | 0             | 0            |
    | 4     | 2022 | 0             | 0            |

#  Scenario: Calculate retirement age using valid years
#    Given That user is asked for year of birth and enters a valid month "03"
#    When The user types "1900" and presses enter
#    Then The program should calculate the retirement age of 65 years and 0 months
