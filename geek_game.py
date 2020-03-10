import random
words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
             'шайба', 'олимпиада', 'сноуборд')

secret_word = random.choice(words_list)

gamer_word = ['*'] * len(secret_word)
print(' '.join(secret_word))
error_counter = 0
while True:
    letter = input('ввведите букву').lower()

    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            # print(idx, symbol)
            if symbol == letter:
                gamer_word[idx] = letter
        # if ''.join(gamer_word) == secret_word:
        if '*' not in gamer_word:
            print('вы выиграли!!!')
            print('было загадано слово:', secret_word.upper())
            break

    else:
        error_counter += 1
        if error_counter == 8:
            rint('Lose')
            break
        pass
    print("".join(gamer_word))
print('Again?')
