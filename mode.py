#not completed
A=[1,1,1,2,2]
a={}
for x in range(0,len(A)-1):
    M=0
    for y in range(0,len(A)-1):
        if A[x]==A[y]:
         M=M+1
    a[M]=x
print(a)
