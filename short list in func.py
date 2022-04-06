# do not want repitid value
def ishu():
    num=[1,2,3,3,3,3,4,5,6,5]
    i=0
    k=[]
    while i<len(num):
        if num[i] not in k:
            k.append(num[i])
        else:
            pass
        i=i+1
    print(k)
ishu()


