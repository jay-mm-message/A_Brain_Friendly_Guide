
#names = [ 'Kim', 'John', 'Josh' ]
#emails = [ 'Kim@oreilly.com', 'john@abc.com', 'josh@wickedlysmart.com' ]

#for i in range (0, len(names), 1):
#    print("Address Book No. : ", i + 1 , ", name: ", names[i], ", email: ", emails[i])

users = { 'Kim':'Kim@oreilly.com', 'John':'john@abc.com' , 'Josh':'josh@wickedlysmart.com' }

for user in users:
    print("name: ", user, ", email: ", users[user])

user = input("Give a name: ")
if user in users:
    print(user, "'s email address is: ", users[user])
else:
    print(user, "'s email address not exist.")
