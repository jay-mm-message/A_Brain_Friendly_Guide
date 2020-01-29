
# palindrome 回文 tcaoact, bab
def is_palindrome(lists):
    diff_line = int(len(lists) / 2)

    for i in range(0, diff_line, 1):
        if (lists[0+i]) != (lists[-1-i]):
            return False
    return True

words = input("Please give words: ")
print("Is palindrome: ", is_palindrome(words))
