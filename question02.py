def change_string(s):
    s="x"+s[1:]
    print("inside function:",s)

    my_string="hello"

    change_string(my_string)
    print("after function call :", my_string)