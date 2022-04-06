# def oddeven():
#     a=int(input("enter to ckeck no"))
#     if a%2==0:
#      print("even")
#     else:
#             print("odd")
# oddeven()

def oddeven(i):
    num=int(input("enter number"))
    while i<=num:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i=i+1
oddeven(0)


