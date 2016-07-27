import re

from shape import *

main_menu = {
    '1. Rectangle': Rect,
    '2. Circle': Circle,
    '3. Cuboid': Cuboid,
    '4. Cylinder': Cylinder,
    '9. Quit': None
}

def main():
    choice = do_menu(main_menu)
    shape_class = main_menu[choice]

    if shape_class == None: return

    valid_dimensions = False

    while not valid_dimensions:
        print('\nEnter the {}{}'.format(
            ', '.join(shape_class.required_args),
            '.' if len(shape_class.required_args) == 1 else ' separated by stuff.'))
        dimensions = input('> ')
        dimensions = re.split('[^0-9.]+', dimensions)

        if len(dimensions) != len(shape_class.required_args): continue

        try:
            dimensions = [float(i) for i in dimensions]
        except:
            continue

        valid_dimensions = True

    shape = shape_class(*dimensions)
    print(shape)

    main()


def do_menu(menu):
    key_match = []
    while len(key_match) != 1:
        print('\nSelect a shape:')
        [print(key) for key in sorted(menu.keys())]
        choice = input('> ')

        # get matches on string in key
        key_match = [key for key in menu.keys() if choice.lower() in key.lower()]

        if len(key_match) > 1:
            print('\nFound too many matches for: {}'.format(choice))

        if len(key_match) == 0:
            print('\nNo matches found for: {}'.format(choice))

    return key_match[0]


if __name__ == '__main__':
    main()
