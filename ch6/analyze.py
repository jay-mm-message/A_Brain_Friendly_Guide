
import lyrics_paper

def output_results(score):
    level_no = "0"
    if score >= 90:
        level_no = "5"
        print("Reading level of ", level_no, "th Grade")
    elif score >= 80:
        level_no = "6"
        print("Reading level of ", level_no, "th Grade")
    elif score >= 70:
        level_no = "7"
        print("Reading level of ", level_no, "th Grade")
    elif score >= 60:
        level_no = "8-9"
        print("Reading level of ", level_no, "th Grade")
    elif score >= 50:
        level_no = "10-12"
        print("Reading level of ", level_no, "th Grade")
    elif score >= 30:
        print("Reading level of College Student")
    else:
        print("Reading level of College Student")


def count_syllables_in_word(word):
    count = 0

    endings = ".,;!?:"
    last_char = word[-1]

    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]

    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False

    if processed_word[-1] in 'yY':
        count = count + 1

    return count

def count_syllables(words):
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count

    return count

def count_sentences_1(word):
    count = 0
    for char in word:
        if char == '.' or char == '?' or char == ';' or char == '!':
            count = count + 1
    return count

def count_sentences_2(word):
    count = 0
    terminals = ".?!;"

    for char in word:
        if char in terminals:
            count = count + 1
    return count

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    print("text: ", text)
    print()

    words = text.split()
    total_words = len(words)
    total_syllables = count_syllables(words)
    print("words: ", words)
    print("total_words: ", total_words)
    #for word in words:
    #    total_sentences = total_sentences + count_sentences_1(word)
    for word in words:
        total_sentences = total_sentences + count_sentences_2(word)
    print("total_sentences: ", total_sentences)
    print("total_syllables: ", total_syllables)
    print()

    score = (206.835 - 1.015 * ( total_words / total_sentences )
                - 84.6 * ( total_syllables / total_words))
    output_results(score)

compute_readability(lyrics_paper.text)
