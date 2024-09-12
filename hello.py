#age= input("enter your age:" )
#age=int(age)
#print(type(age))
 
#edu= input("enter your edu: ")
#edu=int(edu)
#print(type(edu))

#height= input("enter your heigh:" )
#height=int(height)
#print(type(height))

#if(age <= 18 and edu <=14 and height<=5):
    #print("you are pass")
#else:
    #print("you are fail")

#01 
#hs = "hello"
#print(" hello")
#hs="faizaazhar"
#02
#myname ="faizaazhar"
#name="faizaazhar"  
#name="faizaazhar" 
#nameFirst="faizaazhar"
#NameFirst="faizaazhar"
#name1st="faizaazhar"
#name-name="faizaazhar"
#03
#name="faiza"
#age=" 14"
#print ("hello my name " +name +age)
#04
#name1 = "faiza"
#name1 = "azhar"
#print("name1")
#05
#age1="26"
#age2=" 27"
#print(" age1,age2" "age1 +age2 ")
#06
#x =11
#if x==10:
    #print(" x is 10 ")
#else:
    #print(" x is not 10")
#07
 #a=10
 #a=10+10
 #08
#hp=10
#if hp!= 10:
 #   print(" healthy")
#else:
 #   print("unhealthy")
 #09
#num =input("enter your number" )
#num=int(num)
#if(num==90):
 #   print("you are pass" ,"Grade A")
 #10
#num = input("enter your name")
#num=int(num)
# print("you are pass" ,"Grade B")
#elif num>=70:
#    print("you are pass" ,"Grade C")
#else:
 #   print("you are fail" ,"GradeD")
#11
#mark= 100
#if( mark>=90 and mark<= 100):
 #   print( " excellent ! grade A")
#elif( mark>=80 and mark<90):
 #   print(" good! grade B")
#elif( mark>=70 and mark<80):
 #       print(" average ! grade c")
#else:
 #   print( "invalid garde")
 #12
#num1=90
#num2=100
#if( num1>10 or num2>10):
 #   print(" num1 is greater than")
 #13
