print('привет')
with open('data.txt', 'a') as f:
    f.writelines('строчка\n')
print('добавили строчку')