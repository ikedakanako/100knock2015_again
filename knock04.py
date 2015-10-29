#!usr/bin/python
#coding:utf-8
def word_location(sentence):
	word_list = list(); word_loc_dict = dict(); num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
	word_list = sentence.split()
	for n,word in enumerate(word_list):
		if n in num_list:
			word_loc_dict[word[:1]] = n + 1
		else:
			word_loc_dict[word[:2]] = n + 1
	return word_loc_dict
if __name__=='__main__':
	sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
	for word,loc in sorted(word_location(sentence).items(), key=lambda x:x[1]):
		print word,loc
