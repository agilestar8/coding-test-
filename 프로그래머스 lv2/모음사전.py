from itertools import product
    
def solution(word):
    arr = ["A","E","I","O","U"]
    dictionary = []

    for i in range(1,6): # 1자리부터 5자리까지
        # dictionary += list(map(''.join, permutations("AEIOU", i)))   # 순열은 AA,AAA, EE같은 경우는 포함안함
        # dictionary += list(map(''.join, product("AEIOU", repeat = i))) # 모든 경우 포함한 경우의 수

        # 리스트에 여러개 추가 : extend
        dictionary.extend(list(map(''.join, product(arr, repeat = i))))
            
    dictionary.sort() # 사전 순 정렬

    # 단어가 사전에서 몇 번째에 있는지 구하기
    answer = dictionary.index(word) + 1

    return (answer)
