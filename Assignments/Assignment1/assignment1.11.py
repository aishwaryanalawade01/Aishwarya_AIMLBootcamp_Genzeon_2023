# Bitwise AND
x = 10  # Binary: 1010
y = 6   # Binary: 0110
result_and = x & y
print("Bitwise AND:", result_and)  # Output: 2 (Binary: 0010)

# Bitwise OR
x = 10  # Binary: 1010
y = 6   # Binary: 0110
result_or = x | y
print("Bitwise OR:", result_or)  # Output: 14 (Binary: 1110)

# Bitwise XOR
x = 10  # Binary: 1010
y = 6   # Binary: 0110
result_xor = x ^ y
print("Bitwise XOR:", result_xor)  # Output: 12 (Binary: 1100)

# Bitwise NOT
x = 10  # Binary: 1010
result_not = ~x
print("Bitwise NOT:", result_not)  # Output: -11 (Binary: 11111111111111111111111111110101)

# Bitwise Left Shift
x = 5  # Binary: 0101
num_bits_shift = 2
result_left_shift = x << num_bits_shift
print("Bitwise Left Shift:", result_left_shift)  # Output: 20 (Binary: 10100)

# Bitwise Right Shift
x = 15  # Binary: 1111
num_bits_shift = 2
result_right_shift = x >> num_bits_shift
print("Bitwise Right Shift:", result_right_shift)  # Output: 3 (Binary: 0011)
