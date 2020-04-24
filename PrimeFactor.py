number = int(input("Enter Number"))


def prime(num):
    count = 1
    for i in range(1, num):
        if num % i == 0:
            count += 1
        if count > 2:
            break

    if count == 2:
        return True
    return False


def factor(x):
    for i in range(1, x+1):
        if x % i == 0 and prime(i):
         print(i,end=" ")


factor(number)
