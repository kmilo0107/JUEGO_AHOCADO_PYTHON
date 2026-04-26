import os
import random
personas = {
    "hombres": [
        "Juan", "Carlos", "Luis", "Andres", "Jorge",
        "Camilo", "Felipe", "Santiago", "Daniel", "Sebastian",
        "Mateo", "Alejandro", "David", "Nicolas", "Diego"
    ],
    "mujeres": [
        "Maria", "Laura", "Ana", "Diana", "Paula",
        "Valentina", "Camila", "Sofia", "Isabella", "Juliana",
        "Daniela", "Natalia", "Carolina", "Andrea", "Tatiana"
    ]
}

letra = ""
salir = "y"

#Crea arreglo con tamaño palabra
def mostrar_espacios(palabra):
    relleno = []
    cantidad = len(palabra)
    for i in range(cantidad):
        relleno.insert(i,"_")    
    return relleno

def validacion_juego():
    ciclo = 3
    #elije nombre del diccionario al azar
    categoria = random.choice(list(personas.keys()))
    palabra = random.choice(list(personas[categoria]))
    palabra = palabra.lower()          

    #llama a función para crear arreglo
    relleno = mostrar_espacios(palabra)
    #valida letra ingresada y rellena campos en el arreglo
    #cuenta los espacios libres
    while ciclo > 0:    
        if "_" in relleno:
            letra = input("Ingrese una letra: -->") 
            letra = letra.lower()
            if letra in palabra:
                cont = -1        
                for i in palabra:
                    cont += 1
                    if i == letra:
                        relleno[cont] = letra

                os.system('cls')        
                print(relleno)
            #descuenta intentos permitidos y finaliza juego
            else:
                ciclo -= 1
                os.system('cls')
                print(f"\U0000274C Te quedan {ciclo} intentos... \U0000274C")
                if ciclo == 0:
                    os.system('cls')
                    print("\U0000274C"*26)
                    print("\U0000274C QUE LASTIMA PERDISTE, INTENTALO NUEVAMENTE ¡¡¡ \U0000274C")
                    print("\U0000274C"*26)
                    print(f"\n \U0000274C La palabra era ➡️  {palabra} ⬅️  \U0000274C \n\n")
                    
        #en caso de que sean acertadas las letras y se llene el arreglo realiza else        
        else:
            print("\U00002705"*29)
            print("\U00002705 FELICITACIONES LOGRASTE DESCUBRIR LA PALABRA SECRETA \U00002705")
            print("\U00002705"*29)
            print("\n\n")
            break 
        
#ciclo para repetir juego o salir
while salir == "Y" or salir == "y":
    os.system('cls')
    validacion_juego()
    print("\u2B50"*38)    
    salir = input("\u2B50 Digite 'y' par volver a jugar, de lo contrario digite otro caracter: -->  ")
      
    if salir != "Y" and salir != "y":
        os.system('cls')
        print("\U0001F44B" * 5, " Bye Bye ", "\U0001F44B" * 5)
        break

  
  
  