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
    position = int(input("whichi position do you want ?")) - 1
    # intrebare ? daca pune text - cum eliminam eroarea la position ?  rindu 49 ?????????????????? 

    if position <= len(notes) and position >= 0:
        pnotes.insert(position, {"text": text, "when": None})
        # intebare ? sa nu scrim "when" - al 2-lea posibil ?????????????????????????????????
    elif position <= 1:
        print(f"you position {position + 1} is not right")
    elif isinstance( position, str):
    # type(position) == str:?????????????????????????????????????????????
    # position == str(position):
        print(f"you position is wrong, you need insert only number")
    else:
        print(f"you position {position} is not right")


# .insert() metod
#  HW : ask the user if he wants it on a specific position 

    # pnotes.append( { "text": text } )

def deleteNote(pnotes) :
    idx = int(input("which one delete : ")) - 1 # dearece numaratoarea se incepe de la 0 zero
    pnotes.pop(idx)

################################################
# 
clear()
addNote(notes)
# deleteNote(notes)   
showNotes(notes) 
