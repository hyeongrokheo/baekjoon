word = input()
target_word_list = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for target_word in target_word_list:
    word = word.replace(target_word, '*')

print(len(word))