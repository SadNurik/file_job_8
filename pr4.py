t_words = []
with open('C:\Python\слайды\python.txt','r') as file:
    for i in file.read().split():
        if ('t' or 'T') in i:
            t_words.append(i)
    print('Слова в которых есть буква T : ',', '.join(t_words))