

#functions
#user defined functions
"""
def A(a,b=1,c=2):
    return a+b+c
print(A(3))
print(A(4,4,4))
print(A(2,2))

#keyword
def A(a,b=1,c=2):
    return a+b+c
print(A(a=2,b=3))
print(A(c=3,a=2,b=3))

#positional
def add(a,b,c):
    return a+b+c
print(add(10,20,30))

#arbitrary keyword
def key_arg(**kwargs):
    return kwargs
my_dict=key_arg(Apples=10,Bananas=20,Chikoo=30)
print(my_dict['Apples'])
print(my_dict)

#arbitrary positional
def add_num(*n):
    print(n)
    print(sum(n))

add_num(1,2,3,4,5,6)


#higher order functions
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def explain(func):
    greet=func("Hi I am hiGher OrDer")




#lambda
def incr(x):
    x=x+1
    return x
print(incr(4))


print("lambda example")
print((lambda x:x+1)(4))
res=lambda x:x+1
print(res(4))

print((lambda x,y:x**y)(2,2))

li=[1,2,3,4,5]
def inc(num):
    return num+2
res_list=list(map(inc,li))
print(res_list)

print(list(map(lambda x:x+2,li)))

def eor(num):
    if num%2==0:
        return "the number {} is even".format(num)
    else:
        return "the number {} is odd".format(num)

l=[1,2,3,4,5,6,7,8,9,10]
list(map(eor,l))

l4=['apples','bananas','chikus']
r=list(map(lambda x:x.capitalize(),l4))
print(r)


#filter
def odd_num(n):
    if n%2!=0:
        return n
myl=[7,8,5,4,1,6,7]
print(list(filter(odd_num,myl)))

l6=[5,6,7,97,354,335,23]
temp=list(filter(lambda x:x%2==0,l6))
print(temp)

#modules
import os
#os.mkdir("hi")
#os.chdir("hi")
#os.getcwd()
#os.listdir()
#os.rmdir()

os.rmdir("/content/hi")

import math as m
print(m.pi)

import statistics as st
print(st.mean([21,29,34]))

import random as r
print(r.randrange(1,50))
print(r.randint(1,10))
print(r.random())

gn=random.randint(1,10)
gn2=int(input("guess the number"))
if gn2==gn:
    print("you are giving a party")
else:
    print("bachgaya")

#class & object
class CO:
    def addn(self,a,b):
        return a+b
    def subn(self,a,b):
        return a-b
    obj=CO()
    print("addition of two numbers is",obj.addn(5,5))
    print("sub of 2 nos is",obj.subn(5,4))


#inheritence

#single
class Animal:
    def animal_sounds(self):
        return "makes sound"
class Cat(Animal):
    def cat_sounds(self):
        return self.animal_sounds()+"\tMEOW"
    def _str_(self):
        return "CAT"

catobj=Cat()
print(catobj,catobj.cat_sounds())

#multilevel assign


#exceptions
try:
    print(z)
except NameError as ne:
    print("exception occurred",ne)

"""

#file management
#f=open("sample.txt",'x')

import os
os.remove("sample.txt")
f=open("sample.txt",'w')
f.write("WELCOME to Python")
f.close()

f=open("sample.txt","r")
print(f.read())
f.close()

f=open("sample.txt","r")
print(f.read(3))
print(f.tell())
print(f.seek(3))
print(f.seek(0))
print(f.readline())
print(f.readlines())

#copy from one txt file to another

f1=open("f1.txt",'r')
temp=f1.read()
f1.close()

f2=open("f2.txt",'w')
f2.write(temp)
f2.close()


#pickle
import pickle
myl=['a','b','c','d','e']
f3=open("f3.txt",'wb')
pickle.dump(myl,f3)
f3.close()

#unpickle
import pickle
pickle_off=open("f3.txt",'rb')
e=pickle.load(pickle_off)
print(e)

#regular expression
import re
pattern=r"COOKIE"
sequence="Cookie"
if re.match(pattern,sequence):
    print("Matching")
else:
    print("Not a match")


import re
mail=input("enter a mail id")
str1=r'[A-Za-z0-9._-]+@[A-Za-z0-9.-]+[A-Z|a-z]{2,}'
print(re.search(str1,mail).group())
