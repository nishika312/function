from math import degrees
from re import I


# def sum(a,b,c):
#     count=0
#     count/sum
#     num=a+b+c
#     print(num)
# sum(2,6,6)

# def sum(a,b,c):
#     d=a+b+c
#     e=d//3
#     print(d)
#     print(e)
# sum(3,4,5)

def oddeven(i):
    num=int(input("enter number"))
    while i<=num:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i=i+1
oddeven(0)
