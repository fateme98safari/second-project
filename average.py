import math
avg=0
n=0
sum=0
while 1==1:
    print("enter score: ")
    score=float(input())
    n=n+1
    sum=sum+score
    str=input("to exit write exit: ")
    if str=="exit":
        avg=sum/n
        print("average is: ", avg)
        break
    else:
        continue


