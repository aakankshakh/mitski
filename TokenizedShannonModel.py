import numpy as np
import string

from transformers import AutoTokenizer

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

with open('all_mitski_lyrics.txt', 'r') as file:
    data = file.read().replace('\n', '')

data = data.lower()
data = data.translate(str.maketrans('','',string.punctuation))
data = data.translate(str.maketrans('','',string.digits))

tokenizer = AutoTokenizer.from_pretrained("gpt2")

mitski_tokens = tokenizer(data)

freq_dict = {}

count = 0

for i in range(len(mitski_tokens['input_ids'])-1):

    token = mitski_tokens['input_ids'][i]
    next_token = mitski_tokens['input_ids'][i+1]

    if token in freq_dict:
        if next_token in freq_dict[token]:
            freq_dict[token][next_token] += 1
        else:
            freq_dict[token][next_token] = 1
    elif token not in freq_dict:
        freq_dict[token] = {next_token:1}


def generate_next_token(freq_dict,token):

    next_possible_tokens = list(freq_dict[token].keys())
    values_of_tokens = freq_dict[token].values()

    probs = np.cumsum(list(values_of_tokens))
    rando = np.random.rand()

    for i in range(len(next_possible_tokens)):

        if rando < probs[i]:

            return next_possible_tokens[i]

first_token = mitski_tokens['input_ids'][0]
N = 3000
h = 0

script = [first_token]

while h < N:

    token = generate_next_token(freq_dict,script[-1])
    script.append(token)
    h+=1

decoded_script = tokenizer.decode(script)
print(script)

print(decoded_script)