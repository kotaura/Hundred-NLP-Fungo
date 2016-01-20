#coding:utf-8
'''
	記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
'''
import re

def catext():
	f = open('jawiki-uk.txt')	#or with open(~) as f:
	g = open('jawiki-uk-section.txt', 'w')

	section = re.compile(r'=(=+) (.+) =')

	for line in f:
		l = section.match(line)
		if l:
			g.write("sec%s : " % len(l.group(1)))
			g.write(l.group(2) + "\n")

	f.close()
	g.close()
	print 'done.'

if __name__ == "__main__":
	catext()