# num1 =10
# num2 =11
# if( num1==10):
#   if( num2==11):
#     print(" both numbers are equal")
# else:
#     print(" num1 is equal yto 10")
# 14 list
# name=[89]
# name=name+["faiza"]
# name.append("azhar")
# 15
# names = [89]
# names.insert(10,"Raza")
# # names.insert( 10,34)
# print(type(names),names)
# 16
# names = ["faiza","azhar","raza"]
# names = [1,"faiza"]+names+["azhar"]
# print(type(names),names)
# 17
# ls1 = [1,2,3,4,5]
# ls2 = [6,7,8,9,10]
# ls1.extend(ls2)
# print(type(ls1),ls1)
# 18
# ls=["a",1,2,3,45]
# del ls[1]
# print(type(ls),ls)
# 19
# ls = ["a",1,2,3,45]
# ls.remove (2)
# print(type(ls),ls)
# 20
# ls= ["a",1,2,3,45]
# # # ls2=ls[4]
# # ls2=ls[4:5]
# ls2=ls[0:4:5]
# # ls2=ls[:3]
# print(ls2)
# 21
# ls= [1,2,33,55,0,9,8,7,6,5,4,3]
# ls.sort()
# print(ls)
# 22
# ls= [1,2,33,55,0,9,8,7,6,5,4,3]
# ls.sort(reverse=True)
# print(ls)
# 23
# ls= [1,2,3,4,5]
# # ls.pop(2)
# ls.pop(-1)
# print(ls)
# 24
# ls= [1,2,3,4,5]
# # le= len(ls)
# le =len(ls)-1
# print(le)
# 25 tuple
# tup = ("HELOO","world","faiza")
# print(tup)
# print(type(tup))
# 26
# tup1 = ("hello",)
# print(tup1)
# print(type(tup1))
# 27 constructure
# tup = (1,2,3,)
# # print(len(tup))
# print(tup[0])
# 28list and its methods
# tup=list((1,2,3))
# y= list(tup)
# # y.append(4)
# 28
# print(y)
# tup = tuple(y)
# # y.insert(0,"hello")
# # print(tup)
# # print(type(tup))
# 29
# tuple = (1,2,3,4,5,6,7,8,9,10)
# y= list(tuple)
# y.remove(2)
# print(y)
# print(type(tuple))
# tuple = (1,2,3,4,5,6,7,8,9,10)
# y=list(tuple)
# del y[2]
# print(y)
# print(type(tuple))
# 30 dictionary
# thisdict = {"name":"John Doe", "age":26, "city":"New York","list":["hello","world","!"]}
# thisdict["first name"] = "Ashutosh"
# print(thisdict["name"])
#31
# x= thisdict.get ("name")
# print(x)
# print (thisdict)
# 32
# thisdict.update ({"name":"Raza"})
# print(thisdict)
# x= thisdict.get ("name")
# print(x)
# print (thisdict.values())
# print (thisdict.keys())
# 32 nested
# thisdict.update ({" name":"Raza","age":26,"city":"New York","list":["hello","world","!"]})
# print(thisdict)
# prnt={
# "child1":
#      {
#      "name":"Raza",
#      "age":26,
#      },
# "child2":{
#             "name":"John Doe",
#             "age":25,
#             },
# "child3":{
#             "name":"Ravi",
#             "age":27,
#             }
#                 }
# # print(prnt)
# # print(prnt["child1"] [ "name"])
# prnt["child1"][ "name"]= "faiza"
# print(prnt)
#33 copy
# dic1 = {"name":"John Doe", "age":26, "city":"New York"}
# dic2 = dic1.copy()
# dic1["name"] = "Ashutosh"
# print(dic1)
# print(dic2)
# prnt2=prnt
# print(prnt)
# print(prnt2)
# prnt2 = prnt2.copy()
# dic1 = {"name":"John Doe", "age":26, "city":"New York"}
# dic2 = dic1.copy()
# dic1["name"] = "Ashutosh"
# print(dic1)
# print(dic2)
# 34 sets
# set1={ 1,2,3,4,5}
# set2={"hello","world","!"}
# set3={True,False,0,1}
# print(set1,type(set1))
#35 sets of constructure
# set1=set({ 1,2,3,4,5})
# print(set1,type(set1))
# 36 add or len or index
# set1 ={ 1,2,3,4,5}
# set1.add(6)
# print( len(set1))
# print(len(set1)-1)
# print(set1)
# 37 update of sets
# set1 ={ 1,2,3,4,5}
# set2 ={ "hello", "world","!",9}
# set1.update(set2)
# print( set1)
# 38 removeof set
# set1 ={ 1,2,3,4,5}
# set1.remove(2)
# print( set1)
# 39 discard of set
# set1 ={ 1,2,3,4,5}
# set1.discard(2)
# print( set1)
# 40 union of set two method
# set1={1,2,3,4,5}
# set2={5,6,7,8,9,10}
# # set3=set1|set2
# # set3=set1.union(set2)
# print( set3)
# 41 intersection of set two method
# set1={1,2,3,4,5}
# set2={5,6,7,8,9,10}
# #set3={10,11,12,13,14,15}
# # set4=set1.intersection(set2,set3)
# set4=set1&set2
# print(set4)

# 42 combined both methods 
# set1={1,2,3,4,5}
# set2={5,6,7,8,9,10}
# set3={11,12,13,14,15}
# set4=set1 & set2 | set3
# print(set4)

# 43 difference of set
# set1={1,2,3,4,5}
# set2={5,6,7,8,9,10}
# set3={11,12,13,14,15}
# # set4=set1.difference(set2)
# set4=set1 - set2
# print(set4)

# 44 In key word of set
# set1={1,2,3,4,5}
# # print(1 in set1)
# print(1 not in set1)

# 45 conditional ternary operator
# x=10
# print("pass") if x==10 else print("x is not 10")

# 46 for loop
# x=10
# for x in range(6):
#     print(x)
# 47 In list
# x=10
# li=[ 1,2,3,4,5]
# for x in li:
#     print(x)

# 48 while loop
# i=0
# while i<5:
#     print(i)
#     i=+1

# 49 break condition and pass statement

# for i in range(5):
#     print(i)
#     if i == 2:
#         break
# for i in range(5):
#     print(i)
#     if i == 2:
#         continue

