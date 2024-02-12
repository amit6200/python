# tuple data structure
# tuple can store any data type
# tuple are immutable, once tuple is ceated you can't update
# data inside tuple

# example=('one','two','three')
# no append,no insert,no pop,no remove
# days=('monday','tuesday')
# tuples are faster than lists

# Methods
# count,index
# len funtion
# slicing
# print(example[:2])


# looping in tuple

mixed=(1,2,3,4.0)
for i in mixed:
    print(i)

# tuple with one element 
# nums=(1)
# words=('words1')
# print(type(words))
# print(type(nums))
# print(type(mixed))

# tuple without parenthesis

# l='njdhk','khdk'
# print(type(l))

# tuple unpacking
# stores=('and','hdsj')
# store1,store2=(stores)
# print(store1)

# list inside tuple

# favorites=('southern mangolia',['tokyo ghoul','landscape'])
# favorites[1].pop()
# favorites[1].append("we made it")
# print(favorites)

# some function used in tuple 
# print(min(mixed))
# print(max(mixed))
# print(sum(mixed))

# function returning two values

# def func(int1,int2):
#     add=int1+int2
#     multiply=int1*int2
#     return add,multiply
# print(func(4,5))

# something more about tuples,list,str

# nums=tuple(range(1,11))
# print(nums)

# nums=list(range(1,11))
# print(nums)

# nums=str((1,2,3,4,5))
# print(nums)
# print(type(nums))
