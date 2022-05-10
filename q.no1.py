# def say_hello(name):
#     print("hello",name)
#     print("how are you?")
# say_hello("Aatif")

# def add_numbers(number1,number2):
#     print("i will add two numbers")()
#     print(number1+number2)
# add_numbers(120,50)
# num_x="134"
# name="rinki"
# add_numbers(num_x,name)

# def say_hello_language(name,language):
#     if language=="hindi":
#         print("namzste",name)
#         print("Aap kaise ho?")
#     elif language=="punjabi":
#         print("sat sri akaal",name)
#         print("how are you")
# say_hello_language("rishabh","punjab")
# say_hello_language("armaan","english")
# say_hello_language("abishek","french")
# say_hello_language("kavay","hindi")


# def say_hello_people(name_x,name_y,name_z,name_a):
#     print("namaste",name_x)#in hindi
#     print("Alah hafiz",name_y)#in urdu
#     print("bonjour",name_z)#in english
#     print("hello",name_a)#in english
# say_hello_people("imitiyaz","rishabh","rohul","vidya")
# say_hello_people("steve","saswata","shakrundin","rajeev")

# def icecream(*flavours):
#   for flavour in flavours:
#     print("i love"+flavour)
# icecream("chocolate","butterscotch","vanilla","strawberry")

# def attendance(name,status="absent"):
#     print(name,"is",status,"today")
# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")

# def greet(*names):
#     for name in names:
#         print("welcome",name)
# greet("rinki","vishal","kartik","bijender")

# def menu(day):
#     if day=="monday":
#         return"butter chicken"
#     elif day=="tuesday":
#         return"mutton chaap"
#     else:
#         return"chole bhature"
#     print("will i be able to print")
# menu(monday)

# mon_menu=menu("monday")
# print(mon_menu)
# tues_menu=menu("tuesday")
# print(tues_menu)
# fri_menu=menu("friday")
# print(fri_menu)


# def fun(x=1,y=2):
#     x=x+1
#     y=y+1
#     print(x,y)
# fun(y=2,x=1)

# num=1
# def fun():
#     num=3
#     print(num)
# fun()
# print(num)

# 
# num=1
# def fun():
#     num=3
#     print(num)
# fun()
# print(num)

# num=1
# def fun():
#     global num
#     num=num+3
#     print(num)
# fun()
# print(num)

# def test(x=1,y=2):
#     x=x+y
#     y=y+1
#     print(x,y)
# test()

# def test(x=1,y=2):
#     x=x+1
#     y=y+1
#     print(x,y)
# test(2,1)

# def fun():
#     list=[56,78,94]
#     i=0
#     max=0
#     while i<len(list):
#         if list[i]>max:
#             max=list[i]
#         i=i+1
#     print(max)
# fun()

# def fun():
#     list=["abc","xyz","aba","1221"]
#     i=0
#     c=0
#     d=[]
#     while i<len(list):
#         if list[i]==len(list):
#             c=c+1
#             d.append(c)
#         i=i+1
#     print(d)
# fun()

# def fun():
#     a=[8,2,3,0,7]
#     i=0
#     sum=0
#     while i<len(a):
#         sum=sum+a[i]
#         i=i+1
#     print(sum)
# fun()

# def fun():
#     list=["1234abcd"]
#     i=-1
#     sum=0
#     while i<len(list):
#         sum=sum+list[i]
#         i=i+1
#     print(sum)
# fun()
        

# def fun():
#     a=[1,2,3,3,3,3,4,5]
#     i=0
#     b=[]
#     while i<len(a):
#         if a[i] not in b:
#             b.append(a[i])
#         i=i+1
#     print(b)
# fun()

# def fun():
#     a=[1,2,3,4,5,6,7,8,9]
#     i=0
#     while i<len(a):
#         if (a[i])%2==0:
#             print(a[i],end="")
#         i=i+1
# fun()

# def fun():
#     a=int(input("enter the weight"))
#     b=int(input("enter the height"))
#     bmi=a/b
#     if bmi<=18.5:
#         print("underweight")
#     elif 18.5<=bmi<=25.0:
#         print("normal")
#     elif 25.0<=bmi<=30.0:
#         print("over weight")
#     elif bmi>=30.0:
#         print("obese")
#     else:
#         print("none")
# fun()


