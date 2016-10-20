# if you want to test wildcards more quickly, please comment line 13 and use fewer characters
import sys
import string
from score_function import score_word
from itertools import permutations
from collections import Counter
from collections import OrderedDict

## get user input from command line argument
#rack = input("enter 7 characters: ").lower()
if len(sys.argv) < 2:
    print("Please enter one argument.")
    quit()
rack = sys.argv[1].lower()
if len(rack) != 7:
    print("You didn't enter 7 characters.")
    quit()
count_word = Counter(rack)
if count_word['*'] + count_word['?'] >2:
    print("You entered more than 2 wildcards.")
    quit()

## find all valid scrabble words
all_words=[]
scrabble_ls=[]

with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]

## find all combinations of characters
for i in range(len(rack)):
    temp=[''.join(t) for t in list(permutations(rack, i+1))]
    all_words.extend(temp)
    
## whether the combination is in the data dictionary    
for item in all_words:
    item_ls=list(item)
    scrabble=[]
    position=[]
    # find the position of all wildcards
    for i in range(len(item_ls)):
        if item_ls[i] in ('?','*'):
            position.append(i)
    
    if len(position) == 0:
        if item.upper() in data:
            scrabble_ls.append(item)
    elif len(position)==1:
        for j in string.ascii_lowercase:
            item_ls[position[0]]=j
            item2=''.join(item_ls)
            if item2.upper() in data:
                scrabble_ls.append(item)
                break
    elif len(position) == 2:
        for j in string.ascii_lowercase:
            item_ls[position[0]]=j
            for k in string.ascii_lowercase:
                item_ls[position[1]] = k
                item2=''.join(item_ls)
                if item2 in data:
                    scrabble.append(item)
                    break
scrabble=set(scrabble_ls)

## sort the scores, score for wildcard is 0
scores={i:score_word(i) for i in scrabble}
scores_sort=OrderedDict(sorted(scores.items(), key=lambda t: t[1], reverse=True))
for word, score in scores_sort.items():
    print(score,word)