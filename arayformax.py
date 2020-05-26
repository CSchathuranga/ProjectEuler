list=[0,0,0,0,0]
#Data input to the array
for x in range(0,5):
    list[x]=int(input("Enter No "))
print(list)
#find the maximum value
max=list[0]
for y in range(0,4):

 if max<list[y+1]:
    max=list[y+1]
#display max
print(max)
                     
