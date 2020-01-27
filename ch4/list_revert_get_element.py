
eighties = [ '', 'duran duran', 'B-52s', 'muse' ]
newwave = [ 'flock of seagulls', 'postal service' ]

remember = eighties[1]

eighties[1] = 'culture club'

hand = newwave[0]

eighties[3] = hand

eighties[0] = eighties[2]

eighties[2] = remember

print(eighties, ", length = ", len(eighties))
#print("eighties last element = ", eighties[len(eighties) - 1])

limmit = -len(eighties)
count = -1
while count != limmit - 1:
    print("eighties[", count, "] = ", eighties[count])
    count -= 1;

