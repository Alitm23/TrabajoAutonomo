import random

palabras = ["url", "interfaz", "algoritmo", "contraseña", "nube"]
indice_azar = random.randint(0, len(palabras) - 1)
palabra_secreta = palabras[indice_azar]

intentos = 6
progreso = []
letras_adivinadas = []

for i in range(len(palabra_secreta)):
    progreso.append("_")

print("=== BIENVENIDO AL JUEGO DEL AHORCADO ===")
print("Adivina una palabra relacionada con la tecnología.")
print("Palabra: ", " ".join(progreso))

while intentos > 0 and "_" in progreso:
    letra = input("Adivina una letra: ").lower()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Ingresa solo una letra válida.")
    
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra antes.")
    
    letras_adivinadas.append(letra)

    letra_encontrada = False
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            progreso[i] = letra
            letra_encontrada = True
    
    if letra_encontrada:
        print("Letra correcta!")
    else:
        intentos = intentos - 1
        print("La letra es incorrecta. Intentos restantes:", intentos)
    
    print("Palabra: ", " ".join(progreso))

if "_" not in progreso:
    print("Ganaste!! La palabra es:", palabra_secreta)
else:
    print("Perdiste :( La palabra era:", palabra_secreta)



    