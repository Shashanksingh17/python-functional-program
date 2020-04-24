year = int(input("Enter Year"))
if year < 1000 and year > 9999:
    print("Wrong Year")
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a Leap Year")
