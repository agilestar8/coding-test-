# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]

d = {}
for t in tickets:
    d[t[0]] = d.get(t[0], []) + [t[1]]
# print(d)

for r in d:
    d[r].sort(reverse = True)
print(d)

stack = ["ICN"]
path = []

while len(stack) > 0:
    top = stack[-1]
    if top not in d or len(d[top]) == 0: #
        path.append(stack.pop()) # 경로에 추가
    else:
        stack.append(d[top][-1]) # 정렬순서대로 먼저 가기
        d[top] = d[top][:-1] # 사전에서 pop

    print(stack)
    print(path)

print(path[::-1])
