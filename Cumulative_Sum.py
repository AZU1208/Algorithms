#累積和

#累積和：「配列Aの第1項から第N項までの部分列の和」を第N項とする配列Bを累積和といいます。
        #(よって累積和も配列です)
#例えば、配列[a, b, c, …]の累積和は[a, a+b, a+b+c, …]です。


#配列 a0,a1,a2,…,aN−1a0,a1,a2,…,aN−1 に対して
#配列 s0,s1,s2,…,sN−1,sNs0,s1,s2,…,sN−1,sN を以下のように定めたもの
#s0=0
#s1=a0
#s2=a0+a1
#s3=a0+a1+a2
#sN=a0+a1+a2+⋯+aN−1です。


#例えば a={3,6,8,23,6,8,2} であれば、s={0,3,9,17,190,3,9,17,19} です。
#sの方がaよりも1だけ配列サイズが大きくなっています。
#これを用いると、例えば配列 aの区間 (4,13) の総和
#a4+a5+a6+a7+a8+a9+a10+a11+a12a4+a5+a6+a7+a8+a9+a10+a11+a12
#はs13−s4s13−s4を計算するだけで求めることができます


def cumsum(xs):
  result = [xs[0]]
  for x in xs[1:]:
    result.append(result[-1] + x)
  return result

#numpyを使用した場合

import numpy
numpy.cumsum(numpy.array(xs))
