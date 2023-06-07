#tuples
t0=(1,2,3,4)
t1=("hi",1.2,4)
t2=("hello",t0,t1)

#indexing
print(t2[2][0])
print(t2[-3])

#slicing
print(t0[2:])

#tuple methods
print(t0.count(1))
print(t0.index(1))
#print(t0.max(1))

#sets
s1={1,3}
s2={1,2,3,"hi",(1,2,3,4)}

l=[1,3,4,5,7]
s3=set(l)
print(s3)
s1.add(2)
print(s1)
s1.update([2,3,4])
print(s1)
s1.discard(4)
print(s1)
#s1.remove(4)
print(s1)

#set operations
a={1,2,3,4}
b={4,5,6,7}

#union
print(a|b)
print(a.union(b))
print(b.union(a))







#dictionary
dic={'name':'srk','phone':1234567890,'add':'pune'}
print(dic['name'])
print(dic.keys())
print(dic.values())
print(dic.get('name'))


#take integer as input
"""a=int(input("enter a number"))
print(a)"""
#by default input is string
"""b=input("enter a string")
print(b)"""

#string formats
name="genzeon"
lang="python"
c='trainees'

print(c, " are learning",lang,"programming at",name)

#format
print("{} are learning {} programming at {}".format(c,lang,name))
print("{1} are learning {2} programming at {0}".format(c,lang,name))

#placehlder
#print("%s "



#if-else
var1=-1
if var1>0:
    print("true")
else:
    print("false")

#if-else nested
age=int(input("\nEnter age"))
if(age>7):
    print("full ticket")
    if(age>60):
        print("senior citizen")
else:
    print("half ticket")

#loops
#for loops
ln=[65,66,78,46,12,64]
sum=0
for val in ln:
    sum=sum+val
print("the sum is",sum)

for i in range(1,33,2):
    print(i)

#tables in loops



num=int(input('enter list of tables you want to print'))
i=1
while(i<=num):
    print("\n"f"Table {i}")

    j=1
    while(j<11):
        print(f"{i}*{j}={i*j}")
        j=j+1
    i=i+1

#control statements

#break
for l in "python":
    if l=="h":
        break
    print("current letter:",l)

int1=10
while(int1>0):
    print("current values:",int1)
    int1=int1-1
    if int1==5:
        break

int1=10
while(int1>0):

    int1=int1-1
    if int1==5:
        continue
    print("current values:", int1)

#pass
for l in "python":
    if l=="h":
        pass
        print("this is a pass block")
    print("current letter:",l)