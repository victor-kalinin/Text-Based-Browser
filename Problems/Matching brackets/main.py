# put your python code here
stack_string = list(input())
count_pairs = []
message = 'OK'
try:
    for char in stack_string:
        if char == '(':
            count_pairs.append('(')
        elif char == ')':
            count_pairs.pop()
except IndexError:
    message = 'ERROR'
finally:
    if len(count_pairs) > 0:
        message = 'ERROR'

print(message)
