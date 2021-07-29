import string
import random

def pass_gen():

    s_l = string.ascii_lowercase
    s_u = string.ascii_uppercase
    s_d = string.digits
    s_p = string.punctuation

    # empty list
    pass_list = []

    # add chars to the list
    pass_list.extend(s_l)
    pass_list.extend(s_u)
    pass_list.extend(s_d)
    pass_list.extend(s_p)

    # shuffle passowrd list chars (reorganize the order of the list items)
    random.shuffle(pass_list)

    # get passowrd length from user input
    pass_length = int(input("Enter password length : "))

    # convert password list to string from index 0 to password length enterd from user
    password_result = "".join(pass_list[0:pass_length])

    # print password generated 
    print("Password generated is : ", password_result)

pass_gen()
