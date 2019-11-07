def count_chars_in_string(string):
    count_char = {}

    for char in string:
        if char != ' ':
            if count_char.get(char) is None:
                count_char.update({char: 1})
            else:
                count = count_char.get(char)
                count_char.update({char: count+1})
    return count_char


string = "nothing is impossible"
print(count_chars_in_string(string))
