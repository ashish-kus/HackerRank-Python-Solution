n, a_set, num_operations = int(input()), set(map(int, input().split())), int(input())

operations = {'intersection_update': 'intersection_update', 'update': 'update', 
              'symmetric_difference_update': 'symmetric_difference_update', 'difference_update': 'difference_update'}

for _ in range(num_operations):
    operation, len_other_set = input().split()
    other_set = set(map(int, input().split()))
    getattr(a_set, operations[operation])(other_set)

print(sum(a_set))

