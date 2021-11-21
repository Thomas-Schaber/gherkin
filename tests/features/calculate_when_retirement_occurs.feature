# Created by tommy at 11/21/2021
Feature: Calculates when retirement will occur
	As a user I would like to know when I will be ready to retire

  Scenario: The program asks for year and birth month
    Given The calculator is open
	When The user enters 1998 and the month 03 and hits enter
	Then the program should display “This will be in March of 2065” on the second line of output
