startYear = 1901
endYear = 2000
yearDays = 365
monthDays = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
dayIndex = 1
numOfFirstSundays = 0
print(sum(monthDays))

for year in range(startYear, endYear + 1):
    thisMonthDays = [m for m in monthDays] 
    if(year % 4 == 0):
        for month in range(2, 12):
            thisMonthDays[month] += 1 
        thisYearDays = yearDays + 1
    else:
        thisYearDays = yearDays 
    print("*-*-*")
    print(str(thisMonthDays))
    numOfThisYearSundays = 0
    for day in range(1, thisYearDays + 1):
        if(dayIndex == 6):
            if(day in thisMonthDays):
                print(day)
                numOfThisYearSundays += 1
            dayIndex = 0
        else:
            dayIndex += 1
    numOfFirstSundays += numOfThisYearSundays
    print("---")
    print("Year " + str(year) + " had " + str(numOfThisYearSundays) + " first Sundays")
print("---------------")
print(str(numOfFirstSundays) + " sundays")

    







