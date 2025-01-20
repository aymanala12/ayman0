x = [2.5,4.7,"ayman",6,3,"ali",5,3,"jjj",7]
z=0
for u in x:
    if isinstance(u,int):
        z=z+u
    elif isinstance(u,float):
        z=z+u
    else:
        print("this is not a number :   ",end="")
        print(u)
print(z)