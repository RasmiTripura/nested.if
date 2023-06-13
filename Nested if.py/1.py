year=int(input("Enter a year="))
if year%4==0:
    if year%100!=0 and year%400==0:
        print("Year is leap year")
    else:
        print("Year is not a leap year")
else:
    print("None")