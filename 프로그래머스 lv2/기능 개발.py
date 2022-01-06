progresses = [93, 30, 55]
speeds = [1, 30, 5]
# answer = [2, 1]

day = 0  # 날짜
cnt = 0  # 끝난 일 카운트
answer = []

while len(progresses)>0:

   if (progresses[0] + speeds[0]*day) >= 100:
        progresses.pop(0)
        speeds.pop(0)
        cnt += 1
   else:
       if cnt > 0:
           answer.append(cnt)
           cnt = 0

       day += 1

answer.append(cnt)
print(answer)







