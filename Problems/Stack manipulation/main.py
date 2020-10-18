stack = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'PUSH':
        stack.append(command[1])
    elif command[0] == 'POP':
        stack.pop()

for s in stack[::-1]:
    print(s)