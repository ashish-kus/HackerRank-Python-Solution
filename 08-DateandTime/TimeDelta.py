import datetime
import os

def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.datetime.strptime(t1, format)
    dt2 = datetime.datetime.strptime(t2, format)
    delta = dt1 - dt2
    
    return str(abs(int(delta.total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

