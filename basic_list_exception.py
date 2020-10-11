def make_list():
    numbers_list = []
    counter = 3
    while counter > 0:
        item = get_input()
        try:
            if 0 < int(item) < 50:
                numbers_list.append(item)
                counter = counter - 1
        except ValueError as err:
            raise ValueError
    print(numbers_list)


def get_input():
    try:
        user_input = int(input("Enter a number."))
        return int(user_input)
    except ValueError as err:
        raise ValueError
