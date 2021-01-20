#最大公約数

#①gcd関数を使うパターン
import math

a = 6
b = 4

print(math.gcd(a, b))
# 2


#②gcd関数を作るパターン
def gcd(x, y):    
    x_list = []
    y_list = []
    
    cnt = 1
    while x > cnt :
        if x % cnt == 0:
            x_list.append(cnt)
        cnt += 1

    cnt = 1
    while y > cnt:
        if y % cnt == 0:
            y_list.append(cnt)
        cnt += 1

    cnt_x, cnt_y = 0, 0
    gcd_list = []
    for t_x in x_list:
        for  t_y in y_list:
            if t_x == t_y:
                gcd_list.append(t_y)

    return max(gcd_list)


#③ユークリッドの互除法
#自然数 a,b(a≥b)に対し aを bで割ったあまりを rとすると、次の式が成り立つ。
#gcd(a,b)=gcd(b,r)

a, b = map(int, input().split())
if a < b:
    a, b = b, a
while a % b != 0:
    a, b = b, a % b
print(b)

#（割る数）÷（余り）」を繰り返すと、最後は必ず余りが0になり、
#そのときの割る数が最大公約数になります。


