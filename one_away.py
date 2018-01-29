#check if a given string is one edit or zero edits away from another given string

def check(word1, word2):
	'''Finds the longer word and then iterates through the longer word and checks to see if there are more than two differences
	between the word. Exits as soon as it finds two differences.'''
	if word1 == word2:
		return True

	if max(len(word1),len(word2))>min(len(word1),len(word2))+1:
		return False

	if len(word1)>len(word2):
		longer_word = word1
		shorter_word = word2
	else:
		longer_word = word2
		shorter_word = word1

	unmatched = False
	for val1 in longer_word:
		if not any(x == val1 for x in shorter_word):
			if unmatched:
				return False
			unmatched = True

	return True

def checkSets(word1, word2):
	'''Checks whether the size of the set that is the intersection between the two words is 1 smaller than the size of the largest word'''
	return max(len(word1),len(word2))-1<=len(set(word1).intersection(set(word2)))

def checkProper(word1,word2):
	'''Counts the number of characters and then checks to see if there is a difference in counts which is 2 or more. '''
	if word1 == word2:
		return True

	if max(len(word1),len(word2))>min(len(word1),len(word2))+1:
		return False

	word1_counts = getCharacterCounts(word1)
	word2_counts = getCharacterCounts(word2)

	if len(word1_counts)>len(word2_counts):
		longer_word = word1_counts
		shorter_word = word2_counts
	else:
		longer_word = word2_counts
		shorter_word = word1_counts

	oneCount = 0
	default = 0
	for key in longer_word:
		if longer_word[key] != shorter_word.get(key, default):
			if oneCount>=2:
				return False
			oneCount +=1

	return True

def getCharacterCounts(word):
	'''Counts the number of characters in a string and returns a dictionary of them.'''
	counts = {}
	default = 0
	for val in word:
		counts[val] = counts.get(val,default) + 1
	return counts


if __name__ == '__main__':
	s1 = 'pale'
	s2 = 'peee'
	#These do not account for the fact that there might be multiple of the same character. 
	print(check(s1,s2))
	#These two work
	print(checkSets(s1,s2))  
	print(checkProper(s1,s2))
