import re
from random import randint

import nltk
from tkinter import *

# ------------------------------------------------------------------------------
# f = open('test.txt', encoding="utf-8")
# #print(f.read())
# text = ""
# for i in f:
#     text+=i
#
# #print(text)
# #separating text into sentences
# sentences= re.split(r"[.\n،]", text)
# for sentence in sentences:
#     print("sent \n",sentence)
# tokens = nltk.sent_tokenize(text)
# #separating sentences into words
# for sentence in sentences:
#     tokenizer = nltk.RegexpTokenizer(r"\w+")
#     words = tokenizer.tokenize(sentence)
#     word_trigrams = nltk.trigrams(words)
#     print(words)
#     print("---------------")
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


# def displayOutput():

def getInput():
    line = input.get()
    print(line)
    words = re.split(" ", line)
    print(words)
    drop = OptionMenu


search_btn = Button(root, text='Search', command=getInput)
search_btn.pack()
variable = StringVar(root)
# Create a dropdown list
variable.set("predictions")
options = []
drop = OptionMenu(root, variable, *options)
drop.pack()

# def update(data):
#     # Clear the listbox
#      drop.delete(0, END)
#
#      for item in data:
#          drop.insert(END, item)
#
#
# def fillout(e):
#     # Delete whatever is in the entry box
#     my_entry.delete(0, END)
#
#     # Add clicked list item to entry box
#     my_entry.insert(0, drop.get(ANCHOR))
#
#
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
#
#
# update(options)
# # Create a binding on the listbox onclick
# drop.bind("<>", fillout)
#
# # Create a binding on the entry box
# my_entry.bind("", check)

root.mainloop()
