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
        'friends' : ['Kim'] }

users = {}
users['Kim'] = attributes1
users['John'] = attributes2
users['Josh'] = attributes3

max = 1000
for name in users:
    user = users[name]
    friends = user['friends']

    if len(friends) < max:
        most_anti_social = name
        max = len(friends)

print("The most_anti_social user is: ", most_anti_social)
