def dna_base_frequencies(dna_string):
	valid_bases = ['A','C','G','T']
	base_freq = {}
	base_freq['A'] = 0
	base_freq['C'] = 0
	base_freq['T'] = 0
	base_freq['G'] = 0

	for base in dna_string:
		if base in valid_bases:
			base_freq[base] += 1
	return base_freq


def trancribe_dna_to_rna(dna_string):
	rna = ''
	for base in dna_string:
		rna+= 'U' if base == 'T' else base
	return rna


def reverse_compliment(dna_string):
	rc = ''
	for index in range(len(dna_string)-1, -1, -1):
		base = dna_string[index]
		if base == 'A':
			rc+='T'
		elif base == 'T':
			rc+= 'A'
		elif base == 'C':
			rc+= 'G'
		elif base == 'G':
			rc+= 'C'
	return rc

def hamming_distance(string1, string2):
	shorter_string = string1 if len(string1) <= len(string2) else string2
	longer_string = string1 if shorter_string == string2 else string2

	dist = 0
	for index in range(len(shorter_string)):
		if not shorter_string[index] == longer_string[index]:
			dist +=1
	
	# handle case when string are diff length
	dist += len(longer_string) - len(shorter_string)
	return dist


def ros1(dna_string):
	base_count = dna_base_frequencies(dna_string)
	return str(base_count['A']) + " " + str(base_count['C']) + " " + str(base_count['G']) + " " + str(base_count['T']) + " "

def ros2(dna_string):
	return trancribe_dna_to_rna(dna_string)

def ros3(dna_string):
	return reverse_compliment(dna_string)

def ros6()


print ros1('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
print ros2('GATGGAACTTGACTACGTAAATT')
print ros3('AAAACCCGGT')

