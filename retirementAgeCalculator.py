import re

class retirementAgeCalculator():
    def __init__(self, totalYears=0, totalMonths=0, birthYear=0, birthMonth=0):
        self.totalYears = totalYears
        self.totalMonths = totalMonths
        self.birthYear = birthYear
        self.birthMonth = birthMonth
        self.retirementMonth = 0
        self.retirementYear = 0

    def set_total_years(self, totalYears):
        self.totalYears = totalYears

    def set_total_months(self, totalMonths):
        self.totalMonths = totalMonths

    def set_birth_year(self, birthYear):
        self.birthYear = birthYear

    def set_birth_month(self, birthMonth):
        self.birthMonth = birthMonth

    #convert month to calendar month
    def getMonthCalendarName(self, monthNumericalVal):
        if monthNumericalVal == 0:
            monthNumericalVal = 1
        monthList = {1: "January",
                     2: "February",
                     3: "March",
                     4: "April",
                     5: "May",
                     6: "June",
                     7: "July",
                     8: "August",
                     9: "September",
                     10: "October",
                     11: "November",
                     12: "December"}
        return monthList[monthNumericalVal]

    #convert total number of months to years
    def convertToYears(self, totalMonths):
        remainingMonths = totalMonths % 12
        totalYears = totalMonths // 12
        self.retirementMonth = remainingMonths
        print("Your full retirement age is", totalYears, "and", remainingMonths, "months")
        return totalYears, remainingMonths

    #find the retirement date by finding total months and converting to years
    def retirementDate(self, birthYear, birthMonth):
        self.totalMonths += birthMonth
        self.totalYears += self.totalMonths // 12
        self.totalMonths = self.totalMonths % 12

        self.retirementYear = birthYear + self.totalYears
        self.totalMonths = self.getMonthCalendarName(self.totalMonths)
        print("this will be in", self.totalMonths, "of", self.retirementYear, "\n")

    #find the total number of months to retirement then call retirementDate
    def retirementCal(self):
        birthYear = self.birthYear
        birthMonth = self.birthMonth
        retirementAge = 780 #base year 1937 converted to months

        if birthYear < 1900:
            print("Month or year invalid must be 1900 or later\n")
            return
        elif birthMonth > 12 or birthMonth < 1:
            print("Months are from labeled as number 1-12, 1 for January\n")
            return
        elif birthYear <= 1937:
            retirementAge = 780
        elif birthYear > 2021:
            return

        else:
            year = 1937
            while(year != birthYear):
                if year >= 1943 and year < 1954:
                    retirementAge += 0
                elif year >= 1960:
                    retirementAge += 0
                else:
                    retirementAge += 2

                year += 1
                #print(year)

        self.totalYears, self.totalMonths = self.convertToYears(retirementAge)

        self.retirementDate(birthYear, birthMonth)


    # def main():
    #     answer = ' '
    #     while answer != '':
    #         year = None
    #         month = None
    #
    #         print("Social Security Full Retirement Age Calculator")
    #         answer = input("Enter the year of birth or to exit: ")
    #         #must be 4 digit number
    #         if re.search("[0-9]{4}", answer) and len(answer) == 4:
    #             year = int(answer)
    #             month = int(input("Enter birth month: "))
    #             retirementCal(year, month)
    #         elif answer == '':
    #             break
    #         else:
    #             print("invalid input\n")
    #
    #
    # main()