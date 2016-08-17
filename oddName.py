"""
Jesse Bridge
"""
def name_insert():
    name_error = False
    while name_error == False:
        name = input("what is your name")
        if name == "":
            print ("error")
        else:
            print ("thankyou" + name)
            name_error = True
name_insert()
