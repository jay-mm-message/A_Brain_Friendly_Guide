

def main_crazy_lib(filename):
    my_file = open(filename, 'r')

    text = ''
    for line in my_file:
        text = text + process_line(line)

    my_file.close()

    return text

def process_line(line):
    return line

def main():
    lib = main_crazy_lib('lib.txt')
    print(lib)

if __name__ == '__main__':
    main()
