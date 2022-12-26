# Create a helper function param (text) > split() -> l

def split(text):

    words = []
    word = ""
    for c in text:      # same as lis, dictionar
        if c != " ":
            word += c # se primbla prin fiecare litera formeaza cuvintu
        else:
            words.append(word) ## cind da de spatiul gol il imbraca cuvintul in lista
            word = ""

    words.append(word)  ## il ea ape urmatorul cuvint si il pune in lista

    return words

# Calling our function
print( split( "hello people" ) )                
print( split( "I love python 3" ) )   
