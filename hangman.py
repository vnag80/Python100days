import random
def check_word(word,letter,result):
    for num in range(0,len(word)):
        if (result[num] == '_' and word[num] == letter):
           result[num] = letter
    print(result)
    return result
def array_concat(word):
    con_str = ''
    for ch in word:
        con_str += ch
    return con_str;
words_list = ['venkat','fun','like','sanvi']
len_list = len(words_list);
random_word = words_list[random.randint(0,len_list - 1)];
word = [];
for num in range(0,len(random_word)):
    word.append('_')
print(word);
print("If you guess 5 wrongs you will be hanged");
result = ''
bad_tries = 0;
while( result == ''):
    guess = input("Enter the next guess")
    before_str = array_concat(word)
    check_word(random_word, guess, word)
    print(before_str)
    print(array_concat(word))

    if array_concat(word) != before_str:
        print(word)
        if array_concat(word) == random_word:
            result = 'win'
            print(f'you win and word is {array_concat(word)}');
    else:
        bad_tries += 1;
        if bad_tries == 5:
            result = 'lost'
            print(f'you Lost 5 bad guesses');


