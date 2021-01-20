#しゃくとり法

#長さnの数列 a1,a2,…,an において

#「条件」を満たす区間 (連続する部分列) のうち、最小の長さを求めよ
#「条件」を満たす区間 (連続する部分列) のうち、最大の長さを求めよ
#「条件」を満たす区間 (連続する部分列) を数え上げよ

#に使用できる。


#例題: Atcoder ABC032


n,k = map(int,input().split())
s = [int(input()) for i in range(n)]

if 0 in s:
    print(n)
else:
    r, ans, tmp = 0, 0, 1
    for l in range(n):
        while r < n and tmp*s[r] <= k:
            tmp *= s[r]
            r += 1
        ans = max(ans,r-l)
        if l == r:
            r += 1
        else:
            tmp //= s[l]
    print(ans)
