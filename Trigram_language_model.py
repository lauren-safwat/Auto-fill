# A trigram language model using Arabic language corpus

import re
import nltk

# Program global variables
tokens = []
sequences = {}


# -----------------------------------------------------------------------------

def prepareCorpus():
    # Opening and reading corpus file line by line
    file = open("E:\\FCAI\\4th year , 2nd semester\\NLP\\Assignments\\Assignment 1\\report_1.txt", "r",
                encoding='UTF-8')
    corpus = file.readlines()

    for i in range(len(corpus)):
        # Removing the special characters
        corpus[i] = re.sub('[\W_]+', ' ', corpus[i])

        # Word-tokenization
        words = nltk.word_tokenize(corpus[i])
        tokens.extend(words)


# -----------------------------------------------------------------------------

def nGrams(n_grams):
    for n in range(1, n_grams + 1):
        for i in range(len(tokens) - (n - 1)):
            seq = [tokens[j] for j in range(i, i + n)]
            seq = " ".join(seq)
            freq = sequences.get(seq, 0) + 1
            sequences[seq] = freq


# -----------------------------------------------------------------------------

def printSequences():
    for key in sequences:
        print(key, " :: ", sequences[key])

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Main function
prepareCorpus()
print(tokens)
print()
nGrams(3)
printSequences()
