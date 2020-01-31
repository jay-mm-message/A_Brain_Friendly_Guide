
#Sorry, an error occured opening

try:
    file_name = input("Give a file name: ")
    my_file = open(file_name, 'r')
except:
    print("Sorry, an error occured opening: ", file_name)
else:
    my_text = my_file.read()

    print("file text: ")
    print(my_text)

    my_file.close()
