import sys
import ScrabbleMod
import string
import collections

"""This script provides a list of words that can be made from a 7 tile or less scrabble rack
   call it with a string of letters (the rack) a word refernce file and an optional letter 
   position constraint  example: scrabble.py "asdfq*?" sowpods.txt v3
   Wildcards take the form of * or ? and there can be up to 2 of them"""

print (sys.argv)

# check the input and catch commpn errors
if len(sys.argv)<2:
	raise Exception ('Argument error: please supply 1) a rack string and 2) a word file')
if len(sys.argv[1])>7 | len(sys.argv[1])<1:
	raise Exception ('Rack error: please supply a good rack, of 1-7 tiles') 

# LOAD EVERYTHING
with open(sys.argv[2], 'r') as f:
	wordfile=f.readlines()
	data = [datum.strip('\n\r') for datum in wordfile]

print('this is a sample of your wordfile', str(data[0:6]))
rack=sys.argv[1].upper()


# if there is a fixed position filter the list 
try:
	#fixed=sys.argv[3]
	fx_ltr=str(sys.argv[3][0].upper())
	fx_num=int(sys.argv[3][1])-1 # remember to adjust for 0 indexing
	print ('The fixed position letter is ' + fx_ltr)
	print ('The fixed position number is ' + str(fx_num))	
	if str.find(rack, fx_ltr) < 0 : 	# check that the fixed letter is in the rack 
		print('the rack is {0} and the letter is {1}'.format(rack, fx_ltr))
		raise Exception ('the letter listed as required is not in the rack')
except:
	fx_ltr=None

#Check each word in the list to see if it can be made up of the letters in the rack
#To allow for wildcards, keep a counter and skip n mismatches when you run into a mismatch
WdCd=str.count(rack, '*' ) + str.count(rack, '?' )
AcceptedWordVal={}

# MAIN LOOP 
for word in data: # for each word 
	# RESET THE VARIABLES
	WordScore=0 # this can be build letter by letter as they match (wildcards are skipped)
	temprack=list(rack) # an consumable rack that we can pop letters off of
	WdCd=str.count(rack, '*' ) + str.count(rack, '?' ) 

	# FIXED POSITION CHECKS
	# if the fixed position does not match the word or if the word is 
	# too short, go to the next word
	if fx_ltr is not None: 
		#print ('fixed ltr is not none')
		if len(word)-1 < fx_num:
			continue
			#print('lent_iss')
		if word[int(fx_num)] != fx_ltr:
			continue
			#print('num_iss')

	# NOTE the use of a "for break else loop" here
	# informative print statements can be used to trouble shoot (remove ##> comment marks)
	for i in range(len(word)):	# check each letter of the word to see if it is in the rack	
		if word[i] not in temprack:

			if WdCd != 0: # if there is a 
			   WdCd -= 1
			   ##>print('used wildcard for' + word[i] + 'in word' + word)
			else: 
				##>print (rack + 'does not have all the letters in' + word)
				break  # check the next letter 
		elif word[i] in temprack: # if there is a match remove the tile from your rack
			temprack.remove(word[i])
			WordScore=WordScore+ScrabbleMod.score_word(word[i]) # score only non wildcard letters
			##>print('Found the letter: ' + word[i] + 'in word' + word)
			##>print("These are your remaining letters " + str(temprack))
		##>input("next?")
	else : 
		##>print ('found all letters for', word, 'in ', str(rack))
		AcceptedWordVal[word]=WordScore
WordLs=(sorted(AcceptedWordVal.items(), key = lambda x: x[1], reverse=True))
print(WordLs)

