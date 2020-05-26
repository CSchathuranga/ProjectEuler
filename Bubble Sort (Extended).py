#Sorting the array
    print("length of the array =",len(A))
    for x in range(0,len(A)-1):
        for y in range(0,len(A)-1-x):
            if A[y]>A[y+1]:
                temp=A[y]
                A[y]=A[y+1]
                A[y+1]=temp
    print("A =",A)
    print("Maximum Value =",A[len(A)-1])
    print("Minimum Value =",A[0])
    #find average
    tot=0.0
    for s in range(0,len(A)):
        tot=tot+A[s]
    avg=tot/len(A)
    print("Average Value =",avg)
    #find mean
    c=int((len(A)/2))
    if (len(A)%2==0):
        mean=(A[c-1]+A[c])/2
    else:
        mean=A[int((len(A)+1)/2)-1]
    print("Mean Value=",mean)
