
verb_ans = ['buying', 'forgetting', 'eating']
noun_ans = ['pudding', 'monkey', 'pizza']
adjective_ans = ['crazy']

verb_num= 0
adj_num = 0
n_num = 0

def main_crazy_lib_origin(filename):
    try:
        my_file = open(filename, 'r')

        text = ''
        for line in my_file:
            text = text + process_line_origin(line)

        my_file.close()

        return text

    except FileExistsError:
        print("Sorry, couldn't find", filename + ".")
    except IsADirectoryError:
        print("Sorry", filename, "is a directory.")
    except:
        print("Sorry, could not read", filename)

def main_crazy_lib(filename):
    try:
        my_file = open(filename, 'r')

        text = ''
        for line in my_file:
            text = text + process_line(line)

        my_file.close()

        return text

    except FileExistsError:
        print("Sorry, couldn't find", filename + ".")
    except IsADirectoryError:
        print("Sorry", filename, "is a directory.")
    except:
        print("Sorry, could not read", filename)


def process_line_origin(line):
    return line

def process_line(line):

    words = line.split();

    symbol = ''
    process_line_word = ''

    global verb_num
    global adj_num
    global n_num

    for word in words:

        stripped = word.strip(",.:!?")
        if stripped != word:
            symbol = word[-1]
            tmp = stripped
            word = tmp

        if word in 'VERB_ING':
            word = verb_ans[verb_num]
            verb_num = verb_num + 1
        if word in 'NOUN':
            word = noun_ans[n_num]
            n_num = n_num + 1
        if word in 'ADJECTIVE':
            word = adjective_ans[adj_num]
            adj_num = adj_num + 1

        process_line_word = process_line_word  + ' ' + str(word) + str(symbol)
        symbol = ''

    process_line_word = process_line_word + str('\n')
    return process_line_word

def main():
    print("Q: ")
    file_name = input("Give a file name: ")
    lib = main_crazy_lib_origin(file_name)
    print(lib)

    print("Answer:")
    print("Noun: ", noun_ans)
    print("Verb: ", verb_ans)
    print("Adj: ", adjective_ans)
    print()

    lib = main_crazy_lib(file_name)
    print(lib)
    print("ver: ", verb_num, "noun_ans: ", n_num, "adj: ", adj_num)

if __name__ == '__main__':
    main()
