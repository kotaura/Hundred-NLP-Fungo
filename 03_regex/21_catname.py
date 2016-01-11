#coding:utf-8
'''
	記事中でカテゴリ名を宣言している行を抽出せよ．
'''
import re

def catname():
	f = open('jawiki-uk.txt')	#or with open(~) as f:
	g = open('jawiki-uk-category.txt', 'w')

	category = re.compile('\[\[Category:.+\]\]')

	for line in f:
		if category.match(line):
			g.write(line.strip() + '\n')

	f.close()
	g.close()
	print 'done.'

if __name__ == "__main__":
	catname()
