

my_phone_book = {} # Use dictionary

my_phone_book['pual'] = '555-1201'
my_phone_book['jenny'] = '867-5309'
my_phone_book['devid'] = '321-6617'
my_phone_book['jamie'] = '771-0091'

names = { 'pual', 'jenny', 'devid', 'jamie' }

for name in names:
    print("name: ", name, ", phone number: ", my_phone_book[name])
