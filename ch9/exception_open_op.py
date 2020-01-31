
try:
    file_name = input("Give a file name: ")
    my_file = open(file_name, 'r')
except FileNotFoundError:
    print("Sorry, ", file_name, " could not be found.")
except IsADirectoryError:
    print("That's a directory not a file!")
else:
    print("It's a good thing we could open that file.")
    my_file.close()

finally:
    print("I'm running no matter what happens.")
