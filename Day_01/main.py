x=True
y=False


s="hello world"
#x=b"hello"
x=bytearray(5)
x=memoryview(bytes(4))

a=3
b=4.0
c=float(a)
d=int(b)
print(c,d)

e=a+b
print(a+b)
print(a-b)
print(a**b)
print(a//b)


x="hello world"
y={1:'a',2:'b'}
print('H' in x)
print(1 in y)
print('a' in y)

str1="Genzeon"
print(str1[0])
print(str1[-1])
print(str1[:])
print(str1[1:])
print(str1[:4])
print(str1[2:5])
print(str1[-7:-1])
print(str1[0:5:2])
print(str1[::-1])


a="hi"
b="python"
c=a+b
d=a*4
print(c)
print(d)


str="hey there"
print(str.upper())
print(str.strip())
print(str.swapcase())


myl=[1,2,'a',"hello"]
print(myl)
myl2=[4,6,3.5]
myl3=[99,myl,myl2]
print(myl3)
print(myl[3][1])
print(myl3[1][3][1:4])

lis=[1,2,3,4]
lis.append(5)
print(lis)

l1=[33,23,15,54,90]
l1.sort()
print(l1)

print("Hello"+'python')


