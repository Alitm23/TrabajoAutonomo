####### JUEGO DEL AHORCADO #######

# Importar librería para elegir palabra al azar 
import random

# --- ZONA DE CONFIGURACIÓN Y PALABRAS ---
PALABRAS_FACILES = ["url", "ram", "cpu", "red", "api", "bug"]
PALABRAS_MEDIAS = ["nube", "html", "proxy", "pixel", "virus"]
PALABRAS_DIFICILES = ["interfaz", "algoritmo", "contraseña", "firewall", "malware"]

VOCALES = "aeiou"
CONSONANTES = "bcdfghjklmnpqrstvwxyz"

# FUNCIONES
def seleccionar_palabra(dificultad):
    if dificultad == "1":
        return random.choice(PALABRAS_FACILES)
    elif dificultad == "2":
        return random.choice(PALABRAS_MEDIAS)
    elif dificultad == "3":
        return random.choice(PALABRAS_DIFICILES)
dificultad_valida = False
dificultad = ""
while dificultad_valida == False:
    print()
    print("Elige una dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    dificultad = input("> ")
    if dificultad == "1" or dificultad == "2" or dificultad == "3":
        dificultad_valida = True
    else:
        print("¡Opción no válida! Por favor, elige 1, 2 o 3.")

palabra_secreta = seleccionar_palabra(dificultad)


def dibujar_ahorcado(intentos_fallidos):
    print()
    if intentos_fallidos == 0:
        print("   -----")
        print("   |   |")
        print("       |")
        print("       |")
        print("       |")
        print("       |")
        print(" ----------")
    elif intentos_fallidos == 1:
        print("   -----")
        print("   |   |")
        print("   O   |")
        print("       |")
        print("       |")
        print("       |")
        print(" ----------")
    elif intentos_fallidos == 2:
        print("   -----")
        print("   |   |")
        print("   O   |")
        print("   |   |")
        print("       |")
        print("       |")
        print(" ----------")
    elif intentos_fallidos == 3:
        print("   -----")
        print("   |   |")
        print("   O   |")
        print("  /|   |")
        print("       |")
        print("       |")
        print(" ----------")
    elif intentos_fallidos == 4:
        print("   -----")
        print("   |   |")
        print("   O   |")
        print("  /|\  |")
        print("       |")
        print("       |")
        print(" ----------")
    elif intentos_fallidos == 5:
        print("   -----")
        print("   |   |")
        print("   O   |")
        print("  /|\  |")
        print("  /    |")
        print("       |")
        print(" ----------")
    elif intentos_fallidos == 6:
        print("   -----")
        print("   |   |")
        print("   O   |")
        print("  /|\  |")
        print("  / \  |")
        print("       |")
        print(" ----------")

# Inicializar variables del juego
intentos = 6  # Máximo de intentos permitidos
intentos_fallidos = 0  # Contador de intentos fallidos
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
    dibujar_ahorcado(intentos_fallidos)
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
        intentos = intentos - 1
        intentos_fallidos = intentos_fallidos + 1  # Restar un intento
        print("La letra es incorrecta. Intentos restantes:", intentos)

    # Mostrar progreso actual
    print("Palabra: ", " ".join(progreso))

# Fin del juego
# Verificar si ganó o perdió
if "_" not in progreso:  # Operador relacional !=
    print("Ganaste!! La palabra es:", palabra_secreta)
else:
    print("Perdiste :( La palabra era:", palabra_secreta)