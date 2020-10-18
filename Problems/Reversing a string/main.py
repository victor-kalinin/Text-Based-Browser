n = int(input())

my_stack = []

for _ in range(n):
    my_stack.append(input())

for x in my_stack[::-1]:
    print(x)
