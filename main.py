# Auto-completion of sentences Program using NLP with a simple GUI

import Trigram_language_model as model
from tkinter import *


# -----------------------------------------------------------------------------

def update(data):
    # Clear the listbox
    listBox.delete(0, END)

    # Add toppings to listbox
    for item in data:
        listBox.insert(END, item)


# -----------------------------------------------------------------------------

def autoFill(event):
    line = my_entry.get()
    inputText = re.split(" ", line)

    predictions = []
    if (len(inputText) == 1):
        if inputText[0] in model.bigramsModel:
            for i in range(5):
                if i >= len(model.bigramsModel[inputText[0]]):
                    break;
                predicted = model.bigramsModel[inputText[0]][i][0]
                predictions.append(predicted)

    else:
        given = " ".join(inputText[-2:])
        if given in model.trigramsModel:
            for i in range(5):
                if i >= len(model.trigramsModel[given]):
                    break;
                predicted = model.trigramsModel[given][i][0]
                predictions.append(predicted)

    update(predictions)


# -----------------------------------------------------------------------------

def getInput(event):
    line = my_entry.get()
    my_entry.focus_set()
    print(line)
    my_entry.insert(len(line), listBox.get(ANCHOR))


# -----------------------------------------------------------------------------

# GUI
root = Tk()
root.title("AutoFill")
root.geometry("500x300")

# Create a label
my_label = Label(root, text="What are you looking for? ", font=("Helvetica", 10), fg="blue")
my_label.pack(pady=20)

# Create an entry box
inputText = StringVar()
my_entry = Entry(root, textvariable=input, font=("Helvetica", 20))
my_entry.pack()

listBox = Listbox(root, width=25, font=20, justify="right")
listBox.pack()

listBox.bind("<<ListboxSelect>>", getInput)
my_entry.bind("<space>", autoFill)

root.mainloop()

# -----------------------------------------------------------------------------
