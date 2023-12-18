import calendar
import os

print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

pregunta = "si"

while pregunta == "si":
    año = int(input("Que año quieres mostrar: "))
    mes = int(input("Que mes quieres mostrar[1-12]:  "))
    
    print(calendar.month(año, mes))
    
    pregunta = input("Quieres mostrar otro?[si/no]: ")
    if pregunta == "si":
        p = input("Quieres limpiar la pantalla[si/no]: ")
        if p == "si":
            os.system('cls' if os.name == 'nt' else 'clear')
        if p == "no":
            p == "si"
    if pregunta == "no":
        print("Hasta otro dia :)")