
def wrapper(f):
    def fun(l):
        # [print("+91 " + i[-10:-5] + " " + i[-5:]) for i in sorted(l)]
            f(map(lambda n: f'+91 {n[-10:-5]} {n[-5:]}', l))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# 3
# 09191919191
# 9100256236
# +919593621456
