
number = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
c= []
for i in range(len(number) - 1):
    n = number[i]
    i += 1
    m = number[i]
    if m > n:
        c.append(m)
print(c)
