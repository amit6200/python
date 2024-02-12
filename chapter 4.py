# function

# def add_two(a,b):
#     return a+b
# total=add_two(5,4)
# print(total)

# add two number using function


# def add_two(a,b):
#     return a+b
# a=int(input("Enter first number "))
# b=int(input("Enter second number "))
# total=add_two(a,b)
# print(total)

# sum of string using function


# def add_two(a,b):
#     return a+b
# a=input("Enter first name ")
# b=input("Enter second name ")
# total=add_two(a,b)
# print(total)

# return vs print

# return

# def add_three(a,b,c):
#     return a+b+c
# total=add_three(5,5,5)
# print(total)

# print

# def add_three(a,b,c):
#     print(a+b+c)
    
# add_three(5,3,2)

# practice function
# question 1
# def last_char(name):
#     return name[-1]
# print(last_char("amit"))

# question 2

# def odd_even(num):
#     if num%2==0:
#         return "even"
#     else:
#         return"odd"
# num=int(input("enter your number "))
# print(odd_even(num))

# question 3

# def greter_smaller(a,b):
    
#     if a>b:
#         return a
#     else:
#         return b
# a=int(input(" first number "))    
# b=int(input("second number "))
# bigger=greter_smaller(a,b)
# print(f"{bigger} is greater") 

# define greatest

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>a:
#         return b
#     else:
#         return c
# a=int(input("first number "))
# b=int(input("second number "))
# c=int(input("third number "))    
# d=greatest(a,b,c)
# print(f"{d} is a greter")


# function inside function
# palindrom
# def is_palindrom(word):
#     if word==word[::-1]:
#         return True
#     return False
# word=input("Enter your word ")
# print(is_palindrom(word))


#define fibonacci serise
# 0 1 1 2 3 5 8 13 21 34

# def fabonacci(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(a, b)
#     else:
#         print(a,b,end=" " )
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(b,end=" ")    

# fabonacci(10)

# default parameters
# defalut parameters always make in last

# scope of variable inside and outside functions
# # scope
# def func():
#     x=4
#     return x
# def func2():
#     print(x)
# func2()    
# this program is given error

# LIST

n=int(input("Enter your number "))
def finb(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            
            c=a+b
            a=b
            b=c
            print(b,end=" ")     
finb(n)


