#!usr/bin/python
#coding:utf-8
def string_reverse(word):
	word_rev = word[::-1]
	return word_rev
if __name__=='__main__':
	print string_reverse('stressed')
