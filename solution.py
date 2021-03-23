# def solution(list):
#     old_len = len(list)
#     list = [x for x in list if x != 0]
#     if len(list) == 1 and list[0] < 0 and old_len > 1:
#         print(0)
#         return
#     n = len([x for x in list if x < 0])
#     if (n % 2 != 0 and len(list) > 1):
#         mx = max([n for n in list if n < 0])
#         # list = [x for x in list if x != mx]
#         for i, x in enumerate(list):
#             if x == mx:
#                 del(list[i])
#                 break
#     res = 0
#     if len(list) > 0:
#         res = 1
#         for x in list:
#             res = res * x
#     print(res)


# list = [-5]
# solution(list)

# def solution(l):
#     # Your code here
#     # l.sort()
#     l.sort(key=lambda s: list(map(int, s.split('.'))))
#     print(','.join(map(str, l)))


# l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
# solution(l)

print()
