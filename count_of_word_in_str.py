def count_of_word_in_string(input_str, search_str):
    count = 0
    word = ""

    for i in range(len(input_str)):
        if input_str[i] != " ":
            word += input_str[i]
            # when index reaches input_str end then we need to check the word
            if i == (len(input_str) - 1) and word == search_str:
                count += 1
        else:
            if word == search_str:
                count += 1
            word=""

    return count


str1 = "Meena is very good and Meena is good dancer."
str2 = "is very Meena good and Meena is good dancer is"

print(count_of_word_in_string(str1, "Meena"))
print(count_of_word_in_string(str2, "Meena"))
print(count_of_word_in_string(str1, "xyz"))
print(count_of_word_in_string(str2, "is"))
