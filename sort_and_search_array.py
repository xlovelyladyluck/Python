import array as arr

simple_array = ['7', '20', '65', '8', '23', '67']

item = input("Please enter a number to see the array position.")


def search_array(thing):
    try:
        index_position = simple_array.index(thing)
        print(f'The position of "{thing}" is:', index_position)
    except ValueError as err:
        print(f'The item "{thing}" is not found in this array', err)


search_array(item)


def sort_array(array):
    sorted(array)
    print(array)


sort_array(simple_array)
