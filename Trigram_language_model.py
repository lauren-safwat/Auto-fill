# A trigram language model using Arabic language corpus

import re
import nltk

# -----------------------------------------------------------------------------

def prepareCorpus():
    # Opening and reading corpus file line by line
    path = "E:\\FCAI\\4th year , 2nd semester\\NLP\\Assignments\\Assignment 1\\Auto fill\\Corpus.txt"
    file = open(path, 'r', encoding='UTF-8')
    corpus = file.read()
    file.close()

    # Removing the special characters
    corpus = re.sub('[\W_]+', ' ', corpus)

    # Word-tokenization
    tokens.extend(nltk.word_tokenize(corpus))

# -----------------------------------------------------------------------------

def nGramsFreq(n, nGrams):
    for i in range(len(tokens)-n+1):
        seq = tokens[i:i+n-1]
        seq = " ".join(seq)
        if seq not in nGrams:
            nGrams[seq] = {}
        freq = nGrams[seq].get(tokens[i+n-1], 0) + 1
        nGrams[seq][tokens[i+n-1]] = freq

# -----------------------------------------------------------------------------

def calcProb(nGrams):
    for key in nGrams:
        keyProb = float(sum(nGrams[key].values()))
        for word in nGrams[key].keys():
            nGrams[key][word] /= keyProb
        nGrams[key] = sorted(nGrams[key].items(), key=lambda x: x[1], reverse=True)

# -----------------------------------------------------------------------------

# Main:

tokens = []
bigramsModel = {}
trigramsModel = {}

prepareCorpus()

nGramsFreq(2, bigramsModel)
nGramsFreq(3, trigramsModel)

calcProb(bigramsModel)
calcProb(trigramsModel)
