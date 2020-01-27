

def get_arribute(query, default):
    question = query + "[" + default +"]? "
    answer = input(question)
    if answer == '':
        answer = default
    return answer

msg = "You chose"
hair = get_arribute("What color hair", "brown")
print(msg, hair)

hair_lenght = get_arribute("What hair length", "short")
print(msg, hair_lenght)

eyes = get_arribute("What eye color", "blue")
print(msg, eyes)

gender = get_arribute("What gender", "female")
print(msg, gender)

glasses = get_arribute("Has glasses", "no")
print(msg, glasses)

beard = get_arribute("Has beard", "no")
print(msg, beard)
