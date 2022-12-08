#  I use Tabs


def check_letter(letter, word, user_word):
	index = 0
	while index > -1:
		index = word.find(letter, index)
		if index != -1:
			user_word[index] = letter
			index += 1
	return user_word


def main():
	#  приветствие
	#  выбор загаданного слова из списка слов
	word = 'anaconda'
	user_word = ['_' for _ in range(len(word))]
	attempts = 0
	while attempts < 7 and '_' in user_word:
		print(*user_word)
		letter = input('Ваша буква: >_ ')
		user_word = check_letter(letter, word, user_word)
		attempts += 1

	print(attempts, user_word)


main()
