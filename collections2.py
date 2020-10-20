from collections import deque

for t in range(int(input())):
    _, sql = input(), deque(map(int, input().split()))
    ans = True

    for w in range(len(sql) - 1):
        if sql[0] >= sql[1]:
            sql.popleft()
        elif sql[-1] >= sql[-2]:
            sql.pop()
        else:
            ans = False
            break
    print('Yes' if ans else 'No')


#     list = 0
#     try:
#         right = d.pop()
#         left = d.popleft()
#     except IndexError:
#         continue

#     while left != "":
#     	if right >= left:
#         	print("No")
#         	count+=1
#     	elif left >= right and left != "":
#     		print("Yes")
#     		count+=1


# for t in range(int(input())):
#     input()
#     lst = [int(i) for i in input().split()]
#     min_list = lst.index(min(lst))
#     left = lst[:min_list]
#     right = lst[min_list+1:]
#     if left == sorted(left, reverse=True) and right == sorted(right):
#         print("Yes")
#     else:
#         print("No")
