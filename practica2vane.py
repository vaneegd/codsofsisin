#calcular en base a un valor dado por el usuario 
#su equivalencia en las diferentes divisas definidas

yuan = 2.81
yen = 0.13 
dólar = 20.54 
euro = 21.29
libra = 25.56

pesos = input("ingresa la cantidad de pesos a convertir: ")

pesos = int(pesos) 

print("tus pesos son %.2f yenes" %(pesos/yuan))

print(pesos/yen)

print(pesos/dólar)

print(pesos/euro)

print(pesos/libra)