# write your code here
for n in range(1, 11):
    with open(f'file{n}.txt', 'w') as f:
        f.write(str(n))
