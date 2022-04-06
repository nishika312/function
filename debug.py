# def calculate(a,b):
#     sum = a+b
#     print(sum)
# calculate(4,5)

# def multi(a,b):
#     multi=a*b
#     return multi
# print(multi(3,4))

# def ishu(number1,number2,number3):
#     sum=number1+number2+number3/3
#     print(sum)
# ishu(1,3,2)

# def voter(age):
#     if age>18:
#         print("eligible")
#     else:
#         print("not eligible")
# voter(20)

def distance(kms):
    if kms < 20:
        print("close")
    elif kms < 50:
        print("median")
    else:
        print("far")
distance(20)