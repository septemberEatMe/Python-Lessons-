user = {'name':'Vitaliy',
        'first':'Alex',
        'second':'Lena'
}

for key,value in user.items():
    print('Key:', key)
    print('Value:', value)
    print(' ' *100)


favourite_languages = {'Alex':'C++',
                       'Sara':'Java',
                       'Lena':'C#',
                       'Pavel Cat':'Ruby',
                       'John Snow':'Python'
                       }
                    
for name,language in favourite_languages.items():
    print(name.title(),'s favourite languages:', language)