#write a program that works out whether if a given year is a leap year.
#logic to determine a leap year : on every year that is evenly divisible by 4 except every year that is evenly divisible by 100 unless the year is also evenly divisible by 400.
year = int(input("Please enter the year you want to check: "))
if(year%4 == 0 and year%100 == 0 and year%400 == 0):
    print("This is a leap year")
elif(year%4 == 0 and year%100 == 0 and year%400 != 0):
    print("This is not a leap year")
elif(year%4 == 0):
    print("This is a leap year")
else:
    if year > 0:
        print("This is not a leap year")
    else:
        print("Please enter a valid value")