phrase = str(input('Введите предложение на английском: '))

vowels = ['o', 'e', 'i', 'u', 'a']

length = len(phrase)
low_letters = phrase.lower()
vowels_count = sum(low_letters.count(vowel) for vowel in vowels)
words_replace = low_letters.replace('ugly', 'beauty')
start_end_check = phrase.startswith('The') and phrase.endswith('end')

print(f'Длина: {length}\n'
      f'Нижний регистр: {low_letters}\n'
      f'Количество гласных: {vowels_count}\n'
      f'Замена слов: {words_replace}\n'
      f'Удовлетворение условия: {start_end_check}')
