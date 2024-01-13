cube = lambda x: x**3

def fibonacci(n):
    sequence = []
    for i in range(n):
        if i == 0 or i == 1:
            sequence.append(i)
        else:
            integer = sequence[i-1] + sequence[i-2] 
            sequence.append(integer)
    return sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
