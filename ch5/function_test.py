
balance = 10500
camera_on = True

def steal(balance, amount):
    global camera_no
    camera_no = False

    if (amount < balance):
        balance = balance - amount

    return amount
    camera_no = True

print("balance : ", balance)
proceeds = steal(balance, 1250)
print("Criminal: you stole", proceeds)
print("balance : ", balance)
