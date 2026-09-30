def add_entry(id):
    id["city"] ="delhi"
def reassign_dict(id):
     id = {"name": "nishi" , "age": 19}
     print("inside" , id )
my_dict={"name": "nishi"}
print("before:",my_dict)
add_entry(my_dict)
print("after add_entry:" , my_dict)
reassign_dict(my_dict)
print("after reassign_dict :" , my_dict)
