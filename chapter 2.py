# string

first_name="Amit"
last_name="Singh"
a=first_name+" "+last_name
# print(a)
# print(first_name+str(3))
# print(first_name*3)
# how to take input by user
# using input function we are take the input

# name=input("type your name")
# print("hello "+name)
# age=input("Enter your age")
# print("your age is "+age)

# int function

# a=int(input("enter a value of a "))
# b=int(input("enter a value of b "))
# c=a+b
# print("c is "+str(c))

# a=str(4)
# b=int("44")
# c=float("33")
# print(b+c)#float

#more about variable
# name,age="Amit","19"
# print("hello "+name+" your age is "+age)
# x=y=z=9
# print(x)
# print(y)
# print(z) 

# two variable in one time
# name,age=input("enter your name and age ").split(" ")
# print(name)
# print(age)

#string formating
name="Amit"
age=20
# print("hello {} your age is {}".format(name,age))#pytho 3

# python 3.6 in string formatting

# print(f"hello {name} your age is {age +2}") 

# find the average 

# a=input("enter first number :")
# b=input("enter second number :")
# c=input("enter third number :")
# a, b, c=input("enter three number :").split(",")
# sum=(int (a)+ int (b)+ int (c))/3
# print(f"average of three numbers :{sum}")

# string indexing
# a="python"
# print(a[4])
# print(a[-1])



# string slicing
# lang="python"
# print(lang[0:2])
# print(lang[2:4])
# print(lang[2:])
# print(lang[:3])
# print(lang[:-3])

# step argument
# print("amit"[2:3])
# print("Amit"[0:5:3])
# print("Amit"[::3])
# print("Amit"[-1::-1])

# n=input("Enter your name ")
# print(n[::-1])

# string method

# a="Amit"
# print(len(a))

# lower method in small latter
a="AMit"
# print(a.lower())
# capital latter
# print(a.upper())
# starting latter capital and other are small in title method
# print(a.title())
# in count method count the latter how much time 
# print(a.count("A"))

# exercise
# name,char=input("Enter name and character").split(",")
# print(f"length of your name is {len(name)}")
# print(f"character count:{name.count(char)}")


# strip method
# a="     am   it    "
# b="....................."
# lstrip() remove left side spaces
# print(a.lstrip()+b)
# rstrip()remove right side spaces 
# print(a.rstrip()+b)
# use strip()remove bothe left and right spaces
# print(a.strip()+b)
# use replace()method remove all spcace in string
# print(a.replace(" ","")) 

# replace method 
# a="I am a student"
# b=a.replace(" ","_")
# print(b)

# find method use find the position of any char string
# print(a.find("I"))

# a="amit"
# b=a.center(8,"*")
# print(b)
# print(len(b))

# a="string"
# print(a[1])

# more operator

name="harsh"
name=name+"it"
print(name)
age=90
age=age-80
print(age)