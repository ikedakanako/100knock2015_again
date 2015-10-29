#!usr/bin/python
#coding:utf-8
def odd_string(word):
	word_odd = word[::2]
	return word_odd
if __name__=='__main__':
	print odd_string(u'パタトクカシー')
