n = input("Введите n") # Строка текста
n = int(n) #  Строку преобразует в целое число
for i in range(1 , n+1 ):
    if i > 5 and i <= 9: 
        continue # Пропусти тело ниже  
    if i > 17 and i <= 37:
        continue
    if i > 78 and i <= 87:
        continue
    print(i,end = " ")
