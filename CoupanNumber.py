from random import random

size = int(input("Enter the Number of Unique Copons You Want: "))
listOfRandom = []
count = 0


# Balance the Range of Random number is being Generated
def pow():
    rangeofrandom = 10
    temp = size
    while temp != 0:
        rangeofrandom *= 10
        temp //= 10
    return rangeofrandom


while True:
    number = (random() * pow()) // 10
    count += 1
    if number not in listOfRandom:
        listOfRandom.append(number)
    if len(listOfRandom) == size:
        break
print("Total Number of Random Number Generated: ", count)
print(listOfRandom)
