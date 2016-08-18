def main():
    lower = 10
    upper = 50
    get_number(lower,upper)

def get_number(lower,upper):
    number = int(input("please enter a number between 10 and 50: "))
    while number < lower or number > upper:
        print('please enter a valid number!')
        number = int(input('please enter a number between 10 and 50: '))
    print("valid number")


main()