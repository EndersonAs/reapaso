#Extraer los numeros mayores a 15 de una lista y guardarlos en otra lista

myList = [10, 20, 5, 200, 9, 15, 3, 40]
myList2=[]

print(myList)

if myList[0] >= 15:
  myList2.append(myList[0])
if myList[1] >= 15:
  myList2.append(myList[1])
if myList[2] >= 15:
  myList2.append(myList[2])
if myList[3] >= 15:
  myList2.append(myList[3])
if myList[4] >= 15:
  myList2.append(myList[4])
if myList[5] >= 15:
  myList2.append(myList[5])
if myList[6] >= 15:
  myList2.append(myList[6])
if myList[7] >= 15:
  myList2.append(myList[7])

print(myList2)