import json
my_list = []

with open('depthlist.txt', 'r') as f:
    lines = f.readlines()
    for x, line in enumerate(lines):
        if line > lines[x-1]:
            my_list.append("increased")

print(len(my_list)+1)

#this returned the correct result