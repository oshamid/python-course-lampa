# d = {"name":"abolfazl", "age":22}
# print(d[i])
# print(type(d))
# print(isinstance(d, dict))
# for key, value in d.items():
#     print(key,value)
######################################
# print(dir(dict))it
# print(d.pop("name"))
# print(d)
#######################################3
# tuple  iterable , immutable, hashable orderede
# x = (1,2,3,4,5)
# print(type(x))
# print(x)
# for i in x:
    # print(i)

# y = (1,)
# print(type(y))
# for i in y:
#     print(i)
# print(x[1])
# print(x)
# y = (1,2,3,1,4,5)
# print(x is y)
# y = list(x)
# y[1]="hamid"
# print(tuple(y))
# print(x + y)
# print(dir(tuple))
# print(y.count(1))
# print(x.index(3))
#########################################
# """set iterable not douplicated not oreder immutable not hashable"""
# """ frozenset hashable immutable"""
# s = {1,2,3,"ali",frozenset({"abolfazl"}), 3}
# print(s)
# for i in s:
    # print(i)
# print(s[0])
# s[0] = "abolfazl"
# print(s)
# y = frozenset({1,2,3,4,4})
# s.update({99,88})
# s.remove("ali")
# s.pop()
# s.remove(8)
# print(s)
# print(dir(set))
#########################################
# a=int(input("?"))
# for i in arr:
#     print(i)
# for i in range(8):
    # print(arr[i] == target)

# print(arr[0])
# time complexcit = O(n)
# log(N)
# arr=[1,2,3,43,55,6,7,8]
# target = 37
# first = 0
# last = len(arr) -1
# while first <= last:
#     mid = (first + last) // 2 
#     if arr[mid] == target:
#         print(mid)
#         break
#     elif arr[mid] < target:
#         first =mid + 1
#     else:
#         last =mid - 1
    
# else:
#     print(-1)
#################################################

# 4444 3333 2222 1111 $ 444 333 222 111 $ 44 33 22 11 $ 4 3 2 1
# target = 3
# 333 222 111$ 33 22 11$ 321
# 22 11 $2 1
##################################################
# x = [1,2,3]
# x.remove(2)
# def foo():
#     print(1)
# foo()
# name = input("whats ur name? \n")
# def foo(name):
#     print(f"my name is {name}")
# foo("ali")
# def foo(arr):
#     for i in arr:
#         if i % 2 == 0:
#             print(i)
# foo([1,2,3,4,8,77,99])


# target = int(input())
# def ag (target):
#     arr=[1,2,3,43,55,6,7,8]
#     first = 0
#     last = len(arr) -1
#     while first <= last:
#         mid = (first + last) // 2 
#         if arr[mid] == target:
#             print(mid)
#             break
#         elif arr[mid] < target:
#             first =mid + 1
#         else:
#             last =mid - 1
        
#     else:
#         print(-1)
# ag(target)
#################################################
# def foo(arr, *args,**kwargs):
#     print(arr)
#     print(args)
#     print(kwargs)

# foo( 1,2,3, "ali", name="hamidreza")
#################################################
# def foo(name, family, code):
#     print(f"{name} --> {family}")

# foo("ali", "sadeghi", 998)
##################################3
# def foo(x):
#     return 5 * x
# print(foo(4))
# print(foo(5))
# print(foo(44))
# print(foo(22))
####################################
# def foo(x):
#     print(x * 3)
# foo(5)

# foo = lambda x:x*3
# print(foo(5))
##############################3
# foo = lambda x, y:x + y
# print(foo(8, 9))
# ################################3
# lst1=[1,2,3,4,11]
# lst2=[1,2,3,4,11]
# if len(lst1) == len(lst2):
#     for i in range(lst1):
#         m = lst1[i]
#         for x in range(lst2):
#             s = lst2[x]
#             if m==s:
#                 print("Yes")
            

# else:
#     print("No")

##########################################################
# with open("demo.txt", "r") as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())

# f = open("demo.txt", "w")
# f.write("lkxjndfvlx")
# f.close()
#################################################
# import json

# me = {
#     "name":"ali",
#     "age":22
# }
# print(json.dumps(me))
# with open("demo.txt", "a") as file:
#     file.write(str(me))
####################################################
import csv


with open("teacher.csv", "a") as csvfile:
    lists =["first_name", "last_name", "password"]
    x = csv.DictWriter(csvfile, fieldnames=lists)
    x.writeheader()
    x.writerow(
        {
        "first_name":"abolfazl",
        "last_name":"karimi",
        "password":"0165"
    })

with open("teacher.csv", "r") as rf:
    x = csv.reader(rf)
    for i in x:
        print(", ".join(i))