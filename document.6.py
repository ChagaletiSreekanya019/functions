# def fun():
# #     a=[1,2,3,4,5,6,7,8,9]
# #     i=0
# #     while i<len(a):
# #         if (a[i])%2==0:
# #             print(a[i],end="")
# #         i=i+1
# # fun()


# print( in [[1],2,3])
# l=[[p,q] for p in (0,4) for q in (0,4)]
# print(l)

# a=[0,0,4,5,0,1,3,2]
# a.sort()
# print((a))
# i=0
# b=[]
# while i<len(a):
#     if a[i]==0:
#        a.remove(a[i])
#     i+=1
# a=[1,2,3,4]
# string="emp"
# i=0
# b=[]
# while i<len(a):
#     e=string+str(a[i])
#     b.append(e)
#     i=i+1
# print(b)

# a=["p","q"]
# n=1
# i=0
# b=[]
# while i<len(a):
#     e=a[i]*n
#     b.append(e) 
#     n=n+1


# a=[1,2,3,4]
# # string="emp"
# # i=0
# # b=[]
# # while i<len(a):
# #     e=string+str(a[i])
# #     b.append(e)
# #     i=i+1
# # print(b)
# i=i+1
# print(b)


a=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
b=[]
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a[i]):
        if a[i] not in b:
            b.append(a[i])
            c=c+1
        j=j+1
        if c<=1:
            print(b)
    i=i+1
print(b)