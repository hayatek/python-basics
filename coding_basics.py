#改行は\n、タブは\t
#split():はスペースと改行とタブが複数あってもそこで分割される
#s = "one two  three   \nfour \t"
#print(s.split())
#one
#two
#three
#four
#strip()は両端の空白やタブを削除する

#input_s = "   200         300   "
#str = input_s.strip()
#print(str)
#200 300

#受け取った文字列を整数に変換する(list,map,int)
input_s = "200 300"
#lst = list(map(int, input_s.split()))
lst = map(int, input_s.split())
print(lst)
