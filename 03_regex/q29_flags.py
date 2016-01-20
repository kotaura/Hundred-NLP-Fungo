#coding:utf-8
'''
	26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ
'''
import requests, json

print 'parsing start...'

with open('jawiki-uk-fundamental-markup.json') as f:
	template = json.load(f)
g = open('jawiki-uk-flags.txt', 'w')

wiki_api = "http://ja.wikipedia.org/w/api.php?"

prop = {
	'action': "query",
	'prop': "imageinfo",
	'iiprop': "url",
	'format': "json",
	'formatversion': '2',
	'utf8': '',
	'continue': ''
}

for country in template:
	if u'国旗画像' in country:
		countryname = country[u'略名']
		filename = country[u'国旗画像']
		prop['titles'] = "Image:" + filename
		r = requests.get(url=wiki_api, params=prop)
		d = json.loads(r.text)
		try:
			file_url = d['query']['pages'][0]['imageinfo'][0]['url']
		except:
			print(d)
			break
		print(filename, file_url)
		g.write(countryname.encode('utf8').replace('|', ''))
		g.write(', %s\n' %file_url)
g.close()
print 'done.'
