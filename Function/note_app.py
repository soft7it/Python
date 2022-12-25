from os import system
from datetime import datetime
### Notes APP

# * timer - alarm

notes = [
    {
        "text": "table 1, 2 soups",
        "when": "03:57",
    },
    {
        "text": "bill to table 2",
        "when": "21:08",
    },
    {
        "text": "call mom",
        "when": None,
    },
]

def clear():
    system("cls")


def showNotes(pnotes):
    now = datetime.now() # get exact time now
    h, m = now.hour, now.minute
    for note in pnotes:  #
        warning = "" # asteapta! alarma 
        if note["when"] != None:
            fragments = note["when"].split(":")
            nh, nm = int(fragments[0]), int(fragments[1])
            if h == nh and nm - m < 5 :
                warning = "( 5 or less min left !!!)"
        print(f"{note['text']} {warning}")


def addNote(pnotes) :
    text = input("enter text: ") 

# .insert() metod
#  HW : ask the user if he wants it on a specific position 

    pnotes.append( { "text": text } )

def deleteNote(pnotes) :
    idx = int(input("which one : ")) - 1 # dearece numaratoarea se incepe de la 0 zero
    pnotes.pop(idx)

################################################
# 
clear()
# addNote(notes)
# deleteNote(notes)   
showNotes(notes)     
