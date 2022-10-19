import random
import re
import sys
used_words_old = dict()
from operator import itemgetter

def main_function(file,word_first,n_count):

    try:
        f = open(file,"r",encoding='utf-8')
    except OSError:
        print(f"The file does not exist!")

    with f:

        data = f.read()
        data = char_check(data)

        random_word(data,word_first,n_count)
    #print(f.closed)

def char_check(input):
    pattern=r'[^a-zA-ZäöåÄÖÅ]'
    return(re.sub(pattern, ' ', input.lower()))


def observed_words(word,text):
    splitted = text.split()
    words_observed = [splitted[i + 1] for i in range(len(splitted)) if splitted[i]==word and i + 1 < len(splitted)]

    dic_observed = dict()

    for word in words_observed:
        if word in dic_observed:
            dic_observed[word] += 1
        else:
            dic_observed[word] = 1
    return dic_observed

def random_word(text,word_first,n_count):
    global used_words_old

    used_words_old = dict()  # Clear Global Variable
    iteration = 0
    generated_text = word_first
    next_word = word_first

    while int(n_count) > iteration:
        new_word = random_word_from_word_list(text,next_word)
        if new_word == None:
            break
        generated_text = generated_text + ' ' + new_word
        next_word = new_word
        iteration = iteration + 1
    print(generated_text)



def random_word_from_word_list(text,word):
    global used_words_old
    if used_words_old.get(word) == None:#because next work can be the same word.
        words_observed = observed_words(word,text)
        if len(words_observed) > 0:
            seq_words_observed = []
            for top_words, top_times in sorted(words_observed.items(), key=itemgetter(1),reverse = True):
                lst_words_observed = [top_words] * top_times
                seq_words_observed.extend(lst_words_observed)
            random_index = random.randint(0,len(seq_words_observed) - 1)
            used_words_old[word] = seq_words_observed # update global variable
            return seq_words_observed[random_index]
        else:
            return None
    else:
        seq_words_observed = used_words_old[word]
        random_index = random.randint(0,len(seq_words_observed) - 1)
        used_words_old[word] = seq_words_observed # update global variable
        return seq_words_observed[random_index]



def main():
    if len(sys.argv) == 4:
        main_function(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print("Function needs to take three arguments: a file name of a text file, a starting word and a maximum number of words!")



main()

