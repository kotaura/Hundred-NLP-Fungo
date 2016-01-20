#coding:utf-8
'''
	記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
'''
import re, json

def passstr(string):
	return string

def tplext(file, func):
	res = []
	data = {}
	flag = False
	key = None
	start = re.compile(r'\{\{基礎情報')
	end = re.compile(r'\}\}')
	row = re.compile(r'^\s?\|?\s?(.+?)\s?=(.*)\|?')

	for line in file:
		if start.match(line):
			flag = True
			continue
		if end.match(line):
			flag = False

		if flag:
			l = row.match(line)
			if l:
				data[l.group(1).strip()] = func(l.group(2).strip())
				key = l.group(1).strip()
			else:
				m = re.match(r'(.*)\}\}$', line)
				if m:
					data[key] += func(m.group(1).strip())
					flag = False
				else:
					data[key] += func(line.strip())
		else:
			if len(data) > 0:
				res.append(data.copy())
				data.clear()

	print 'done.'
	return res

if __name__ == "__main__":
	f = open('jawiki-uk.txt')
	g = open('jawiki-uk-tpl.json', 'w')
	r = tplext(f, passstr)
	with open('jawiki-uk-tpl.json', 'w') as h:
		json.dump(r, h, ensure_ascii=False)
