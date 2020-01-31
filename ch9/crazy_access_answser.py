

verb_ing = ['buying', 'forgetting', 'eating']
noun = ['pudding', 'monkey', 'pizza']
adjective = ['crazy']


def main_crazy_lib_origin(filename):
    my_file = open(filename, 'r')

    text = ''
    for line in my_file:
        text = text + process_line_origin(line)

    my_file.close()

    return text
def main_crazy_lib(filename):
    my_file = open(filename, 'r')

    text = ''
    for line in my_file:
        text = text + process_line(line)

    my_file.close()

    return text

def process_line_origin(line):
    return line

def process_line(line):

    words = line.split();
    verb = 0
    adj = 0
    n = 0

    process_line_word = ''
    for word in words:
        if word in 'VERB_ING':
            word = verb_ing[verb]
            verb = verb + 1
        if word in 'NOUN':
            word = noun[n]
            n = n + 1
        if word in 'ADJECTIVE':
            word = adjective[adj]
            adj = adj + 1

        process_line_word = process_line_word + ' ' + word + ' '

    process_line_word = process_line_word + '\n'
    return process_line_word

def main():
    lib = main_crazy_lib('lib.txt')
    print(lib)
    lib = main_crazy_lib_origin('lib.txt')
    print(lib)

if __name__ == '__main__':
    main()
