def make_list():
    numbers_list = []
    counter = 3
    while counter > 0:
        item = get_input()
        numbers_list.append(item)
        counter = counter - 1
    print(numbers_list)


def get_input():
    user_input = int(input("Enter a number."))
    return str(user_input)
