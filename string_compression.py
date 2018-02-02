#compress a string into the counts of it. 

def compress(word):
	'''This counts all the characters in the word'''
	count = {}
	for i in range(len(word)):
		count[word[i]] = count.get(word[i],0)+1

	s=''
	for key in count:
		s+=key
		s+=str(count[key])

	return s

def compress2(word):
	s = ''
	counts = {}
	c=word[0]
	for i in range(1, len(word)):
		
		if word[i] != c:
			for key in counts:
				s+=str(key)
				s+=str(counts[key])
			counts = {}
		if not counts:
			c = word[i]
		counts[word[i]] = counts.get(word[i],0)+1

		if i==len(word)-1:
			for key in counts:
				s+=str(key)
				s+=str(counts[key])

	return s

def compress3(word):
	s = ''
	count = 0
	for i in range(len(word)):
		count= count+1

		if i+1>=len(word) or word[i]!=word[i+1]:
			s+=word[i]+str(count)
			count = 0
	return word if len(s)>len(word) else s


if __name__ == '__main__':
	print(compress3('aabcccccaa'))