#bit全探索

#みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。
#財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。


money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    total = 0
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
            total += item[j][1]  # 買い物累計額にも加算
    if (total <= money):
        print(total, bag)



#ABC 079C Train Ticket

n = [int(x) for x in input()]
op_cnt = len(n) - 1  # すき間の個数
for i in range(2 ** op_cnt):
    op = ["-"] * op_cnt  # あらかじめ ["-", "-", "-"] というリストを作っておく
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "+"  # フラグが立っていた箇所を "+" で上書き
    print(op)
