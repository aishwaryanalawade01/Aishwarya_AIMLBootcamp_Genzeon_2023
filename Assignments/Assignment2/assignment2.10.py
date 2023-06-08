"""
#2.10
def count_digits(num):
    count=len(str(num))

    file=open("countdigit.txt","w")
    file.write(str(count))
    return count

input=123456789
res=count_digits(input)
print(f"Total digits in input:{res}")
"""

"""
#2.11
def cal_sum(n):
    sum=(n * (n + 1))/2

    file=open('sumresult.txt','w')
    file.write(str(sum))
    return sum

input_no=int(input("Enter a number: "))

res=cal_sum(input_no)
print(f'Sum of first {input_no} natural numbers is: {res}')
"""


"""
#2.12
def capitalize_list(in_ls):
    cap_ls=list(map(str.capitalize, in_ls))
    file=open("listupper.txt",'w')
    file.write(str(cap_ls))
    return cap_ls

input_ls=input("Enter list of elements separated by commas: ").split(',')

res=capitalize_list(input_ls)
print("Capitalized list: ",res)
"""


#