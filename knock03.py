#!usr/bin/python
#coding:utf-8
def number_of_char(sentence):
	num_list = list()
	for word in sentence.split():
		if word.endswith(',') or word.endswith('.'):
			word = word[:-1]
		num_list.append(len(word))
	return num_list
if __name__=='__main__':
	sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving     quantum mechanics.'
	for num in number_of_char(sentence):
		print num,
