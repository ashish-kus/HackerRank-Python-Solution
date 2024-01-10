from collections import namedtuple

def main():
    n=int(input())
    b=input().split()
    c=[input().split() for _ in range(n)]
    print(sum(int(c[z][b.index("MARKS")])for z in range(len(c)))/len(c))
if __name__ == "__main__":
    main()
