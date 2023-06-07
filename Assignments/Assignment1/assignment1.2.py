#List

lang=["C",'java','javascript']
lang.append('python')
print(lang)

x=lang.copy()
print(x)
x.clear()
print(x)

print(lang.count("python"))
colors=["red","black"]
print(colors)
lang.extend(colors)
print(lang)

print(lang.index("java"))
lang.insert(1,"C#")
print(lang)
lang.pop(1)
print(lang)
lang.remove("java")
print(lang)
lang.reverse()
print(lang)
lang.sort()
print(lang)