# def fun():
#     a="the quick Brow Fox"
#     i=0
#     c=0
#     if a>="A" and a<="Z":
#         c=c+1
#         print(i)
#     elif a>="a" and a<="z":
#         i=i+1
#     print(i)
# fun()

# def fun():
#     i=1
#     c=[]
#     while i<=30:
#         if i<=5:
#             print(i**2)
#         if 25<=i>=30:
#             print(i**2)
#         i=i+1
# fun()



# def fun():
#     a=[2,-7,5,-64,-14]
#     i=0
#     count=0
#     count1=0
#     while(i<len(a)):
#         if(a[i]>0):
#             print(a[i],"positive number")
#             count=count+1
#         else:
#             print(a[i],"negitive number")
#         i=i+1
#     print(count,"count of positive number")
#     print(count,"count of negitive number")
# fun()

# def fun():
#     a=int(input("enter the number"))
#     if(a%3==0 and a%5==0):
#         print("fizzbuzz")
#     elif(a%5==0):
#         print("buzz")
#     elif(a%3==0):
#         print("fizz")
#     else:
#         print(a)
# fun()


# def fun():
#     i=0
#     while i<=10:
#         print(i,"*",5,"=",i*5)
#         i=i+1
# fun()

# def fun():
#     a=int(input("enter the age"))
#     if a<=13:
#         print("drink toddy")
#     elif a<=17:
#         print("drink coke")
#     elif a<=18:
#         print("drink beer")
#     elif a<=20:
#         print("drink thum")
#     elif a<=30:
#         print("drink whisky")
# fun()


# def fun():
#     a=[9,1,1,9]
#     i=0
#     s=""
#     while i<len(a):
#         s=s+str(a[i]**2)
#         i=i+1
#     print(s)
# fun()

# def fun():
#     a=[12,67,98,34]
#     i=0
#     s=[]
#     while i<len(a):
#         c=a[i]//10
#         d=a[i]%10
#         e=c+d
#         s.append(e)
#         i=i+1
#     print(s)
# fun()

# def fun():
#     string="1234abcd"
#     i=0
#     rev=0
#     sum=0
#     while i<len(string):
#         sum=sum+rev
#         rev=rev/string
#         i=i+1
#     print(rev)
# fun()

# def fun():
#     a=[[1,2],[3,4,5],[5,6,7,8,9],[7,7,8,5,5,6],[9,6,4,3],[4]]
#     i=0
#     ind=[]
#     maxi=0
#     while i<len(a):
#         b=(len(a[i]))
#         if maxi<b:
#             maxi=b
#             ind=a[i]
#         min=a[i]
#         indi=a[i]
#         if min>mmin:
#             min=b
#             indi=a[i]
#         i=i+1
#     print(maxi,ind)
#     print(len(min),indi)
# fun()


# i=1
# while i<=6:
#     k=1
#     while k<=6-i:
#         print(" ",end=" ")
#         k=k+1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     m=1
#     while m<i:
#         print(i-m,end=" ")
#         m=m+1
#     print()
#     i=i+1


# a=[10,14,2,23,19]
# i=0
# max1=0
# while i<len(a):
#     if a[i]>max1:
#         max1=a[i]
#     i=i+1
# max2=0
# i=0
# while a[i]>max2:
#     if a[i]!=max1:
#         max2=a[i]
#     i=i+1
# print(max1+max2)

# a=[4,6,2,1,9,63,-134,566]
# max=0
# i=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# min=a[0]
# i=0
# while i<len(a):
#     if a[i]<min:
#         min=a[i]
#     i=i+1
# print(max)
# print(min)


# def fun():
#     a=[7,1,4,23,1203,95,403,84]
#     i=0
#     while i<len(a):
#         if (a[i])%2==0:
#             print((a[i]),"even num")
#         else:
#             print((a[i]),"odd num")
#         i=i+1
# fun()

# def fun():
#     a=[3,4]
#     i=0
#     while i<len(a):
#         print(a[i]**a[i+1])
#         break
# fun()

# a=[1,2,3,2,3,2,4,3,5,6]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     n=[]
#     count=[]
#     if j<len(a):
#         if a[i]==a[j]:
#             count=count+1
#     j=j+1
#     n.append(count)
#     n.append(a[i])
#     if n not in c:
#         c.append(n)
#     i=i+1
# print(c)


i=1
while i<=100:
    j=1
    while j<=i:
        if i%j==0:
            print(i,"not")
        else:
            print(i,"prime")
        i=i+1







    













