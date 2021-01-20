#二項係数

def nCk(n, k, p):
    denominator,numerator =1,1
    for i in range(1,k+1):
        numerator  = numerator*(n-i+1)
        denominator  = denominator*i 
    return numerator/denominator


#二項係数高速化(逆元)
    

def nCk(n, k, p):
    denominator,numerator =1,1
    for i in range(1,k+1):
        numerator  = (numerator*(n-i+1))%p
        denominator  = (denominator *i)%p 
    return (numerator * pow(denominator , p - 2, p)) % p



   
#factorialを使用する場合
#p = n! / (n - r)!

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)
