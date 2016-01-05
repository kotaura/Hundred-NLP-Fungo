#coding:utf-8
'''
	与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
'''
def ngram():
	s = 'I am an NLPer'
	#Character Bi-Gram
	charBiGram = [s[i:i+2] for i in range(len(s) - 1)]
	#Word Bi-Gram
	words = [word.strip(",.") for word in s.split()]
	wordBiGram = ["-".join(words[i:i+2]) for i in range(len(words) - 1)]

	print charBiGram
	print wordBiGram

if __name__ == "__main__":
	ngram()
