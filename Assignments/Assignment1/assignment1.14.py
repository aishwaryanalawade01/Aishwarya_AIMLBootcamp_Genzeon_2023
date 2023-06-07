# Negative Indexing
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print("Negative Indexing:")
print(fruits[-1])  # Output: kiwi
print(fruits[-2])  # Output: grape
print(fruits[-3])  # Output: orange

# Slicing
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print("\nSlicing:")
print(fruits[1:4])  # Output: ['banana', 'orange', 'grape']
print(fruits[:3])   # Output: ['apple', 'banana', 'orange']
print(fruits[2:])   # Output: ['orange', 'grape', 'kiwi']
print(fruits[1:5:2])  # Output: ['banana', 'grape']
print(fruits[::-1])  # Output: ['kiwi', 'grape', 'orange', 'banana', 'apple']
