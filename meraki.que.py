#  def say_hello(name):
# #     print("hello",name)
# #     print("how are you?")
# # say_hello("Aatif")

# def add_numbers(number1,number2):
#     print("i will add two numbers")
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
# 
# def menu(day):
#     if day=="monday":
#         return"butter chicken"
#     elif day=="tuesday":
#         return"mutton chaap"
#     else:
#         return"chole bhature"
#     print("will i be able to print")
# menu("day")

print("hello")
print("bye")
def fun():
    print("10")
    print("done")
print("5")
fun()
print("start")

# def fun():
#     num=int(input("enter"))
#     a=["a",1,"2",5,"b","q"]
#     i=1
#     while i<len(a):
#         print(a[i])
#         i=i+1
# fun()

# def sum_list(lis):
#     if len(lis)==1:
#         return lis[0]
#     return lis[0]+sum_list(lis[1:])
# print(sum_list[1,4,7,10])

def add(*a):
    sum=0
    for i in a:
        sum=sum+i
    return sum
print(add(1,2,3,4,5))

# def fun(**a):
#     for i in a.items():
#         print(i)
# fun(num=5,colour="blue",fruit="apple")

# def pattern(number):
#     if number==1:
#         return 10
#     elif number % 2==0:
#         return pattern(number-1)+1
#     else:
#         return pattern(number-1)*10
# print(pattern(3))

