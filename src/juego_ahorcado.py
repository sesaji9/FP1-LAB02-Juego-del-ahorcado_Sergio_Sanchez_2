import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower()
    cadena = cadena.strip()
    cadena = cadena.replace("á","a")
    cadena = cadena.replace("é","e")
    cadena = cadena.replace("í","i")
    cadena = cadena.replace("ó","o")
    cadena = cadena.replace("ú","u")
    cadena = cadena.replace("ü","u")
    return cadena
    # TODO: Implementa esta función (y elimina la instrucción pass)

def enmascarar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    resultado = ""
    for letra in palabra_secreta:
        if letra in letras_usadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado
    # TODO: Implementa esta función (y elimina la instrucción pass)


def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    if "_" not in palabra_enmascarada:
        return True
    else:
        return False
    # TODO: Implementa esta función (y elimina la instrucción pass)
    


# TODO: Implementa la función mostrar_estado
def mostrar_estado(palabra_enmascarada,letras_usadas, intentos_res):
    print(f"Estado: {palabra_enmascarada}")
    " ".join(palabra_enmascarada)
    if letras_usadas == "":
        print("Letras usadas: ninguna")
    else:
        print(f"Letras usadas: {letras_usadas}")
    print(f"Intentos restantes: {intentos_res}")

# TODO: Implementa la función pedir_letra
def pedir_letra(letras_usadas):
    letra = input("Introduce una letra: ").lower()
    while True:
        if letra.isdigit():
            letra = str(input("Debes introducir una letra: "))
        elif len(letra) > 1:
            letra = str(input("Debes introducir una letra: "))
        elif letra in letras_usadas:
            letra = str(input("Esa letra ya la has usado anteriormente, introduce otra: "))
        else:
            return letra

        #REVISAR POR QUE AL PONER "A" SÍ FUNCIONA

# TODO: Implementa la función jugar

# TODO: Escribe el programa principal
