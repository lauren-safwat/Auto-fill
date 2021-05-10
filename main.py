# Auto-completion of sentences Program using NLP with a simple GUI

import pandas as pd
import re
import nltk
from random import randint
from tkinter import *

#Program Global Variables

# -----------------------------------------------------------------------------

def readData():
    path = "E:\\FCAI\\4th year , 2nd semester\\NLP\\Assignments\\Assignment 1\\Bigram.csv"
    path2 = "E:\\FCAI\\4th year , 2nd semester\\NLP\\Assignments\\Assignment 1\\Trigram.csv"
    bigram = pd.read_csv(path, encoding='UTF-8', header=0, index_col=0)
    trigram = pd.read_csv(path2, encoding='UTF-8', header=0, index_col=0)
    return bigram, trigram

# -----------------------------------------------------------------------------

def getInput():
    line = input.get()
    print(line)
    words = re.split(" ", line)
    print(words)
    drop = OptionMenu

# -----------------------------------------------------------------------------

# def createList():
#     variable = StringVar(root)
#     # Create a dropdown list
#     variable.set("predictions")
#     options = []
#     for i in range(0, 5):
#         value = randint(0, 90)
#         options.append(value)
#     drop = OptionMenu
#     if bool == False:
#         drop = OptionMenu(root, variable, *options)
#         drop.pack()
#     else:
#         drop = drop.configure(root, variable, *options)
#     bool = True

# -----------------------------------------------------------------------------

# def update(data):
#     # Clear the listbox
#      drop.delete(0, END)
#
#      for item in data:
#          drop.insert(END, item)

# -----------------------------------------------------------------------------

# def fillout(e):
#     # Delete whatever is in the entry box
#     my_entry.delete(0, END)
#
#     # Add clicked list item to entry box
#     my_entry.insert(0, drop.get(ANCHOR))

# -----------------------------------------------------------------------------

# def check(e):
#     typed = my_entry.get()
#     if typed == '':
#         data = options
#     else:
#         data = []
#         for option in options:
#             if typed.lower() in option.lower():
#                  data.append(option)
#     update(data)

# -----------------------------------------------------------------------------

# def displayOutput():

# -----------------------------------------------------------------------------

# GUI
root = Tk()
root.title("AutoFill")
root.geometry("500x300")

# Create a label
my_label = Label(root, text="What are you looking for? ", font=("Helvetica", 10), fg="blue")
my_label.pack(pady=20)

# Create an entry box
input = StringVar()
my_entry = Entry(root, textvariable=input, font=("Helvetica", 20))
my_entry.pack()

bool = False

# search_btn = Button(root, text='Search', command=getInput)
# search_btn.pack()
variable = StringVar(root)

# Create a dropdown list
variable.set("predictions")
options = ["Option 1", "Option 2"]
drop = OptionMenu(root, variable, *options)
drop.pack()
drop.bind(root, "<<ListboxSelect>>", getInput)
# update(options)
# # Create a binding on the listbox onclick
# drop.bind("<>", fillout)
#
# # Create a binding on the entry box
# my_entry.bind("", check)

root.mainloop()

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