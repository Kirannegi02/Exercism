from string import ascii_lowercase as lower
def is_pangram(sentence):
    
    return all(letter in sentence.casefold() for letter in lower)
