import lingo  

def jugar():
    secreta = "12345"
    intentos = 0

    print("Tienes 6 intentos para adivinar el numero de 5 cifras.")

    while intentos < 6:
        print("Intento " + str(intentos + 1) + " de 6")
        apuesta = input("Dime un numero: ")
        
        if apuesta == secreta:
            print("¡Ole! Has acertado el numero.")
            return 
        
        pista = lingo.las_pistas(secreta, apuesta)
        print("Pistas: " + pista)
        intentos = intentos + 1

    print("Mal mal ... El numero era " + secreta)
if __name__ == "__main__":
    jugar()