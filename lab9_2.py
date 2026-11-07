Count = 0
meetA = False
meetL = False
while True: 
    name = input()
    # Если имя пустое, тогда длина имени 0 - выйдем из цикла break
    if len(name) == 0:
        break
    if name == "Levon":
        # print("Встретили ", name)
        meetL = True
    if meetA and not meetL:
        Count+=1 # Каждый раз добавляем единичку Count=Count+1
    #print(name, Count)
    if name == "Alexandra":
       # print("Встретили ", name)
        meetA = True
    # Выйти из условия сдвиг на четыре пробела
   
print(Count)

    

    

