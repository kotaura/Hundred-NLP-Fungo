#coding:utf-8
'''
	タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''

def spacereplace():
	f = open('hightemp.txt')
	print (f.read().replace('\t', ' '))
	f.close()

if __name__ == "__main__":
	spacereplace()

# On terminal
# sed 's/\t/ /g' hightemp.txt
