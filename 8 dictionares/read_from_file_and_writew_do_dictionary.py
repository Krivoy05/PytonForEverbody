"""
Exercise 1: [wordlist2]

Write a program that reads the words in words.txt and stores them as keys in a dictionary.
It doesn't matter what the values are.
Then you can use the in operator as a fast way to check whether a string is in the dictionary.

"""



def read_file_as_list_of_lines(file):
    file_as_list_of_lines = list()
    f = open(file,"r")
    for line in f:
        file_as_list_of_lines.append(line)
    return file_as_list_of_lines

def get_list_of_word_fron_list_of_lines(li):
    result_li = list()
    for line in li:
        result_li += line.split()
    return result_li


def add_to_ditcionary_fron_list(li):
    result_di = dict()
    for word in li:
        result_di[word] = word
    return result_di

def read_file_and_return_list_of_words(file_name):
    line_of_words = read_file_as_list_of_lines(file_name)
    list_of_words = get_list_of_word_fron_list_of_lines(line_of_words)
    return list_of_words

def read_from_file_and_return_dictioonary_of_words(file_name):
    result_di = dict()
    li_of_wors = read_file_and_return_list_of_words(file_name)
    result_di = add_to_ditcionary_fron_list(li_of_wors)
    return result_di

def read_from_file_and_return_dictioonary_of_words_metod_2(file_name):
    res_di = dict()
    f =open(file_name,"r")
    for line in f:
        words = line.split()
        for word in words:
            if res_di.get(word) == None:
                res_di[word] = 1
            else:
                res_di[word]+=1
    return res_di

def count_word_from_file(file_name):
    result_di = dict()
    f = open(file_name,"r")
    for line in f:
        words = line.split()
        for word in words:
            result_di[word] = result_di.get(word,0)+1
    return result_di

result = count_word_from_file("words.txt")
print(result)