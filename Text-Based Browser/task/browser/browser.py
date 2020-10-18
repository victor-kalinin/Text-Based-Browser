import sys
import os

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
sites = {'nytimes.com': nytimes_com, 'bloomberg.com': bloomberg_com}
args = sys.argv
stack = []

pages_dir = args[1]
if not os.path.exists(pages_dir):
    os.mkdir(pages_dir)

while True:
    user_input = input()
    if user_input == 'exit':
        break
    elif user_input == 'back':
        if len(stack) > 1:
            stack.pop()
            user_input = stack.pop()
        else:
            continue

    if user_input.find('.') < 0 or user_input not in sites.keys():
        print('Address error')
        continue
    else:
        stack.append(user_input)
        filename = user_input[:user_input.find('.')]
        if os.path.exists(pages_dir + '//' + filename):
            with open(pages_dir + '//' + filename) as f:
                for line in f:
                    print(line.strip())
        else:
            print(sites[user_input])
            with open(pages_dir + '//' + filename, 'w') as f:
                f.write(sites[user_input])

