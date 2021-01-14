S1 = int(input("Из какой системы? (2, 8, 10, 16) --> "))
# Проверка на 2, 8, 10, 16
while True:
    if S1 == 2 or S1 == 8 or S1 == 10 or S1 == 16:
        break
    else:
        S1 = int(input("Ошибка, введите еще раз --> "))

S2 = int(input("В какую систему? (2, 8, 10, 16) --> "))
# Проверка на 2, 8, 10, 16
while True:
    if S2 == 2 or S2 == 8 or S2 == 10 or S2 == 16:
        break
    else:
        S2 = int(input("Ошибка, введите еще раз --> "))


# Проверки
def Proverka2(tt):
    for s in tt:
        b = True
        if s != '0' and s != '1':
            b = False
    return b


def Proverka8(tt):
    for s in tt:
        b = True
        if not (s >= '0' and s <= '7'):
            b = False
    return b


def Proverka10(tt):
    for s in tt:
        b = True
        if not (s >= '0' and s <= '9'):
            b = False
    return b


def Proverka16(tt):
    for s in tt:
        b = True
        if not ((s >= '0' and s <= '9') or (s >= 'A' and s <= 'F') or (s >= 'a' and s <= 'f')):
            b = False
    return b


# Переводы
def Perevod_10_2(tt):
    n10 = int(tt)
    t2 = ""
    while n10 > 0:
        ostatok = n10 % 2
        t2 = str(ostatok) + t2
        n10 = n10 // 2
    return t2


def Perevod_2_10(tt):
    n10 = 0
    for s in tt:
        k = int(s)
        n10 = n10 * 2 + k
    return str(n10)

def Perevod_10_8(tt):
    num = int(tt)
    base = 8
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum


def Perevod_8_10(tt):
    n10 = 0
    for s in tt:
        k = int(s)
        n10 = n10 * 8 + k
    return str(n10)


def Perevod_16_10(tt):
    n10 = 0
    for s in tt:
        if s >= '0' and s <= '9':
            k = int(s)
        elif s >= 'A' and s <= 'F':
            k = ord(s) - ord('A') + 10
        else:
            k = ord(s) - ord('a') + 10
        n10 = n10 * 16 + k
    return n10


def Perevod_10_16(tt):
    n10 = int(tt)
    n = n10
    t16 = ""
    while n > 0:
        ostatok = n % 16
        if ostatok < 10:
            s = str(ostatok)
        else:
            s = chr(ord("A") + ostatok - 10)
        t16 = s + t16
        n = n // 16
    return t16


def Perevod_2_8(tt):
    d = Perevod_2_10(tt)
    g = Perevod_10_8(d)
    return g


def Perevod_2_16(tt):
    d = Perevod_2_10(tt)
    g = Perevod_10_16(d)
    return g


def Perevod_8_2(tt):
    d = Perevod_8_10(tt)
    g = Perevod_10_2(d)
    return g


def Perevod_8_16(tt):
    d = Perevod_8_10(tt)
    g = Perevod_10_16(d)
    return g


def Perevod_16_2(tt):
    d = Perevod_16_10(tt)
    g = Perevod_10_2(d)
    return g


def Perevod_16_8(tt):
    d = Perevod_16_10(tt)
    g = Perevod_10_8(d)
    return g

y = True
while y:
    t = input("Введите исходное число --> ")
    # Проверка числа t
    if S1 == 2:
        b = Proverka2(t)
    elif S1 == 8:
        b = Proverka8(t)
    elif S1 == 10:
        b = Proverka10(t)
    elif S1 == 16:
        b = Proverka16(t)

    if b is True:
        y = False
    else:
        print("Ошибка! В следущий раз введите нормальное число!")

# Перевод числа
if S1 == 2 and S2 == 10:
    rez = Perevod_2_10(t)
elif S1 == 10 and S2 == 2:
    rez = Perevod_10_2(t)
elif S1 == 8 and S2 == 10:
    rez = Perevod_8_10(t)
elif S1 == 10 and S2 == 8:
    rez = Perevod_10_8(t)
elif S1 == 16 and S2 == 10:
    rez = Perevod_16_10(t)
elif S1 == 10 and S2 == 16:
    rez = Perevod_10_16(t)
elif S1 == 2 and S2 == 8:
    rez = Perevod_2_8(t)
elif S1 == 2 and S2 == 16:
    rez = Perevod_2_16(t)
elif S1 == 8 and S2 == 2:
    rez = Perevod_8_2(t)
elif S1 == 8 and S2 == 16:
    rez = Perevod_8_16(t)
elif S1 == 16 and S2 == 2:
    rez = Perevod_16_2(t)
elif S1 == 16 and S2 == 8:
    rez = Perevod_16_8(t)

if b is True:
    print(t, "-->", rez)
