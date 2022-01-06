# def solution1(s):
#     answer = True
#     p = 0
#     y = 0
#
#     for i in s:
#         if i == 'p' or i == 'P':
#             p += 1
#         elif i == 'y' or i == "Y":
#             y += 1
#
#     if p == 0 and y == 0:
#         answer = False
#     elif p != y:
#         answer = False
#
#     return answer

def solution2(s):
    answer = True

    if s.lower().count('p') == s.lower().count('y'):
        answer = True
    else:
        answer = False

    return answer