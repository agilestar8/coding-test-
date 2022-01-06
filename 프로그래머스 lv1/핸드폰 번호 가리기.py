def solution(phone_number):
    a = phone_number[:-4]
    b = phone_number[-4:]
    return "*" * len(a) + b