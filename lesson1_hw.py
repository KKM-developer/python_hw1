import math
#задача 1
day = int(input('Введите день '))
if 1<=day<= 5:
    print('NO')
elif 6<= day<=7:
    print('YES')
else:
    print('in week only 7 days')

#задача 2
def CheckArg(bool1, bool2, bool3):
    if not (bool1 or bool2 or bool3) == (not bool1 and not bool2 and not bool3):
        print(f'X={bool1}|y={bool2}|z={bool3}|{True}')

x = [True, False]
y = [True, False]
z = [True, False]
for i in x:
    for j in y:
        for h in z:
            CheckArg(i, j, h)

#задача 3
def CheckQ (numb1, numb2):
    print('I') if numb1>0 and numb2>0 else 0
    print('II') if numb1 < 0 and numb2 > 0 else 0
    print('III') if numb1 < 0 and numb2 < 0 else 0
    print('IV') if numb1 > 0 and numb2 < 0 else 0

x = int(input('Введите Х: '))
y = int(input('Введите Y: '))
CheckQ(x, y)

#задача 4
def CheckP (numb):
    print('X>0|Y>0') if numb==1 else 0
    print('X<0|Y>0') if numb==2 else 0
    print('X<0|Y<0') if numb==3 else 0
    print('X>0|Y<0') if numb==4 else 0
p = int(input('Введите номер четвери: '))
CheckP(p)

#задача 5
aX = int(input('Введите координату X первой точки: '))
aY = int(input('Введите координату Y первой точки: '))
bX = int(input('Введите координату X второй точки: '))
bY = int(input('Введите координату Y второй точки: '))
print(f'Расстояние между точками A[{aX}, {aY}] и В[{bX}, {bY}] = {round(math.sqrt((bX-aX)**2+(bY-aY)**2), 2)}')