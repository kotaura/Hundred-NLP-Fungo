#coding:utf-8
'''
	引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
'''
import sys

def generator(x=12, y='気温', z=22.4):
	argv = sys.argv
	if len(argv) == 2:
		x = str(argv[1])
	elif len(argv) == 3:
		x = str(argv[1])
		y = str(argv[2])
	elif len(argv) == 4:
		x = str(argv[1])
		y = str(argv[2])
		z = str(argv[3])
	else:
		print 'Input words must be lower than 3. I will print default.'
		pass
	print (str(x) + '時の' + y + 'は' + str(z))

if __name__ == "__main__":
	generator()
