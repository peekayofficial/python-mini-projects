users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print('Dave' in emptylist)

# Indexing
print(users[0])
print(users[-2])

# Using a method
print(users.index('Sara'))

# Range of Values
print(users[0:2])
print(users[1:])
print(users[-3:-1])

# Length of the list
print(len(users))

# Adding items to a list using append method
users.append('Percival')
print(users)

# Adding other lists to an existing list
users += ['Tom', 'Jane', 'Morris']
print(users)

# Using extend method
users.extend(['Taps', 'Mike'])
print(users)

# users.extend(data)
# print(users)
