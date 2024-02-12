# how to create dict

# user={'name':'amit','age':20}
# print(user)
# print(type(user))

# # second method to create dict
user1=dict(name='Amit',age=20)
# print(user1)

# in dict we are access data using key
# print(user1['name'])
# print(user1['age'])

# type of data store in dictionary 
# anything
# numbers,strings,list,dictionary

# user_info={
#     'name':'amit',
#     'age':20,
#     'fav_movies':['asur','famliy man'],
#     'fav_tunes':['awakening','fairy tale']
    
# }
# print(user_info)
# print(user_info['fav_movies'])

# how to add data in empty dictionary

# user={}
# user['name']='mohit'
# user['age']=100
# print(user)

# in  keyword and itertions in dictionary
# user_info={
# 'name':'amit',
# 'age':20,
# 'fav_movies':['asur','famliy man'],
# 'fav_tunes':['awakening','fairy tale']
# }

# check key
# if 'names' in user_info:
#     print('present')
# else:
#     print('not present')

# check value

# if 'amit' in user_info.values():
#     print('present')
# else:
#     print('not present')

# loops in dictionary

# all key print this method.
# for i in user_info:
#     print(i)

# all value print this method.
# for i in user_info.values():
#     print(i)

# values method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# item method
# user_item=user_info.items()
# print(user_item)

# user_info={
# 'name':'amit',
# 'age':20,
# 'fav_movies':['asur','famliy man'],
# 'fav_tunes':['awakening','fairy tale']
# }

# how to add data
# user_info['fav_song']=['song1','song2']
# print(user_info)

# pop method
# popped_item=user_info.pop('fav_tunes')
# print(f"popped item is {popped_item}")
# print(user_info)

# popitem method
# popped_item=user_info.popitem()
# print(user_info)
# print(popped_item)

# update method
# user_info={
# 'name':'amit',
# 'age':20,
# 'fav_movies':['asur','famliy man'],
# 'fav_tunes':['awakening','fairy tale']
# }

# more_info={'name':'amit singh','state':'up','hobbies':['cricket','coding']}

# user_info.update(more_info)
# print(user_info)

# fromkeys are use to create dict

# d=dict.fromkeys(('name','age','hight'),'unknown')
# d=dict.fromkeys(("abc"),'unknown')
# d=dict.fromkeys((range(1,11)),'unknown')
# d=dict.fromkeys(['name','age'],['unknown,unknown'])
# print(d)

# get method
# d={'name':'unknown', 'age':'unknown',}
# print(d.get('age'))
# if 'name' in d:
#     print('present')
# else:
# #     print('not present')
# if d.get('name'):
#     print('present')
# else:
#     print('not present')

# clear()
# d.clear()
# print(d)

# # copy()
# d1=d.copy()
# print(d1)

# d={'name':'unknown', 'age':'unknown','age':33}
# # print(d.get('names','not found'))
# print(d)

# cube finder
# def cube_finder(n):
#     cubes={}
#     for i in range(1,n+1):
#         cubes[i]=i**3
#     return cubes
# print(cube_finder(10))

# word counter
# def word_counter(s):
#     count={}
#     for char in s:
#         count[char]=s.count(char)
#     return count
# print(word_counter('amit'))


# user_info={
# 'name':'amit',
# 'age':20,
# 'fav_movies':['asur','famliy man'],
# 'fav_tunes':['awakening','fairy tale']
# }

# user={}
# name=input('what is your name:')
# age=input('what is your age:')
# fav_movies=input('your fav movies separated by , ').split(',')
# fav_songs=input('your fav songs separated by , ').split(',')

# user['name']=name
# user['age']=age
# user['fav_movies']=fav_movies
# user['fav_songs']=fav_songs
# # print(user)
# for key, value in user.items():
#     print(f"{key}:{value}")



    