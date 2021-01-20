#オイラー関数
#正の整数 N が与えられたとき、1,2,…,N のうち N と互いに素であるものの個数を
#φ(N)と表します。これをオイラー関数とよびます。

#【互いに素】

#2 つの整数 a,b が互いに素であるとは、以下の条件を満たすような整数 d が存在しないことをいう:

#d>1
#a は d で割り切れる
#b は d で割り切れる


#a=6,b=8のとき、a も b も 2 で割り切れるので、a,b は互いに素ではありません
#a=6,b=11のとき、これらをともに割り切る正の整数は 1 しかないので、a,b は互いに素です
#言い換えれば、a と b の「最大公約数が 1」ということです。


#順番に試す。＊遅い
n=int(input())

lst=[]
c=0
ans=0
for i in range(2,n):
	for j in range(2,n):
		if n%j==0 and i%j==0:
			c+=1
	if c==0:
		ans+=1
	c=0
print(ans+1)



#最大公約数を利用
from math import gcd

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


#高速化
n=m=int(input())
i=2
while i*i<=n:
    if n%i==0:
        m=m*(1-1/i)
        while n%i==0: 
            n//=i
    i+=1
if n!=1:
    m=m*(1-1/n)
print(round(m))
