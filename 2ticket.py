lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
j = 0
lst = ' " '.join(lst)
lst2 = ''
print(lst)  # проверка разделителя
while i < len(lst)-1:
    if lst[i-1] >= '0' and lst[i-1] <= '9' or lst[i+1] >= '0' and lst[i+1] <= '9':
        lst2 = lst2 + lst[i]
    elif lst[i] >= '0' and lst[i] <= '9':
        lst2 = lst2 + '0' + lst[i]
    else:
        lst2 = lst2+lst[i]
    i+=1
lst2 = lst2 + lst[i]
# print(lst2) проверка что строка адекватна
lst = ''  # обнуляем первую строку
i = 0
while i < len(lst2) - 2:
    if (lst2[i] == '"' and (lst2[i+2] == '+' or lst2[i+2] == '-')) or (lst2[i] == '"' and (lst2[i+2] >= '0' and lst2[i+2] <= '9')):
        lst = lst + lst2[i]
        i += 1
    if lst2[i] == '"' and (lst2[i - 2] <= '0' or lst2[i - 2] >= '9') and (lst2[i + 2] <= '0' or lst2[i + 2] >= '9'):
        i += 1
    else:
        lst = lst + lst2[i]
        i+=1
lst = lst + lst2[i] + lst2[i+1]
print(lst) # проверка строки
