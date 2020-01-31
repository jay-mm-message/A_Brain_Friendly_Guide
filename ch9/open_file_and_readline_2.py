

my_file = open('lib.txt', 'r')

i = 0
for my_text in my_file:
    print("(", i, ": ", my_text)
    i = i + 1

#i = 0
#while True:
#    my_text = my_file.readline()
#    if my_text != '':
#        print("(", i, ": ", my_text)
#        i = i + 1
#    else:
#        break
my_file.close()
