def print_formatted(number):
    w = len(f'{number:b}')
    for i in range(1,number+1):
        print(f'{i:{w}} {i:{w}o} {i:{w}X} {i:{w}b}')
