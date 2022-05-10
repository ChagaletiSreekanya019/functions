# ist=[12,34,96]
#     i=0
#     max=0
#     while i<len(list):
#         if list[i]>max:
#             max=list[i]
#         i=i+1
#     print(max)
# fun()

# a=[1,2,[1,2,3],[4,5,6,7],[8,9]]
# i=0
# min=0
# ind=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         b=len(a[i])
#         while j<len(a[i]):
#             if min>min:
#                 min=b
#                 ind=a[i]
#             j=j+1
#     i=i+1
# print(min,ind)

i=1
while i<=3:
    j=1
    while j<=i:
        print("=",end="")
        j=j+1
    print()
    i=i+1
i=2
while i>=1:
    j=1
    while j<=i:
        print("=",end="")
        j=j+1
    print()
    i=i-1


