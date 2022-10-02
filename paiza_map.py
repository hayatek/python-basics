# 入力文字列を整数に変換してリストに格納してHとWを取得

mainList = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '.', '#', '.', '#', '.', '#', '.', '#', '.'],
            ['.', '#', '.', '#', '.', '#', '.', '#', '.', '#'],
            ['#', '.', '#', '.', '#', '.', '#', '.', '#', '.'],
            ['.', '#', '.', '#', '.', '#', '.', '#', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            ]

H = 10
W = 10

# H, W = list(map(int, input().split()))
print('H=', H)
print('W=', W)

# Checkフラグ
isCheckTrue = False

# 各行を配列に格納
# mainList = []
# for _ in range(H):
#     mainList.append(list(input()))
# print('mainList=',mainList)

# 最終行
maxRow = int(H) - 1

# 最終列
maxCol = int(W) - 1

print('maxRow=', maxRow)
print('maxCol=', maxCol)


# 配列をループで回す


for i in range(H):
    for j in range(W):
        # 一番上の行
        if i == 0:
            # 左端の判定
            if j == 0:
                if mainList[i][j+1] == '#' and mainList[i+1][j] == '#':
                    print(str(i) + ' ' + str(j))
            # 右端の判定
            elif j == maxCol:
                if mainList[i][j-1] == '#' and mainList[i+1][j] == '#':
                    print(str(i) + ' ' + str(j))
            # 左端/右端以外の判定
            else:
                if mainList[i][j-1] == '#' and mainList[i][j+1] == '#' and mainList[i+1][j] == '#':
                    print(str(i) + ' ' + str(j))

        # 一番下の行
        elif i == maxRow:
            # 左端の判定
            if j == 0:
                if mainList[i-1][j] == '#' and mainList[i][j+1] == '#':
                    print(str(i) + ' ' + str(j))
            # 右端の判定
            elif j == maxCol:
                if mainList[i][j-1] == '#' and mainList[i-1][j] == '#':
                    print(str(i) + ' ' + str(j))
            # 左端/右端以外の判定
            else:
                if mainList[i][j-1] == '#' and mainList[i][j+1] == '#' and mainList[i-1][j] == '#':
                    print(str(i) + ' ' + str(j))
         # 中間の行
        else:
            # 左端の判定
            if j == 0:
                if mainList[i][j+1] == '#' and mainList[i+1][j] == '#' and mainList[i-1][j] == '#':
                    print(str(i) + ' ' + str(j))
            # 右端の判定
            elif j == maxCol:
                if mainList[i][j-1] == '#' and mainList[i+1][j] == '#' and mainList[i-1][j] == '#':
                    print(str(i) + ' ' + str(j))
            # 左端/右端以外の判定
            else:
                if mainList[i-1][j] == '#' and mainList[i+1][j] == '#' and mainList[i][j-1] == '#' and mainList[i][j+1] == '#':
                    print(str(i) + ' ' + str(j))

# 模範解答

# h, w = map(int, input().split())
# s = [list(input()) for _ in range(h)]

# for y in range(h):
#     for x in range(w):
#         flag_row = False
#         flag_column = False

#         if x == 0 or s[y][x - 1] == "#":
#             if x == w - 1 or s[y][x + 1] == "#":
#                 flag_row = True

#         if y == 0 or s[y - 1][x] == "#":
#             if y == h - 1 or s[y + 1][x] == "#":
#                 flag_column = True

#         if flag_column and flag_row:
#             print(y, x)
