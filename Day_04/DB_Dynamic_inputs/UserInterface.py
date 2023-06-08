import Input_pack
from fetch_branch import fetch_based_branch
while True:
    print("----------MENU---------")
    print('''
    1.Enter Participant details
    2. Fetch the participant details
    3. Fetch participant based on branch
    4. Enter wrongly entered name change
    5. exit''')

    print("Choose any option from above menu:")
    ch=int(input())
    if ch==1:
        u.input_data()
    elif ch==2:
        f.fetch_data()
    elif ch==3:
        input_branch=input("Enter Branch to be fetched:")
        fetch_based_branch(input_branch)
    elif ch==4:
        pass
    else:
        break




#input should be comma separated values
#id & new name
#101,Ash - 1 line input
#id, new name