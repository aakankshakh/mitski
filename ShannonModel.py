import numpy as np
import string

with open('all_mitski_lyrics.txt', 'r') as file:
    data = file.read().replace('\n', '')

data = data.lower()

alphabet = list(set(data))

data = data.translate(str.maketrans('','',string.punctuation))

freq_dict = {}

for letter in alphabet:

    freq_dict[letter] = {}

    indexes = [i+1 for i, ltr in enumerate(data) if ltr == letter]

    count = 0

    for i in indexes:

        if i == len(data):
            i = 0

        if data[i] not in freq_dict[letter].keys():

            freq_dict[letter][data[i]] = 0

        sub_ind = [j for j, ltr in enumerate(data) if ltr == data[i]]

        f_count = len(set(indexes).intersection(sub_ind))

        freq_dict[letter][data[i]] += f_count

    total = sum(freq_dict[letter].values())

    for key in freq_dict[letter]:

        freq_dict[letter][key] = freq_dict[letter][key]/total

def generate_next_letter(freq_dict,letter):

    values = freq_dict[letter].values()
    letters = list(freq_dict[letter].keys())

    probs = np.cumsum(list(values))

    rando = np.random.rand()

    for i in range(len(letters)):

        if rando < probs[i]:

            return letters[i]
        

letter = data[0]
N = 1000
h = 0

script = letter

while h < N:

    letter = generate_next_letter(freq_dict,letter)
    script += letter
    h+=1


print(script)

        
    
        

        
        

    

