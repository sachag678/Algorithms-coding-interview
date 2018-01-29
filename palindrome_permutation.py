#check if a string is a permutation of a palindrome. the palindrome doesn't need to be limited to dctionary words.
from collections import defaultdict
def check(word):
	'''Takes a word and check if it is a permutation of a palindrome'''
	word_with_no_space = word.replace(" ","").lower()
	return checkPalindrom(word_with_no_space)

def checkPalindrom(word):
	'''Checks if word is a palindrome by counting the number of letter characters and putting them in dict 
	and then checking to see if there is a max of one odd count. Only one odd count allowed for odd lengths of a word
	and 0 odd counts for the even length of a word.'''
	#word = list(word)
	char_counts = {}
	default = 0
	for i in range(len(word)):
		char_counts[word[i]] =  char_counts.get(word[i],default) + 1

	print(char_counts)
	
	foundOdd = False
	for val in char_counts.values():
		if val%2 == 1:
			if foundOdd:
				return False
			foundOdd = True

	return True

if __name__ == '__main__':
	s = 'aabb'
	print(check(s))