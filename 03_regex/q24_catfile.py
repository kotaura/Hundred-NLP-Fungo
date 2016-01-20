#coding:utf-8
'''
	記事から参照されているメディアファイルをすべて抜き出せ．
'''
import re

def catext():
	f = open('jawiki-uk.txt')	#or with open(~) as f:
	g = open('jawiki-uk-media.txt', 'w')

	media = re.compile(r".*(ファイル|File|file):(.*\.[a-zA-Z0-9]+)\|.*")

	for line in f:
		l = media.match(line)
		if l:
			g.write(l.group(2) + "\n")

	f.close()
	g.close()
	print 'done.'

if __name__ == "__main__":
	catext()
