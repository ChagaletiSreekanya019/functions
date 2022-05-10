def fun():
    a=[[1,2],[3,4,5],[5,6,7,8,9],[7,7,8,5,5,6],[9,6,4,3],[4]]
    i=0
    ind=[]
    maxi=0
    while i<len(a[i]):
        b=(len(a[i]))
        if maxi<b:
            maxi=b
            ind=a[i]
        min=a[i]
        indi=a[i]
        if min>min:
            min=b
            indi=a[i]
        i=i+1
    print(maxi,ind)
    print(len(min),indi)
fun()
