
cost = [55.8, 46.51, 97, 1.33, 2, 22, 44.2, 5.01, 6.22, 44.22, 4.4, 2.4, 4, 4, 4, 33.4, 44, 5, 6.09, 6.66]
i = 0
while i < len(cost):
    cost[i] = format(cost[i],'.2f')
    i+=1
print(cost)
str1 = ''
str2 = ''
i=0
while i<len(cost):
    str1 = str(cost[i])+ ', ' + str1
    i+=1
print(str1)  #проверка что цены работают
i=0
while i < len(str1)-2:
    if str1[i+1] == '.':
       str2 = str2 + str1[i] + ' руб '
       i+=2
    elif str1[i+1] == ',':
        str2 = str2 + str1[i] + ' коп'
        i+=1
    else:
        str2 = str2 + str1[i]
        i+=1
print (str2)


