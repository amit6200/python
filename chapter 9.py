# what is list comprehension
# with the help of list comprehension we can create of list in one line

# create a list of square from 1 to 10
# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)   this is a basic type to create list 

# square=[i**2 for i in range(1,11)] 
# print(square)

# we are creating the negative list
# basic list concept
# negative=[]
# for i in range(1,11):
#     negative.append(-i)
# print(negative)   

# using list comprehension
# negative=[-i for i in range(1,11)]
# print(negative) 

# example
# names=['amit','kit'] 
# new-list=['a','k']

# new_list=[]
# for name in names:
#     new_list.append(name[0])
# print(new_list)    

# new_list=[name[0] for name in names]
# print(new_list)  

# exercise  
# reserve string

# def reverse_string(l):
#     return[name[::-1] for name in l]
# print(reverse_string(['abc','def']))

# list comprehension with if statement

# numbers=list(range(1,11))
# # print(numbers)
# # even list
# nums=[]
# for i in numbers:
#     if i%2==0:
#         nums.append(i)
# print(nums)        
# |^ same work using list comprehension

# numbers=list(range(1,11))
# even_list=[i for i in numbers if i%2==0]
# print(even_list)

# odd number list using list comprehension
# numbers=list(range(1,11))
# odd_list=[i for i in numbers if i%2!=0]
# print(odd_list)

# example
# def num_to_string(l):
#     return[str(i) for i in l if (type(i)==int or type(i)==float) ]
# print(num_to_string([True,False,[1,2,3],1,1.0,3]))  

# list comprehension with if else
# nums=[1,2,3,4,5,6,7]

# new_list=[]
# for i in nums:
#     if i%2==0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)

# same work using list comprehension
# new_list=[i*2 if (i%2==0) else -i for i in nums]
# print(new_list)

# nested list in list comprehension
# example=[[1,2,3],[1,2,3],[1,2,3]]

# nested_list=[[i  for i in range(1,4)] for j in range(3)]
# print(nested_list)
# simple way
# new_list=[]
# for j in range(3):
#     new_list.append([1,2,3])
# print(new_list)    