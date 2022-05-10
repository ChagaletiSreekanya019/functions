def fun():
    list=[12,34,96]
    i=0
    max=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    print(max)
fun()

