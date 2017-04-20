



def firstRepeatedWord(s):
	word_indexes = {}
	for word in s.split():
		if word in word_indexes:
			return word
		else:
			word_indexes[word] = 1




if __name__ == "__main__":
	s = "he had had quite enough of this nonsense"
	print firstRepeatedWord(s)