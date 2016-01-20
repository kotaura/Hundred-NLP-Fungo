#coding:utf-8
'''
	記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
'''
import re

def catext():
	f = open('jawiki-uk.txt')	#or with open(~) as f:
	g = open('jawiki-uk-category-name.txt', 'w')

	category = re.compile('\[\[Category:(.+)\]\]')

	for line in f:
		l = category.match(line)
		if l:
			g.write(l.group(1) + '\n')

	f.close()
	g.close()
	print 'done.'

if __name__ == "__main__":
	catext()
