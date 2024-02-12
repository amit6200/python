# list in python
# ordered collection of items

# num=[1,2,3]
# print(num)

# a=["abcd","jhsd"]
# print(a)

# mix=[1,2,3,"five",2.3,None]
# print(mix[:6])

# mix[1]='two'
# print(mix)

# add data to list

# fruits=['apple']
# fruits.append('mango')
# print(fruits)

# fruits=[]
# fruits.append("mango")
# print(fruits)

# # more method to add data in list 
# # insert method
# a=["mango"]
# a.insert(0,"apple")
# print(a)

# join two list
# a=["apple"]
# b=["mango"]
# c=a+b
# print(c)

# # extand method
# a=["apple"]
# b=["mango"]
# a.extend(b)
# print(a)
# print(b)
# a.append(b)
# print(a)

# common methods to delete data from list
# pop method
# a=["ab","cd","bn"]
# a.pop(1)
# print(a)

# delete oprator
# a=["ab","cd","bn"]
# del a[1]
# print(a)

# remove method
# a=["ab","cd","bn","cd"]
# a.remove("ab")
# a.remove("ac")
# a.remove("cd")
# print(a)

# in keyword with list
# a=["ab","cd","bn","cd"]
# if "ab" in a:
#     print("present")
# else:
#     print("not present")

# some more list methods

# count method
# a=["ab","cd","bn","cd"]
# b=a.count("cd")
# print(b)

# sort method is sort the list
# a=["ab","cd","bn","cd"]
# a.sort()
# print(a)
# a=[1,3,5,2,1]
# a.sort()
# print(a)

# sorted function is only print in sorted order
# a=[1,3,5,2,1]
# print(sorted(a))
# print(a)

# clear methods
# a=[1,3,5,2,1]
# a.clear()
# print(a)

# copy method
# a=[1,3,5,2,1]
# b=a.copy()
# print(b)

# list comparision
# 'is' vs '==' comparision

# a=[1,2,3,4,5,6,7,8]
# b=[6,7,8]
# c=[1,2,3,4,5,6,7,8]
# print(a==b) #value are not equal
# print(a==c) #value are same
# print(a is c) # is check in same place in memory  but == to check list value

# join and split methods
# spilt method convert string to list
# a='amit,24'.split(',')
# print(a)

# name,age=input("enter your name and age ").split(',')
# print(name)
# print(age)

# join method
# convert list to string
# a=['amiit','24']
# b=','.join(a)
# print(b)

# list vs array
# c,c++,java
# array int,string

# list - store any data/flexible
# array module -fix data type
# javascript array=python list/flexible

# list vs string
# strings are immutable
# list are mutable

# s="string"
# t=s.title()
# print(t)

# l=['a','v','d']
# # l.pop()
# l.append("r")
# print(l)

# looping in list
# for loop

# fruits=['a','b','c']
# for fruit in fruits:
#     print(fruit)

# while loop 
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

# list inside list 

# l=[[1,2,3],[4,5,6],[7,8,9]]
# # print(len(l))
# # print(l[0])
# # for sublist in l:
# #     for i in sublist:
# #         print(i)

# # b=l[1][1]
# b=l[2][2]
# print(b)
# s="string"
# print(type(s))

# more about list
# range method
# numbers=list(range(1,11))
# pop method
# b=numbers.pop()
# print(numbers)
# print(b)  
# index method  
# print(numbers.index(1))#item ka index print hoga is method se
# pass by value
# def negative_list(l):
#     negative=[]
#     for i in l:
#         negative.append(-i)
#     return negative
# print(negative_list(numbers))    

# def square_list(l):
#     square=[]
#     for i in l:
#         square.append(i**2)
#     return square
# print(square_list(numbers)) 
 
# def reverse_list(l):
#      l.reverse()
#      return l
# numbers=[1,2,3,4,5]
# print(reverse_list(numbers))

# def reverse_list(l):
#     return l[::-1]
# numbers=[1,2,3,4,5]
# print(reverse_list(numbers))

# every list element reverse
# def reverse_elements(l):
#     elements=[]
#     for i in l:
#         elements.append(i[::-1])
#     return elements

# words=['abc','asd'] 
# print(reverse_elements(words))   

# filter odd even

# def filter_odd_even(l):
#     odd=[]
#     even=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     output=[odd,even]
#     return output
# nums=[1,2,3,4,5,6,7,8,9]
# print(filter_odd_even(nums))        

# find common element in list
# def common_finder(l1,l2):
#     output=[]
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output  

# print(common_finder([1,2,3,4],[1,2,5,6]))   

# min and max functions

# number=[6,60,4]
# # print(min(number))
# # print(max(number)) 

# def greatest_diff(l):
#     return max(l)-min(l)
# print(greatest_diff(number))

# /find the sublist in list
# def sublist(l):
#     count=0
#     for i in l:
#         if type(i)==list:
#             count+=1
#     return count
# a=[1,23,4,[12,4]]   
# print(sublist(a))       
