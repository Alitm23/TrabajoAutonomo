####### JUEGO DEL AHORCADO #######

# Importar librería para elegir palabra al azar 
import random

# --- ZONA DE CONFIGURACIÓN Y PALABRAS ---
PALABRAS_FACILES = ["url", "ram", "cpu", "red", "api", "bug"]
PALABRAS_MEDIAS = ["nube", "html", "proxy", "pixel", "virus"]
PALABRAS_DIFICILES = ["interfaz", "algoritmo", "contraseña", "firewall", "malware"]
VOCALES = "aeiou"
CONSONANTES = "bcdfghjklmnpqrstvwxyz"
print("=== BIENVENIDO AL JUEGO DEL AHORCADO ===")


# FUNCION SELECCIONAR PALABRA SEGUN DIFICULTAD
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
    print("Por favor, elige una dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    dificultad = input(">> ")
    if dificultad in ["1", "2", "3"]:
        dificultad_valida = True
    else:
        print("¡Opción no válida! Por favor, elige 1, 2 o 3.")

palabra_secreta = seleccionar_palabra(dificultad)

#FUNCION DIBUJAR AHORCADO
def dibujar_ahorcado(intentos_fallidos):
    """Retorna el dibujo del ahorcado según los intentos fallidos."""
    etapas = [
        """
           -----
           |   |
               |
               |
               |
               |
         ----------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
         ----------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
         ----------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
         ----------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
         ----------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
         ----------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
         ----------
        """
    ]
    return etapas[intentos_fallidos]



# FUNCION MOSTRAR ESTADO DEL JUEGO
def mostrar_estado_juego(progreso):
    print()
    print("Palabra: ", " ".join(progreso))
    return input("Adivina una letra: ").lower() # Pedir al jugador que ingrese una letra
    

# Inicializar variables del juego
intentos = 6  # Máximo de intentos permitidos
intentos_fallidos = 0  # Contador de intentos fallidos
progreso = []  # Lista para guardar letras adivinadas o "_"
letras_adivinadas = []
letras_incorrectas = []
pistas_usadas = 0 
letra = ""

# Llenar progreso con "_" por cada letra de la palabra 
# Usamos un ciclo for para recorrer cada letra de la palabra
for i in range(len(palabra_secreta)):
    progreso.append("_")

print("Adivina una palabra relacionada con el mundo de la tecnología.")


# CICLO PRINCIPAL DEL JUEGO  
while intentos > 0 and "_" in progreso:
    print(dibujar_ahorcado(intentos_fallidos))
    letra = mostrar_estado_juego(progreso)

    # Validar letra ingresada
    if len(letra) != 1 or not letra.isalpha():
        print("Ingresa solo una letra válida.")
        print("Letras incorrectas:", ", ".join(letras_incorrectas))
        print("Intentos restantes:", intentos)
        continue

    # Evitar letras repetidas
    if letra in letras_adivinadas:
        print("Ya ingresaste esa letra antes.")
        print("Letras incorrectas:", ", ".join(letras_incorrectas))
        print("Intentos restantes:", intentos)
        continue

    letras_adivinadas.append(letra)

    # Evaluar letra ingresada
    if letra in palabra_secreta:
        for i, letra_secreta in enumerate(palabra_secreta):
            if letra_secreta == letra:
                progreso[i] = letra
        print("- Letra correcta!")
    else:
        letras_incorrectas.append(letra)
        intentos -= 1
        intentos_fallidos += 1
        print("- Letra incorrecta")

    # Mostrar estado actual del juego
    print(f"- Letras incorrectas: {', '.join(letras_incorrectas)}") # Mostrar letras incorrectas
    print(f"- Intentos restantes: {intentos}") # Mostrar intentos restantes
    print("-----------------------------------")
    if "_" not in progreso:
        break

    # Mostrar opción de pista solo si:
    # 1) tiene al menos 3 fallos
    # 2) no ha usado la pista antes
    # 3) aún faltan al menos 2 letras por descubrir
    if intentos_fallidos >= 3 and pistas_usadas == 0 and "_" in progreso:
        quiere_pista = input("¿Quieres usar una pista? (si/no): ").lower()
        if quiere_pista == 'si':
            if intentos > 1:
                tipo_pista = ""
                while tipo_pista not in ['v', 'c']:
                    tipo_pista = input("¿Pista de vocal (v) o consonante (c)?: ").lower()
                # Buscar y revelar una letra de la pista seleccionada
                pista_encontrada = False
                for i, letra_pista in enumerate(palabra_secreta):
                    if progreso[i] == "_":
                        if tipo_pista == 'v' and letra_pista in VOCALES:
                            progreso[i] = letra_pista
                            pista_encontrada = True
                            break
                        elif tipo_pista == 'c' and letra_pista in CONSONANTES:
                            progreso[i] = letra_pista
                            pista_encontrada = True
                            break
                # Si se encontró una pista, se revela y se descuentan intentos
                if pista_encontrada:
                    print("Pista revelada, pero te cuesta un intento.")
                    intentos -= 1
                    intentos_fallidos += 1
                    pistas_usadas += 1
                    if "_" not in progreso:
                        print("¡Has completado la palabra con ayuda de una pista!")
                        break
                else:
                    print("No quedan letras de ese tipo por revelar.")
            else:
                print("No tienes suficientes intentos para usar una pista.")


# Fin del juego
print(dibujar_ahorcado(intentos_fallidos))
if "_" not in progreso: 
    print("Ganaste!! La palabra es:", palabra_secreta)
else:
    print("Perdiste :( La palabra era:", palabra_secreta)