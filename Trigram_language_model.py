# A trigram language model using Arabic language corpus

import re
import nltk
import pandas as pd

# Program global variables
tokens = []
unigrams = []
bigrams = []
trigrams = []

pd.set_option("precision", 2)

# -----------------------------------------------------------------------------

def prepareCorpus():
    # Opening and reading corpus file line by line
    path = "E:\\FCAI\\4th year , 2nd semester\\NLP\\Assignments\\Assignment 1\\Test.txt"
    file = open(path, 'r', encoding='UTF-8')
    corpus = file.readlines()
    file.close()

    for i in range (len(corpus)):
        # Removing the special characters
        corpus[i] = re.sub('[\W_]+', ' ', corpus[i])

        # Word-tokenization
        tokens.append(nltk.word_tokenize(corpus[i]))

# -----------------------------------------------------------------------------

def nGrams(n, nGrams):
    for sentence in tokens:
        for i in range(len(sentence)-n+1):
            seq = [sentence[j] for j in range(i, i + n)]
            seq = " ".join(seq)
            nGrams.append(seq)

# -----------------------------------------------------------------------------

def calcFreq(nGrams, nGramsModel):
    for seq in set(nGrams):
        givenWords = " ".join(seq.split(" ")[:-1])
        nextWord = " ".join(seq.split(" ")[-1:])
        nGramsModel.loc[givenWords, nextWord] = nGrams.count(seq)

# -----------------------------------------------------------------------------

def calcProb(nGrams, nGramModel):
    for i in range(nGramModel.shape[0]):
        nGramModel.iloc[i,:] /= nGrams.count(nGramModel.index.values[i])

# -----------------------------------------------------------------------------

def writeToFile(fileName, nGramModel):
    path = "E:\\FCAI\\4th year , 2nd semester\\NLP\\Assignments\\Assignment 1\\" + fileName
    nGramModel.to_csv(path, mode='w', float_format='%.3f', encoding='UTF-8', header=True, index=True)

# -----------------------------------------------------------------------------

def trainModel():
    prepareCorpus()

    nGrams(1, unigrams)
    nGrams(2, bigrams)
    nGrams(3, trigrams)

    bigramModel = pd.DataFrame(index=set(unigrams), columns=set(unigrams), data=0)
    trigramModel = pd.DataFrame(index=set(bigrams), columns=set(unigrams), data=0)

    calcFreq(bigrams, bigramModel)
    calcFreq(trigrams, trigramModel)

    calcProb(unigrams, bigramModel)
    calcProb(bigrams, trigramModel)

    writeToFile("Bigram.csv", bigramModel)
    writeToFile("Trigram.csv", trigramModel)

# -----------------------------------------------------------------------------

# Main:

trainModel()
# print(tokens)
# print()
# print("\n".join(bigrams))
# print()
# print("\n".join(trigrams))
# print()
# print(bigramModel)
# print()
# print(trigramModel)
