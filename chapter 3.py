# if conditions
# if condition is true then code will excute

# age=input("Enter your age ")
# age=int(age)
# if age>=14:
    # print("you are above 14")
#  pass statement 
# x=19
# if x>19:
#   pass

# else statement

# age=input("Enter your age ")
# age=int(age)
# if age>=14:
#       print("you are above 14")   
# else:
#     print("you can't play")

# number guessed game

# winning_number=27
# user_input=int(input("guess a number b/w 1 and 100 "))
# if user_input==winning_number:
#     print("you win")
# else:
#     if user_input<winning_number:
#         print("too low")
#     else:
#         print("too high")

# AND OR OPERATOR
# and operator in both condition true then print true
# but or operator in any one condition true then print true


# name='abc'
# age=19
# if name=='abc' and age==19:
#     print("True")
# else:
#     print("false")
    
# name='abc'
# age=19
# if name=='abc' or age==19:
#     print("True")
# else:
#     print("false")

# name =(input("Enter your name "))
# age=int(input("Enter your age "))
# if age>=10 and (name[0]=='a' or name[0]=='A'):
#     print("Watch coco")
# else:
#     print("sorry")

#if elif else statement 
# check multiple conditions

# age=int(input("Enter your age "))

# if 0<age<=3:
#     print("ticket price:free")
# elif 3<age<=10:
#     print("ticket price:150")
# elif 10<age<=60:
#     print("ticket price:250")
# else:
#     print("ticket price:200") 

# in keyword
# name="amit"
# if "a" in name:
#     print("a is present in name")
# else:
#     print("not present")

# check empty or not
# name="amit"
# if name:
#     print("not empty")
# else:
#     print("empty")



# loop in python
# while loop,for loop
# while loop
# i=1
# while i<=10:
#     print(f"Amit {i}")
#     i=i+1

# sum 1 to 10
# total=0
# i=1
# while i<=20:
#     total=total+i
#     i=i+1
#     print(total)

# n=int(input("Enter your number "))
# total=0
# i=1
# while i<=n:
#     total+=i
#     i+=1
#     print(total)

# n=input("Enter your number ")
# total=0
# i=0
# while i<len(n):
#    total+= int(n[i])
#    i+=1
#    print(total)

# name=input("enter your name ")
# i=0
# while i<len(name):
#     print(f"{name[i]}:{name.count(name[i])}")
#     i+=1

# infinite loop
# i=0
# while i<=10:
#     print("hello world")
# while True:
#     print("hello world")

# for loop with range function

# for i in range(1,10):
#     print(f"Amit:{i}")

# example of for loop
# sum from 1 to 10

# total=0
# for i in range(1,11):
#     total+=i
#     print(total)

# n=int(input("Enter your number"))
# total=0
# for i in range(1,n+1):
#     total+=i
#     print(total)

# ask user a num like 1234
# calculate sum of digit 1+2+3+4

# total=0
# num=input("Enter a num")
# for i in range(0,len(num)):
#     total+=int(num[i])
#     print(total)

# exercise
# user name and count each character

# name =input("Enter your name")
# temp=""
# for i in range(len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]}:{name.count(name[i])}")
#         temp += name[i]

# break and continue
# break keyword use break the loop

# for i in range(1,11):
#     if i ==5:
#         break
#     print(i)

# continue
# print 1 to 10 but not 5
# 1,2,3,4,6,7,8,9,10
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

# exercise modify number guessing game

# wining_number=43
# guess=1
# number=int(input("guess a number b/w 1 and 100 "))
# game_over=False

# while not game_over:
#     if number==wining_number:
#         print(f"you win, and you guessed this number in {guess} time")
#         game_over=True
#     else:
#         if number<wining_number:
#             print("too low ")
#             guess+=1
#             number=int(input("guess again "))
#         else:
#               print("too high ")
#               guess+=1
#               number=int(input("guess again "))

# dry principle
# don't repeat code
# wining_number=43
# guess=1
# number=int(input("guess a number b/w 1 and 100 "))
# game_over=False

# while not game_over:
#   if number==wining_number:
#      print(f"you win, and you guessed this number in {guess} time")
#      game_over=True
#   else:
#         if number<wining_number:
#             print("too low ")
#         else:
#               print("too high ")
              
              
#         guess+=1
#         number=int(input("guess again ")) 
        
# step argument
# for i in range(1,11,2):
#     print(i)

# 10,9,8

# for i in range(10,0,-1):
#     print(i)

# for i in range(1,-11,-1):
#     print(i)


# for loop and string

# a="amit"
# for i in a:
# for i in "mohit":
#     print(i)

# example

# num=input("Enter your number ")
# total=0
# for i in num:
#     total+=int(i)
#     print(total)
