#coding:utf-8
'''
	Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
'''
import re, json

def rjson():
	f = open('jawiki-country.json')	#or with open(~) as f:
	g = open('jawiki-uk.txt', 'w')
	target = re.compile(u'イギリス')

	for line in f:
		h = json.loads(line)
		if target.search(h[u'text']):
			g.write(h['text'].encode('utf8') + '\n')

	print 'done.'
	f.close()
	g.close()

if __name__ == "__main__":
	rjson()
