# 入力文字列を整数に変換してリストに格納してHとWを取得
H, W = list(map(int, input().split()))
print('H=', H)
print('W=', W)

# Checkフラグ
isCheckTrue = False

# 各行を配列に格納
mainList = []
for _ in range(H):
    mainList.append(list(input()))
# print('mainList=',mainList)


# 配列をループで回す

for i in range(H):
    for j in range(W):
        print('mainList[i][j]=', mainList[i][j])
        if i == 0 and j == 0:
            if mainList[0][1] == '#' and mainList[1][0] == '#':
                print(str(i) + ' ' + str(j))
        if i == 0 and j != 0:
            if mainList[0][i-1] == '#' and mainList[0][i+1] == '#' and mainList[1][i] == '#':
                print(str(i) + ' ' + str(j))

# #一番上の判定ロジック
# if mainList[0][i-1] == '#' and mainList[0][i+1] == '#' and mainList[1][i] == '#':
#     isCheckTrue = True


# #上左端の判定
# if mainList[0][1] == '#' and mainList[1][0] == '#':
#     isCheckTrue = True

# #上右端の判定
# if mainList[0][W-1] == '#' and mainList[1][W] == '#':
#     isCheckTrue = True

# #下左端の判定
# if mainList[H-1][0] == '#' and mainList[H][1] == '#':
#     isCheckTrue = True

# #下右端の判定
# if mainList[H][W-1] == '#' and mainList[H-1][W] == '#':
#     isCheckTrue = True
