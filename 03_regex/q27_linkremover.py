#coding:utf-8
'''
	26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ
'''
import re, json, q25_templateext, q26_bremover

def linkremover(string):
	internallink = re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")
	bremoved = q26_bremover.bremover(string)
	return internallink.sub(r"\3", bremoved)

if __name__ == "__main__":
	f = open('jawiki-uk.txt')
	g = open('jawiki-uk-fundamental-nostrong-nointernallink.json', 'w')
	r = q25_templateext.tplext(f, linkremover)
	with open('jawiki-uk-fundamental-nostrong-nointernallink.json', 'w') as h:
		json.dump(r, h, ensure_ascii=False)
