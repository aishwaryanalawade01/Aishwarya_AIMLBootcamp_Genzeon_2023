# Identity - is operator
x = 10
y = 10
print("is operator:", x is y)  # Output: True

# Identity - is not operator
x = 10
y = 20
print("is not operator:", x is not y)  # Output: True

# Identity - is operator with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("is operator with lists:", list1 is list2)  # Output: False

# Identity - is not operator with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("is not operator with lists:", list1 is not list2)  # Output: True

# Identity - is operator with None
value = None
print("is operator with None:", value is None)  # Output: True
