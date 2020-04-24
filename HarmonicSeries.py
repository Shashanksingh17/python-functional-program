number = int(input("Enter Number"))
sum = 0
temp = 1
while temp <= number:
    sum += 1 / temp
    temp += 1
print(sum)
