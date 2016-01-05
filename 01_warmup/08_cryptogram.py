#coding:utf-8
'''
	与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

	英小文字ならば(219 - 文字コード)の文字に置換
	その他の文字はそのまま出力
	この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''
import sys

def cipher(s='HelloWorld!'):
	if len(sys.argv) > 1: s = sys.argv[1]
	ss = [s[i] for i in range(len(s))]
	cs = [chr(219 - ord(c)) if 'a'<=c<='z' else c for c in ss]
	print ((str(''.join(ss))) + ' has been encrypted to ' + str(''.join(cs)))

if __name__ == "__main__":
	cipher()
