#coding:utf-8
'''
	26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ
'''
import re, json, q25_templateext, q26_bremover, q27_linkremover

def wikimarkup(string):
	markups = [
		re.compile(r"\[https?://[a-zA-Z0-9\./]+\s(.+)?\]"),
		re.compile(r"#REDIRECT\s?(.+)"),
		re.compile(r"<!--\s?(.+)\s?-->"),
		re.compile(r"\{\{.*[Ll]ang\|[a-zA-Z\-]+\|(.+)\}\}"),
		re.compile(r"(.*)<ref.+(</ref>)?>"),
		re.compile(r"(.*?)<br\s?/?>"),
		re.compile(r"<[a-z]+.*>(.*?)</[a-z]+>")
	]
	removed_str = q27_linkremover.linkremover(string)
	for markup in markups:
		removed_str = markup.sub(r"\1", removed_str)
	return removed_str

if __name__ == "__main__":
	f = open('jawiki-uk.txt')
	g = open('jawiki-uk-fundamental-markup.json', 'w')
	r = q25_templateext.tplext(f, wikimarkup)
	with open('jawiki-uk-fundamental-markup.json', 'w') as h:
		json.dump(r, h, ensure_ascii=False)
