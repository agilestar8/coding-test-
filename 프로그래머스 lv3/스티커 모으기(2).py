def solution(sticker):
    n = len(sticker)
    
    # 스티커 1개일 때
    if n == 1: 
        return sticker[0]

    # 2가지 DP, 각 경우의 최대값을 저장하면서 진행
    dp = [[0 for _ in range(n)] for _ in range(2)]

    # case1.첫번째 스티커를 뗀 경우(맨 뒤 고려)
    dp[0][0] = sticker[0] 
    dp[0][1] = sticker[0] 
    
     # case2.첫번째 안떼고, 두번째 스티커를 뗀 경우    
    dp[1][1] = sticker[1]
    print(dp)
    
    # case1
    for i in range(2, n-1): 
        # 2번 전까지의 최대값 + 현재자신 vs 1번 전까지 최대값 비교
        dp[0][i] = max(dp[0][i-2] + sticker[i], dp[0][i-1])

    # case2
    for i in range(2, n): 
        # 2번전까지의 최대값 + 현재자신 vs 1번전까지 최대값 비교
        dp[1][i] = max(dp[1][i-2] + sticker[i], dp[1][i-1])
    
    # case1는 맨뒤 안씀, case2는 맨뒤까지
    answer = max(dp[0][n-2], dp[1][n-1])
    
    return answer