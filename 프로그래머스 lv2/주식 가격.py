from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        cnt = 0
        now_price = prices.popleft()
        for i in prices:
            if now_price <= i:
                cnt += 1
            else:
                cnt += 1
                break

        answer.append(cnt)

    return answer