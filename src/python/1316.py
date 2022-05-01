from sys import stdin, stdout
# a = int(stdin.readline())
# words = []
# for _ in range(a):
#     words.append(stdin.readline().strip())
# sum_val = 0
# for i in words:
#     start = None
#     length = None
#     if len(i) == i.count(i[0]):
#         sum_val += 1
#         continue
#     for j in i:
#         if start is None:
#             start = j
#             length = i.count(j) - 1
#             continue
#         if j == start:
#             length -= 1
#         else:
#             if length == 0:
#                 if j == i[-1]:
#                     sum_val += 1
#                 start = j
#                 length = i.count(j) - 1
#             else:
#                 break

# print(sum_val)

print('aaabbsssaa'.split('b'))