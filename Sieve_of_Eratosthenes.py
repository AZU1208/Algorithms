#エラトステネスの篩

#ステップ 1: 探索リストに2からxまでの整数を昇順で入れる。
#ステップ 2: 探索リストの先頭の数を素数リストに移動し、その倍数を探索リストから篩い落とす。
#ステップ 3: 上記の篩い落とし操作を探索リストの先頭値がxの平方根に達するまで行う。
#ステップ 4: 探索リストに残った数を素数リストに移動して処理終了。

def prime_eratosthenes(n):
   prime_list = []
   num_list=[]
   for i in range(2, n+1):
       if i not in num_list:
           prime_list.append(i)
           for j in range(i*i, n+1, i):
               num_list.append(j)
   print(prime_list)



#Numpyを使用した場合

import numpy as np

def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum
