
a=[4,6,2,1,9,63,-134,566]
max=0
i=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
min=a[0]
i=0
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
print(max)
print(min)

