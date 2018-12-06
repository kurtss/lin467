import csv
import nagisa
from nltk.corpus import knbc
from nltk.corpus import jeita

out = open('tagged.csv', 'w+')
frequency_bigram = {}
frequency_word = {}
dictionary = {}

def tag_and_write(line):
    line = line.replace('\n', '')
    line = line.replace('〜', '')
    split = line.split(',')
    tagged = nagisa.tagging(split[1] if split[1] else split[0])
    if tagged.postags:
        out.write(line + ',' + tagged.postags[0] + '\n')
    else:
        out.write(line + '\n')

def bigram(first, second):
    return first + ',' + second

def bigram_freq(first, second):
    return bigram_freq_given(bigram(first, second))

def bigram_freq_given(bigram):
    if bigram in frequency_bigram:
        return frequency_bigram[bigram]
    return 0

def word_freq(word):
    if word in frequency_word:
        return frequency_word[word]
    return 0

def bigram_probability(first, second):
    if word_freq(first) == 0:
        return 0
    return (0.0 + bigram_freq(first, second)) / (0.0 + word_freq(first))

# out.write(line + ',' + tagged + '\n')

if __name__ == '__main__':
    with open('word_list.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            kansai = row[0].replace('〜', '')
            standard = row[1].replace('〜', '').split('・')
            if not kansai in dictionary:
                dictionary[kansai] = standard

    total = 0
    prev = 'BOS'
    for word in knbc.words():
        bg = bigram(prev, word)
        if bigram_freq_given(bg) == 0:
            frequency_bigram[bg] = 1
        else:
            frequency_bigram[bg] = frequency_bigram[bg] + 1
        if word_freq(word) == 0:
            frequency_word[word] = 1
        else:
            frequency_word[word] = frequency_word[word] + 1
        prev = word
        # total += 1
        # print(word + ', ' + str(frequency_word[word]))
    prev = 'BOS'
    for word in jeita.words():
        bg = bigram(prev, word)
        if bigram_freq_given(bg) == 0:
            frequency_bigram[bg] = 1
        else:
            frequency_bigram[bg] = frequency_bigram[bg] + 1
        if word_freq(word) == 0:
            frequency_word[word] = 1
        else:
            frequency_word[word] = frequency_word[word] + 1
        prev = word
        total += 1
    # print('total is ' + str(total))
    # tagged_kb = ['眠い', 'から', '早く', '寝', 'よ', '。', '明日', 'も', '仕事', 'や', '。', 'めんどい', 'な', 'あ', '。']
    tagged_kb = ['また', '会え', 'たら', 'めっちゃ', 'ええ', 'な', '〜', '。']
    final_sentence = ''

    prev_word = 'BOS'
    for i in range(len(tagged_kb)):
        word = tagged_kb[i]
        freq = bigram_probability(prev_word, word)
        # if freq > 0:
        highest_prob = freq
        best_word = word
        if word in dictionary:
            for definition in dictionary[word]:
                print('checking frequency for ' + word +':' + definition)
                changed_freq = bigram_probability(prev_word, definition)
                # changed_freq = bigram_probability(definition, prev_word)
                print('freq old: ' + str(freq) + '\nfreq new: ' + str(changed_freq))
                if changed_freq > highest_prob:
                    highest_prob = changed_freq
                    best_word = definition
                    print('best word for ' + word + ' is ' + definition)
        final_sentence = final_sentence + best_word
        prev_word = best_word

    print('the translated sentence is:\n' + final_sentence)