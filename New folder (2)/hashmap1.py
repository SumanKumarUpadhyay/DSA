hp = {}
hp['suman'] = 100
hp['base_language'] = 'python'
hp['language'] = ['java', 'c++', 'python']

print(hp) # {'suman': 100, 'base_language': 'python', 'language': ['java', 'c++', 'python']}
print(hp['language']) # ['java', 'c++', 'python']
print(hp['language'][0]) # java

# delete a key value pair
del hp['base_language']
print(hp) # {'suman': 100, 'language': ['java', 'c++', 'python']}

popped_value = hp.pop('suman')
print(popped_value) # 100
print(hp) # {'language': ['java', 'c++', 'python']}

# check if a key is present in the dictionary
print('language' in hp)

# iterate through dictionary
for key in hp:
    print(key, hp[key])

