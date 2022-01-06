# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import sys
from collections import Counter
  
t = int(sys.stdin.readline())
num_list = []
for _ in range(t):
    num_list.append(int(sys.stdin.readline())) 

def mode(x):
    mode_dict = Counter(x)
    modes = mode_dict.most_common()
    if len(x) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]
    
    return mod

print(round(sum(num_list) / len(num_list)))
num_list.sort()
print(num_list[len(num_list) // 2])
print(mode(num_list))
print(num_list[-1] - num_list[0])