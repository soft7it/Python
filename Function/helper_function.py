# Create a helper function param (text) > split() -> l

def split(text):

    words = []
    word = ""
    for c in text:      # same as lis, dictionar
        if c != " ":
            word += c
        else:
            words.append(word)
            word = ""

    words.append(word)

    return words

# Calling our function
print( split( "hello people" ) )                
print( split( "I love python 3" ) )                