# 50 nested loop condition
# ls1 = ["apple","banana","cherry"]
# ls2 = [5,6,7,8,9,10,11,12,13,14,15]
# for i in ls1:
#     for j in ls2:
#         print(i,j)
# 51 list comprehension
# ls1 = ["apple","banana","cherry"]
# ls2 = [5,6,7,8]
# ls3 = [ (i,j) for i in ls1 for j in ls2]
# print(ls3)
# # Assignment no 2  make a table of number which is given by the user upto 10.make this is python
# x=10
# number=2
# for x in range(1,11):
#     print(f"{number} x {x} = {number * x}")
# iteration and iterable
# ls=[1,2,3,4,5]
# ls2=iter(ls)
# print(next(ls2))
# print(next(ls2))
# print(next(ls2))
# print(next(ls2))
# print(next(ls2))
# function and vaiable scope
# 1.method
# def s():
#     print("hello")
# s()
# 2.
# def s():
#      return "hello world"
# print(s())  
# 3.
# def s():
#     return "world"
# p=s()
# print(p) 
# 4.
# def sum(p):
#     print("hello world",p)
# sum(89)
# 5.
# def sum(p,s):
#      print("hello world",p,s)
# sum(89,90)
# 6.
# def sum(p,s):
#      print("hello world",p+s)
# sum(89,90)
# 7.
# def sum(p,*s):
#      print("hello world",p,s)
# sum(89,90,91)
# 8.
# def sum(**q):
#      return q["name"]+" "+str(q["age"])
# print(sum(name="faiza",age=26))
# 52. variable scope local global
# s=12
# def f():
#     p=19
#     print(p,s)
# f()
# 53.lamdaa expression
# p=lambda x:x**2
# print(p(5))

# # assignment3 add tuple in start and end using string
# tup=list((1,2,3,4))
# y= list(tup)
# y.append("hello")
# print(y)
# tup=list((1,2,3,4))
# y=list(tup)
# y.insert(0,"world")
# print(y)
# tup=list((1,2,3,4))
# y=list(tup)
# y.insert(2,"world")
# print(y)
# 53. map and filter
# def s(n):
#      if n%2==0: 
#         return"even"
# number=[1,2,3,4,5,6,7,8,9,10,]
# even_number=list(map(s,number))
# print(even_number)
# 2.
# def s(n):
#     if n%2==0:
#         return"even"
# number=[1,2,3,4,5,6,7,8 ,9,10,]
# even_number=list(filter(s,number))
# print(even_number)

# 54.inner and nested function
# def s():
#     def p():
#         print("hello")
#     p()
# s()
# 55.file habdling/excception handling
# x=10
# try:
#     print(x)
# except:
#         print("error occurred")
# else:
#         print(" no error occurred")
# finally:
#         print("this is the end")
# 1. 
# f=open("example.txt", "w")
# f.write("hello world")
# f.write("hello world!,2")
# 2.
# f=open("example.txt", "a")
# f.write("hello world!,\n")
# # 3.
# import os
# os.remove("example.txt")
# f=open("example.txt", "a")
# f.write("hello world!,\n")
# print(f.readline(5))
# f.close()
# 4.
# import os 
# os.remove("example.txt")

# 56.class and object
# class person:
#      x =10**2
# p =person()
# print("p.x")
#2.
# class person:
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age
# def show(self):
#      print(f"name: {self.name}, age: {self.age}")
# p=person("faiza",21)
# print(p.name,p.age)
# p1=person("huma",21)
# print(p1.name,p1.age)
# 4. Assignment
# side_lenght=10
# side_lenght =float (input("enter the number of square"))
# area =side_lenght**2
# print("f the area of the side_lenght,{side_lenght} is{area}") 
# assignment 6
# Function to perform calculation
# def calculator():
#     try:
#         # Taking input from the user
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         operation = input("Choose the operation (+, -, *, /): ")

#         # Performing the desired operation
#         if operation == '+':
#             result = num1 + num2
#             print(f"Result: {num1} + {num2} = {result}")
#         elif operation == '-':
#             result = num1 - num2
#             print(f"Result: {num1} - {num2} = {result}")
#         elif operation == '*':
#             result = num1 * num2
#             print(f"Result: {num1} * {num2} = {result}")
#         elif operation == '/':
#             if num2 != 0:
#                 result = num1 / num2
#                 print(f"Result: {num1} / {num2} = {result}")
#             else:
#                 print("Error: Division by zero is not allowed!")
#         else:
#             print("Invalid operation. Please choose +, -, *, or /.")
#     except ValueError:
#         print("Error: Please enter a valid number.")

# # Call the calculator function
# calculator()







 





















