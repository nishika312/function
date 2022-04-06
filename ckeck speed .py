def speed(w):
    if w<70:
        print("70")
    if w>=70:
        print("give 1 point per 5km")
    else:
        print("License suspended")
speed(int(input("enter the speed")))

