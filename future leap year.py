from datetime import date

year = int(input('Enter a year: '))
current_Year = date.today().year
print("Future leap year from current year: ",current_Year)
print("You entered -- year->",year)
for x in range(current_Year,year+1):
    if((x % 4 == 0)and(x % 100 != 0)) or(x % 400 == 0):
        print(x)