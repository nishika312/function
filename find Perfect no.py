def Perfect():
    i=1
    while i<=100:
        s=1
        sum=0
        while s<i:
            if i%s == 0:
                sum=sum+s
            s=s+1
        if sum==i:
            print(i,"perfect number")
        else:
            print(i,"not perfect")
        i+=1
Perfect()               
