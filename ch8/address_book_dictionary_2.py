
#names = [ 'Kim', 'John', 'Josh' ]
#emails = [ 'Kim@oreilly.com', 'john@abc.com', 'josh@wickedlysmart.com' ]

#for i in range (0, len(names), 1):
#    print("Address Book No. : ", i + 1 , ", name: ", names[i], ", email: ", emails[i])

attributes1 = {
        'email' : 'kim@oreilly.com',
        'gender' : 'f',
        'age' : '27',
        'friends' : ['John', 'Josh'] }

attributes2 = {
        'email' : 'john@abc.com',
        'gender' : 'm',
        'age' : '24',
        'friends' : ['Josh', 'Kim'] }

attributes3 = {
        'email' : 'josh@wickedlysmart.com',
        'gender' : 'm',
        'age' : '24',
        'friends' : ['John', 'Kim'] }

#users = { 'Kim':'Kim@oreilly.com', 'John':'john@abc.com' , 'Josh':'josh@wickedlysmart.com' }
users = {}
users['Kim'] = attributes1
users['John'] = attributes2
users['Josh'] = attributes3

for user in users:
    print("name: ", user, ", attributes: ", users[user])

#user = input("Give a name: ")
#if user in users:
#    print(user, "'s email address is: ", users[user])
#else:
#    print(user, "'s email address not exist.")
