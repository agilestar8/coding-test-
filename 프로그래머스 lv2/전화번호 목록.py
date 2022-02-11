phone_book = ["119", "97674223", "1195524421"]	

# 만약에 어떤 번호가 다른 번호의 접두어라면 이 둘은 정렬했을 때 앞뒤에 위치하게 된다.
# 예를 들어 ["1235", "123", "12348", "012"]을 입력으로 받으면, 
# 정렬 시 ["012", "123", "12348", "1235"]가 된다.

def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        # if phone_book[i] in phone_book[i+1]: # 이것은 문자 중간에 접두사가 포함되도 만족하므로 틀림
        
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:  # 문자열 앞에서 접두사 길이만큼만 같아야함
          return False

    return True

