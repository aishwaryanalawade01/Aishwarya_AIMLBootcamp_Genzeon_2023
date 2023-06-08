def replace_spaces_with_hyphens(input_string):
    output_string = input_string.replace(" ", "-")
    return output_string

# Example usage
input_string = "This program converts spaces into hyphen"
output_string = replace_spaces_with_hyphens(input_string)
print(output_string)


# without function
output_string2=""
for iter in input_string:
    if iter==" ":
        output_string2+="-"
    else:
        output_string2+=iter

print(output_string2)

