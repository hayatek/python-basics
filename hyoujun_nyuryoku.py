# 1-1.複数行の文字列を単純出力

s = '''/
aaa
bbb
ccc'''

print(s)

# 1-2.文字列半角スペース区切り
# コード例(1)
for item in 'one two three'.split():
    print(item)

# コード例(2)リスト内包表記
[print(item) for item in 'one two three'.split()]

# 3.整数半角スペース区切り
# 入力
i = 123 456 789

# コードの例
l = list(map(int, i.split()))
for item in l:
    print(item)
