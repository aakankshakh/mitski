import numpy as np
import string
import itertools

k = 1

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

with open('all_mitski_lyrics.txt', 'r') as file:
    data = file.read().replace('\n', '')

'''
data = data.lower()
data = data.translate(str.maketrans('','',string.punctuation))
data = data.translate(str.maketrans('','',string.digits))
'''
alphabet = list(set(data))

#alphabet = [p for p in itertools.product(alphabet, repeat=k)]

print('here')

freq_dict = {}

count = 0

for letter in itertools.product(alphabet, repeat=k):

    letter = ''.join(letter)

    indexes = [i+len(letter) for i in findall(letter,data)]
    if len(indexes) == 0:
        continue

    freq_dict[letter] = {}

    count += 1

    for i in indexes:

        if i == len(data):
            i = 0

        if data[i] not in freq_dict[letter].keys():

            freq_dict[letter][data[i]] = 0
        ## Using Logan's much better, faster idea 
        freq_dict[letter][data[i]] += 1

    total = max(sum(freq_dict[letter].values()),1)

    for key in freq_dict[letter]:

        freq_dict[letter][key] = freq_dict[letter][key]/total

def generate_next_letter(freq_dict,letter):

    if letter in freq_dict.keys():
        values = freq_dict[letter].values()
        letters = list(freq_dict[letter].keys())
    else:
        letters = 'abcdefghijklmnopqrstuvwxyz '
        values = (1/26)*np.ones((len(letters),))

    probs = np.cumsum(list(values))

    rando = np.random.rand()

    for i in range(len(letters)):

        if rando < probs[i]:

            return letters[i]
        

letter = data[0:k]
N = 3000
h = 0

script = letter

while h < N:

    letter = generate_next_letter(freq_dict,script[h:h+k])
    script += letter
    h+=1


print(script)

    
        

    

