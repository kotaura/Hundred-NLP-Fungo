#coding:utf-8
'''
	25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
'''
import re, json, q25_templateext

def bremover(string):
	strong = re.compile(r"''('*)(.+)''\1")
	return strong.sub(r"\2", string)

if __name__ == "__main__":
	f = open('jawiki-uk.txt')
	g = open('jawiki-uk-fundamental-nostrong.json', 'w')
	r = q25_templateext.tplext(f, bremover)
	with open('jawiki-uk-fundamental-nostrong.json', 'w') as h:
		json.dump(r, h, ensure_ascii=False)
