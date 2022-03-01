# 1~16진수까지 가능한 진수 변환
def ConvToK(number,base):
    t = "0123456789ABCDEF" # 0~F까지 16개 문자열
    q,r = divmod(number,base)
    return ConvToK(q,base) + t[r] if q else t[r]

# 10진수 123 --> 3진수 11120
print(ConvToK(123,3))

    
