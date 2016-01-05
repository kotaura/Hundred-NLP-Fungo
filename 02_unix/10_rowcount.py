#coding:utf-8
'''
	行数をカウントせよ．確認にはwcコマンドを用いよ．
'''

def row():
	f = open('hightemp.txt')
	print len(f.readlines())
	f.close()

if __name__ == "__main__":
	row()

# On terminal
# wc -l hightemp.txt
