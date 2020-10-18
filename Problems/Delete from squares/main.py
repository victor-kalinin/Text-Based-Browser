user_input = int(input())

if user_input in squares:
    print(squares.pop(user_input))
else:
    print('There is no such key')
