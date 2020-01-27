

smoothies = [ 'coconut', 'strawberry', 'banana', 'tropical', 'acai berry' ]
has_coconut = [ True, False, False, True, False ]

#i = 0
#while i < len(has_coconut):
#    if has_coconut[i]:
#        print(smoothies[i], 'contains coconut')
#    i = i + 1

limmit = len(has_coconut)
for i in range(limmit):
    if has_coconut[i]:
        print(smoothies[i], 'contains coconut')
