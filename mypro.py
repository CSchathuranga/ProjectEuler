for y in range(100,9,-1):
    if(y%2==1):
        l=0
    else:
        l=-1
    for x in range (y,0,-2):
        print(x,end=" ")
    for s in range(0,(100-y),2):
        print("* *",end="")
    print()
for y1 in range(9,0,-1):
    if(y1%2==1):
        l=0
    else:
        l=-1
    for x1 in range (y1,0,-2):
        print(x1,end=" ")
    for s in range(0,(100-y1),2):
        print("* *",end="")
    print()
