ab = {
    'swaroop':'swaroop@swaroopch.com',
    'Larry'  :'lay@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spmmer':'spammer@hotmail.com'
}
print("swaroop's address is",ab['swaroop'])

del ab['Spmmer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name,adress in ab.items():
    print('Contact {} at {}'.format(name,adress))

ab['Guido'] = 'guido@python.org'


if 'Guido' in ab:#用 if in 来检查是否存在
    print('\nGuido\'s adress is ',ab['Guido'])
