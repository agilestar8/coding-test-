numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] # 누를 번호
hand = "right" # 자주 쓰는 손
answer = ""

keypad = [[1,2,3],
          [4,5,6],
          [7,8,9],
          ["*",0,"#"]]

x1,y1 = 3,0 # 왼손 좌표
x2,y2 = 3,2 # 오른손 좌표
x3,y3 = 0,1 # 가운데 기준 좌표

for i in numbers:

    if i in [1,4,7,"*"]:
        answer += "L"
        if i == 1:
            x1,y1 = 0,0
        elif i == 4:
            x1,y1 = 1,0
        elif i == 7:
            x1,y1 = 2,0
        elif i == "*":
            x1,y1 = 3,0

    elif i in [3,6,9,"#"]:
        answer += "R"
        if i == 3:
            x2,y2 = 0,2
        elif i == 6:
            x2,y2 = 1,2
        elif i == 9:
            x2,y2 = 2,2
        elif i == "#":
            x2,y2 = 3,2

    elif i in [2,5,8,0]:
        if i == 2:
            x3,y3 = 0,1
            left_d = abs(x1 - x3) + abs(y1 - y3)
            right_d = abs(x2 - x3) + abs(y2 - y3)

            if left_d < right_d:
                answer += "L"
                x1,y1 = x3,y3
            elif left_d > right_d:
                answer += "R"
                x2,y2 = x3,y3
            elif left_d == right_d:
                if hand == "right":
                    answer += "R"
                    x2, y2 = x3,y3
                else:
                    answer += "L"
                    x1, y1 = x3,y3
                    
        if i == 5:
            x3,y3 = 1,1
            left_d = abs(x1 - x3) + abs(y1 - y3)
            right_d = abs(x2 - x3) + abs(y2 - y3)

            if left_d < right_d:
                answer += "L"
                x1,y1 = x3,y3
            elif left_d > right_d:
                answer += "R"
                x2,y2 = x3,y3
            elif left_d == right_d:
                if hand == "right":
                    answer += "R"
                    x2, y2 = x3,y3
                else:
                    answer += "L"
                    x1, y1 = x3,y3

        if i == 8:
            x3,y3 = 2,1
            left_d = abs(x1 - x3) + abs(y1 - y3)
            right_d = abs(x2 - x3) + abs(y2 - y3)
            if left_d < right_d:
                answer += "L"
                x1,y1 = x3,y3
            elif left_d > right_d:
                answer += "R"
                x2,y2 = x3,y3
            elif left_d == right_d:
                if hand == "right":
                    answer += "R"
                    x2, y2 = x3,y3
                else:
                    answer += "L"
                    x1, y1 = x3,y3

        if i == 0:
            x3,y3 = 3,1
            left_d = abs(x1 - x3) + abs(y1 - y3)
            right_d = abs(x2 - x3) + abs(y2 - y3)
            if left_d < right_d:
                answer += "L"
                x1,y1 = x3,y3
            elif left_d > right_d:
                answer += "R"
                x2,y2 = x3,y3
            elif left_d == right_d:
                if hand == "right":
                    answer += "R"
                    x2, y2 = x3,y3
                else:
                    answer += "L"
                    x1, y1 = x3,y3

print(answer)






