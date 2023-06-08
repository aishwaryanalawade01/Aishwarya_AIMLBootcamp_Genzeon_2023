#Using Split, Set, and Sorted Functions:

input_string = "orange, white, red, cyan, green, magenta, cyan, pink, white"

words = sorted(set(input_string.split(", ")))
output = ", ".join(words)

print(output)

#Using Split, List Comprehension, Set, and Sorted Functions:
input_string = "orange, white, red, cyan, green, magenta, cyan, pink, white"

words = sorted({word.strip() for word in input_string.split(",")})
output = ", ".join(words)

print(output)


#Using Split, Set, Sorted, and Lambda Functions:
input_string = "orange, white, red, cyan, green, magenta, cyan, pink, white"

words = sorted(set(input_string.split(", ")), key=lambda x: x.lower())
output = ", ".join(words)

print(output)

#Using Split, List, Set, and Sorted Functions:
input_string = "orange, white, red, cyan, green, magenta, cyan, pink, white"

words = sorted(list(set(input_string.split(", "))))
output = ", ".join(words)

print(output)

#Using Split, Set, and Sort Method:
input_string = "orange, white, red, cyan, green, magenta, cyan, pink, white"

words = list(set(input_string.split(", ")))
words.sort()
output = ", ".join(words)

print(output)
