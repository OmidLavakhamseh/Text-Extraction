import re
import sys
from operator import itemgetter
def main_function(file):
    try:
        f = open(file,"r")
    except OSError:
        print(f"The file does not exist!")

    with f:

        data = f.read()
        data = char_check(data)

        freq_table(get_letter_frequencey(data))
        splitted_letter,words_counts=words_count(data)

        print(f"\nThe number of words that the text contains is :{len(splitted_letter)}")
        print(f"\nThe number of unique words that the text contains is :{len(words_counts)}")

        most_observed_word(data,5,3)

        f.close()
  

def char_check(input):
    pattern=r'[^a-zA-ZäöåÄÖÅ]'#caret(^) says to relace those which are not in list
    return(re.sub(pattern, ' ', input.lower()))


def words_count(input):
    splitted =  input.lower().split()
    observation_dict = dict()
    for item in splitted:
        if item in observation_dict:
            observation_dict[item] += 1#For previously seen words
        else:
            observation_dict[item] = 1#For new words
    return(splitted,observation_dict)

def get_top_items(top_count,data_list):
    counter = 1
    top_items = dict()
    for word, count in sorted(data_list.items(), key=itemgetter(1),reverse=True):
        if counter <= top_count:
            top_items[word] = count
            counter += 1
    return top_items

def get_letter_frequencey(input):

    splitted = input.lower().split()

    letter_count = dict()
    for word in splitted:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return(letter_count)

def freq_table(input):
    '''Frequency table for letters'''
    print("Frequency table for alphabetic letters which ordered from the most common to the least")
    for letter, times in sorted(input.items(), key=itemgetter(1),reverse = True):
        print(f"Letter {letter}  --> {times} ")

def observed_words(word,text):
    words_observed = [text[i + 1] for i in range(len(text)) if text[i]==word and i + 1 < len(text)]

    dic_observed =dict()

    for word in words_observed:
        if word in dic_observed:
            dic_observed[word] += 1
        else:
            dic_observed[word] = 1
    return dic_observed

def most_observed_word(text,num_most_common_used,num_observed_words):
    '''To see the five most commonly used words, their frequency and the words that most
    commonly follow them'''
    print(f"The {num_most_common_used} most commonly used words and their frequency and the words that most commonly follow them max {num_observed_words} per word, ordered from most common to least, including information about the number of occurrences most common follow words :-")
    splitted_letter,words_counts=words_count(text)
    top_words_list = get_top_items(num_most_common_used,words_counts)
    for word, times in sorted(top_words_list.items(), key=itemgetter(1),reverse = True):
        print(f"{word} ( {times} occurences )")
        top_items = get_top_items(num_observed_words,observed_words(word,splitted_letter))
        for top_words, top_times in sorted(top_items.items(), key=itemgetter(1),reverse = True):
            print(f"--> {top_words}, {top_times}")




def main():
    '''To see error if user didn't provide file.'''
    if len(sys.argv) == 2:
        main_function(sys.argv[1])
    else:
        print("Provide the file argument please!")



main()

# Question1: In what way did you "clean up" or divide up the text into words?
#Fisrtly we made all the letters lower case,to avoid counting for examle "lord","Lord" and "lord." as different words.
#secondly split the words by space.

#Question2:Which data structures have you used?
#We have used dictionary and list. list for situation we require an ordered sequence of items like seq_words_observed. 
# Also Dictionary when we want to relate values with keys like observation_dict and letter_count(to have observed words with their frequents)