class PalindromeString(str):
    def is_palindrome(self):
        heat = 0
        tail = len(self) - 1

        while heat <= tail:
            if self[heat] != self[tail]:
                return False

            heat = heat + 1
            tail = tail - 1

        return True

word = input("Give a word to check palindrome: ")
palindrome = PalindromeString(word)

if palindrome.is_palindrome():
    print(word, ", it's palindrome.", ", length is", len(word), "and upercase is", word.upper())
else:
    print(word, ", it isn't palindrome.", ", length is", len(word), "and upercase is", word.upper())


