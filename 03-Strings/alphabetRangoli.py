def print_rangoli(size):
    for i in range(size - 1, -size, -1):
        line = ''
        for j in range(size - 1, abs(i), -1):
            line += chr(ord('a') + j) + '-'
        for j in range(abs(i), size):
            line += chr(ord('a') + j) + '-'

        print('--' * abs(i) + line[:-1] + '--' * abs(i))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
