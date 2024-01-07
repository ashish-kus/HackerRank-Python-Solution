from collections import deque
test_cases = int(input())
for _ in range(test_cases):
    size, dq, result_list = int(input()), deque(map(int, input().split())), []
    for _ in range(size):
        if dq[-1] >= dq[0]:
            result_list.append(dq.pop())
        else:
            result_list.append(dq.popleft())

    verdict = "Yes" if result_list == sorted(result_list, reverse=True) else "No"
    print(verdict)
