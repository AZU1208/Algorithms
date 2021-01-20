#素数判定
#引数nが素数かどうかを判定

#正の整数 N が、2 以上 √N 以下の整数で割り切れないならば、
#√N 以上 N−1 以下の整数で割り切れることもない

#i*i<=nという部分が、√N 以下の整数まで試すことを表している。

def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True
