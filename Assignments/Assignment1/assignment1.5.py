fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
x=fruits.copy()
print(x)
fruits.discard("banana")
print(fruits)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
x.difference_update(y)
print(x)
z = x.intersection(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook","cherry"}
z = x.union(y)
print(z)

fruits.pop()
print(fruits)

z = x.isdisjoint(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

z = y.issuperset(x)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

