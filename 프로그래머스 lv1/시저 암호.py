def solution(s, n):
    arr = []

    for i in s:
        if i.isupper():
            arr.append(chr((ord(i)-ord("A")+n)%26 + ord("A")))
        elif i.islower():
            arr.append(chr((ord(i)-ord("a")+n)%26 + ord("a")))
        else:
            arr.append(" ")

    return ("".join(arr))