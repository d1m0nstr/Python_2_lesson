lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
lst2 =''
lst3 =''
lst4 = list(range(len(lst)))
i = 0
j = 0
while i < len(lst):
    lst2 = lst[i]
    j = len(lst2) - 1
    while j > 0 and lst2[j]!= ' ':
        lst3 = lst2[j]+lst3
        j-=1
    lst4[i]=lst3.capitalize()
    i += 1
    lst3 = ''
print (lst4)  # проверка что имена записаны
i = 0
while i<len(lst4):
    print(f"Привет {lst4[i]}")
    i+=1