import random
toss = int(input("How Many Times You Want To toss"))
count=0
head=0
tails=0

value=random.random()
while count<toss:
    if value>0.5:
     head=head+1
     print("head")
    else:
     tails=tails+1
     print("tails")
    count=count+1
    value=random.random()
print(int(head / toss*100))
print(int(tails / toss*100))



