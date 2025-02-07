#coding:utf-8
'''
	スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
'''
from random import shuffle

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(s):
	center = list(s[1:-1])
	shuffle(center)
	return s[0] + ''.join(center) + s[-1]

print(' '.join(typoglycemia(w) if len(w) > 4 else w for w in s.split()))

if __name__ == "__main__":
	typoglycemia
