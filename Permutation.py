#順列全探索


import itertools

n = int(input())
lis = [x for x in range(n)] # 0からn-1までのリスト

permutations_lis=itertools.permutations(lis)# 全ての場合のリストを生成

for one_case in permutations_lis:  #タプルを外す
	for num in one_case:
		print(num, end=" ")
	print("")

#入力：3

#出力：0 1 2
#     0 2 1
#     1 0 2
#     1 2 0
#     2 0 1
#     2 1 0
