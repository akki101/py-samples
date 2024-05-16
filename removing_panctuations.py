def remove_panctuation(str):
    new_str = ''
    for char in str:
        if char.isalpha() or char == ' ':
            new_str += char
    
    print(new_str)
    return new_str



var = "Hi!!, this [is my]. name-"

remove_panctuation(var)