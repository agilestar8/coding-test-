s = input()
s = sorted(s)
sum = 0
str = ""

for i in s:
    if i.isdigit():
        sum += int(i)
    else:
        str += i

print(str, end = "")
print(sum)

# K1KA5CB7
# AJKDLSI412K4JSJ9D