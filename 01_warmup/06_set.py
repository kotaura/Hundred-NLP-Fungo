#coding:utf-8
'''
	"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''
def xyset():
	s1 = 'paraparaparadise'
	s2 = 'paragraph'

	x = set([s1[i:i+2] for i in range(len(s1) - 1)])
	y = set([s2[i:i+2] for i in range(len(s2) - 1)])
	print 'X = ' + str(x)
	print 'Y = ' + str(y)
	print ('Union = '+ str(x|y))
	print ('Difference = '+ str(x-y))
	print ('Intersection = '+ str(x&y))

	if 'se' in x:
		print 'x contains "se"'
	if 'se' in y:
		print 'y contains "se"'

if __name__ == "__main__":
	xyset()
