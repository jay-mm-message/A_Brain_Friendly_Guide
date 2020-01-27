
def drink_me(param):
    msg = 'Drinking ' + param + ' glass'
    print(msg)
    param = 'empty'
    print('<drink_me> param: ', param)

glass = 'full'
drink_me(glass)
print('<gloable> The glass is', glass)
