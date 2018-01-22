#-*- coding:utf-8 -*-
def break_words(stuff):
	words = stuff.split(" ")
	print(words)
	return words

def sort_words(words):
	return sorted(words)

def print_first_word(words):
	word = words.pop(0)
	print(word)
	return word

def print_last_word(words):
	word = words.pop(-1)
	print(word)
	return word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last_word(sentence):
	list1 = []
	words = break_words(sentence)
	first = print_first_word(words)
	list1.append(first)
	last = print_last_word(words)
	list1.append(last)
	print(list1)

if __name__ == '__main__':
	print_first_and_last_word("a is a goog param")
