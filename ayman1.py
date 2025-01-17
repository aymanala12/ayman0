x=0
print("  #")
for x in range(4):
    if x==0 or x==1:
        for i in range(5):
            print("#",end=(""))

    print("",end=(" "))
    if x==2:
        for y in range(3):
            print("#",end=(""))
    print("")
    if x==3:
        print("  #")

    x=x+1

