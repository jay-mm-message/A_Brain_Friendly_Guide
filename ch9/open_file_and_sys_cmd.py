import sys

def main():
    for i in range(0, len(sys.argv), 1):
        print(i, ', ', sys.argv[i])
    if len(sys.argv) != 2:
        print("Please give a file name!")
    else:
        my_file = open(sys.argv[1])
        my_text = my_file.read()
        print("file text:")
        print(my_text)
        my_file.close()

if __name__ == "__main__":
    main()
