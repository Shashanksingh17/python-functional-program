number = int(input("Enter Number"))
temp = 1;
if number >=0 and number<=31:
 while temp <= number:
    print(pow(2,temp))
    temp+=1
else:
   print("Wrong Number") 