# a=[2,-7,5,-64,-14]
# i=0
# count=0
# count1=0
# while(i<len(a)):
#     if(a[i]>0):
#         print(a[i],"positive number")
#         count=count+1
#     else:
#         print(a[i],"negitive number")
#         count1=count1+1
#     i=i+1
# print(count,"count of positive number")
# print(count1,"count of negitive number")

def fun():
    a=int(input("enter the number"))
    if a%2!=0 and a%1!=0 and a%3==0:
        print("prime")
    else:
        print(" error")  
fun()          

