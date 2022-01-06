# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는다.

# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
n,m = map(int,input().split())
card_num = list(map(int,input().split()))
arr = []

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if (card_num[i]+card_num[j]+card_num[k]) <= m:
                arr.append(card_num[i]+card_num[j]+card_num[k])

print(max(arr))
