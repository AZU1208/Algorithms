#最小公倍数

import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)


#3つ以上の最小公倍数

def gcd(a,b):
	if a < b:
		a, b = b, a
	while a % b != 0:
		a, b = b, a % b
	return b

def lcm(a,b):
    return a*b//gcd(a,b)

n=int(input())
a=list(map(int,input().split()))
b=1
for i in a:
	b=lcm(b,i) #1つ１つ最小公倍数を求めていく。
print(b)

#入力: 3               出力：12
#     3 4 6 

