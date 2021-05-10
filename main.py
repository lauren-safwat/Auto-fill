# Auto-completion of sentences Program using NLP with a simple GUI

import pandas as pd

#Program Global Variables

# -----------------------------------------------------------------------------

def readData():
    path = "E:\\FCAI\\4th year , 2nd semester\\NLP\\Assignments\\Assignment 1\\Bigram.csv"
    path2 = "E:\\FCAI\\4th year , 2nd semester\\NLP\\Assignments\\Assignment 1\\Trigram.csv"
    bigram = pd.read_csv(path, encoding='UTF-8', header=0, index_col=0)
    trigram = pd.read_csv(path2, encoding='UTF-8', header=0, index_col=0)
    return bigram, trigram

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Main:

bigramModel, trigramModel = readData()
print(bigramModel)
print()
print(trigramModel)

# -----------------------------------------------------------------------------