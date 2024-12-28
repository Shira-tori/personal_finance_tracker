def get_input() -> str:
    while True:
        choice = input('>: ')
        if choice in {'1', '2', '3', '4'}:
            return int(choice)
        print('Input invalid. Please try again.')
