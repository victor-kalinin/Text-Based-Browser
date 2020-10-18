book_stack = []

for _ in range(int(input())):
    user_do = input().split()
    if user_do[0] == 'BUY':
        book_stack.append(' '.join(user_do[1:]))
    elif user_do[0] == 'READ':
        print(book_stack.pop())