####### JUEGO DEL AHORCADO #######

# Importar librería para elegir palabra al azar 
import random

# Crear una lista de palabras relacionadas con tecnología
palabras = ["url", "interfaz", "algoritmo", "contraseña", "nube"]

# Elegir una palabra al azar de la lista
# Usamos len(palabras) para obtener tamaño de la lista
indice_azar = random.randint(0, len(palabras) - 1)
palabra_secreta = palabras[indice_azar]

# Inicializar variables del juego
intentos = 6  # Máximo de intentos permitidos
progreso = []  # Lista para guardar letras adivinadas o "_"
letras_adivinadas = []  # Lista para evitar repetir letras

# Llenar progreso con "_" por cada letra de la palabra 
# Usamos un ciclo for para recorrer cada letra de la palabra
for i in range(len(palabra_secreta)):
    progreso.append("_")

# Mostrar mensaje de bienvenida 
print("=== BIENVENIDO AL JUEGO DEL AHORCADO ===")
print("Adivina una palabra relacionada con la tecnología.")
print("Palabra: ", " ".join(progreso))

# Ciclo principal del juego 
# Se repite mientras haya intentos y la palabra no esté completa
while intentos > 0 and "_" in progreso:
    
    # Pedir una letra al usuario
    letra = input("Adivina una letra: ").lower()

    # Validar que sea una sola letra 
    if len(letra) != 1 or not letra.isalpha():
        print("Ingresa solo una letra válida.")
        continue  # Volver al inicio del ciclo

    # Verificar si ya se adivinó esa letra 
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra antes.")
        continue  # Volver al inicio del ciclo

    # Agregar letra a la lista de letras ya usadas
    letras_adivinadas.append(letra)

    # Verificar si la letra está en la palabra secreta
    letra_encontrada = False  # Bandera para saber si acertó

    # Usar un ciclo for para recorrer cada letra de la palabra
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:  # Operador relacional 
            progreso[i] = letra  # Reemplazar "_" por la letra
            letra_encontrada = True  # Marcar que encontró al menos una

    # Mostrar resultado de la adivinanza 
    if letra_encontrada:
        print("Letra correcta!")
    else:
        intentos = intentos - 1  # Restar un intento
        print("La letra es incorrecta. Intentos restantes:", intentos)

    # Mostrar progreso actual
    print("Palabra: ", " ".join(progreso))

# Fin del juego
# Verificar si ganó o perdió
if "_" not in progreso:  # Operador relacional !=
    print("Ganaste!! La palabra es:", palabra_secreta)
else:
    print("Perdiste :( La palabra era:", palabra_secreta)