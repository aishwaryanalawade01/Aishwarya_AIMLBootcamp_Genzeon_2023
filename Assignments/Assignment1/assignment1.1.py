#strings

#multiline strings
a="""This is an example
of multiline string.
It is declared using 
3 single/double quotes"""

print(a)

#strings are arrays
print(a[2])

#looping through string
for x in "strawberry":
    print(x)

#string methods
txt="hello! this is a python assignment"
#x=txt.capitalize() #uppercase first letter of sentence and rest to lower
print(txt.capitalize())

txt1="Hello, And Welcome to my World!"
print(txt1.casefold()) #returns a string where all the characters are lower case,  stronger, more aggressive than lower

txt2='strawberry'
print(txt2.center(20))
print(txt2.center(20,"$"))

print(txt2.count('r'))
print(txt2.count('r',3,9))

print(a.count('is'))
print(a.encode())

print(txt1.endswith('!'))
print(txt1.endswith('!',2,9))

txt3="G\te\tn\tz"
print(txt3.expandtabs(3))#set tab size to specifies no of whitespaces, default is 8

print(txt1.find("e"))

t1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
t2 = "My name is {0}, I'm {1}".format("John",36)
t3 = "My name is {}, I'm {}".format("John",36)

print(t1+"\n"+t2,"\n",t3)

print(txt1.title())

myTuple=("Ash","Swanand","Krunali")
x="#".join(myTuple)
print(x)
y="".join(myTuple)
print(y)
s="HAHA"
z=s.join(myTuple)
print(z)

print(txt.partition("python"))
print(txt.replace("python","java",1))
print(txt.split(" "))
print(a.splitlines())
tfill="Hell"
print(tfill.swapcase())
print(tfill.zfill(10))


