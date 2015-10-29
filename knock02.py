#!usr/bin/python
#coding:utf-8
def string_alternate(word1,word2):
	word_alt = u''
	for w1,w2 in zip(word1,word2):
		word_alt += w1 + w2
	return word_alt
if __name__ =='__main__':
	print string_alternate(u'パトカー',u'タクシー')
