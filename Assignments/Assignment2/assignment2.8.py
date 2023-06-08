from functools import reduce
import operator

#input_list = [25, 12, 33, 12, 8, 10]
input_list = input("Enter numbers, separated by spaces: ").split()

# Convert the input elements to integers
input_list = [int(element) for element in input_list]
result = reduce(operator.add, input_list)

print(result)