def solution(s):
    text = s.split(" ")
    arr = []
    for word in range(len(text)):
        for idx in range(len(text[word])):
            if idx % 2 == 0:
                # 대문자
                a = text[word][idx].upper()
                arr.append(a)

            else:
                # 소문자
                b = text[word][idx].lower()
                arr.append(b)
        arr.append(".")

    arr = "".join(arr)
    arr = arr.replace(".", " ")

    return arr[:len(arr) - 1]
