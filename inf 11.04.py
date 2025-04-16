# упражнение 1
import numpy as np
a = input()
lst = a.split("student_")
lst1 = []
fl = 1
for i in range(1, len(lst)):
    lst1.append(int(lst[i]) % 100)
print(int(lst[lst1.index(max(lst1)) + 1]) // 100)


# упражнение 2
r, a = map(int, input().split())
l = np.pi * 2 * r
S1 = np.pi * (r ** 2)
S2 = a ** 2
q = (S1 / S2) * 100
print("Длина окружности равно", round(l, 2), end="")
print(". Площадь круга составляет", round(q, 2), end="")
print("% от площади квадрата.")


# упражнение 3
a, b = map(str, input().split())
a, b = list(a), list(b)
a[0], a[1] = a[1], a[0]
b[0], b[1] = b[1], b[0]
print("".join(a), "".join(b), sep="-")


# упражнение 4
a = input()
k = 0
l = 0
if len(a) < 4:
    for i in range(len(a)):
        if a[i].istitle() == True:
            l += 1
    if l == len(a):
        print(a)
    else:
        print(a, "Не все заглавные")
else:
    for i in range(3):
        if a[i].istitle() == True:
            k += 1
    if k >= 3:
        print(a.upper())
    else:
        print(a)

#упражнение 5
def wrap_in_tag(text, tag):
    valid_tags = ['a', 'abbr', 'b', 'body', 'caption', 'cite', 'code',
                 'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                 'header', 'i', 's']
    
    if tag.lower() in valid_tags:
        return f"<{tag}>{text}</{tag}>"
    else:
        return "Введён неверный тег"
    
tag = input()
text = input()
print(wrap_in_tag(text, tag))


#упражнение 6
a = input()
if len(a) <= 2:
    print(ord(a[0]))
if len(a) > 2 and len(a) < 10:
    if len(a) % 2 == 0:
        medium = len(a) // 2 - 1
    else:
        medium = len(a) // 2
    print(ord(a[0]) + ord(a[medium]) + ord(a[-1]))

if len(a) > 10:
    print(ord(a[-1]))