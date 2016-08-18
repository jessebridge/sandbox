def main():
    name = get_name()
    print_name(name)

def print_name(name):
    for char in range(1, (len(name)), 2):
        print(name[char])

def get_name():
    name = input("please enter your name")
    while name == "":
        print("error")
        name = input("please enter your name")
    return name


def get_name():
    main()


get_name()