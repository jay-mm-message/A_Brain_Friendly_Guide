def is_palindrome_recursive(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome_recursive(word[1:-1])
        else:
            return False

#word = input("Please give a word: ")
words = [ 'tcaoact', 'radar', 'yak', 'rader', 'kayjak' ]
for word in words:
    print(str(word), "is palindrome: ", is_palindrome_recursive(word))
