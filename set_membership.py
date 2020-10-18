set_things = {'1', '7', '23', '29', '15', '78'}


def in_set(set_list, *x):
    found = True
    try:
        if x in set_list:
            found
    except ValueError as err:
        print("Item does not exist")
        found = False

    return found


result = in_set(set_things, '1')

if result:
    print("This item is found.")
