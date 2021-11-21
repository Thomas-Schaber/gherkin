from retirementAgeCalculator import retirementAgeCalculator
import re

def main():
    cal = retirementAgeCalculator(0,0,0,0)
    answer = ' '
    while answer != '':
        year = None
        month = None

        print("Social Security Full Retirement Age Calculator")
        answer = input("Enter the year of birth or to exit: ")
        # must be 4 digit number
        if re.search("[0-9]{4}", answer) and len(answer) == 4:
            year = int(answer)
            month = int(input("Enter birth month: "))
            cal.retirementCal(year, month)
        elif answer == '':
            break
        else:
            print("invalid input\n")


main()