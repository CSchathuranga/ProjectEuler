x=1
a=1
b=2
y=0
tot=0
while(x<31):
    y=a+b
    print(y)
    if(x%2==0):
        tot=tot+y
    a=b
    b=y
    x=x+1
print(x)
tot=tot+2
print(tot)
    
