#coding:utf-8
'''
	「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''
def patokatakushi():
	s1 = u'パトカー'
	s2 = u'タクシー'
	s3 = u''
	for i, j in zip(s1, s2):
		s3 = s3 + i + j
	print s3

if __name__ == "__main__":
	patokatakushi()
