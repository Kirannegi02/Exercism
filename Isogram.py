def is_isogram(string):
    
    this_string = [i for i in string.lower() if i.isalpha()]
    return len(set(this_string)) == len(this_string)
