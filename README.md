# Proyecto Lingo

Repositorio con la práctica del juego Lingo en Python. He intentado organizarlo bien usando ramas en Git, aunque no ha sido del todo fácil.

## Cómo está organizado (ejercicios)

He separado el código en dos partes principales:

### Ejercicio 1: La lógica del juego (rama `develop`)
* **Archivo**: `lingo.py`
* Aquí está la función `las_pistas()` que hace todo el trabajo de comparar las letras. Básicamente:
  * Si aciertas letra y posición → `[X]`
  * Si la letra está pero en otro sitio → `(X)` 
  * Si no está → `X`

### Ejercicio 2: El bucle del juego (rama `feature`)
* **Archivo**: `juego.py`
* Aquí he metido el bucle de los 6 intentos, la parte que interactúa con el usuario.
La rama `main` tiene todo junto ya funcionando.

## Problemas que tuve

Me pasaron varias cosas durante el desarrollo que me hicieron perder bastante tiempo:

### El .gitignore me ocultaba los archivos
Cuando intentaba subir `lingo.py` y `juego.py` a GitHub, Git me decía que no existían. Resulta que el `.gitignore` lo configuré para ignorar archivos `.py` o tenía los nombres de mis archivos.

### Caida del SSH 

La conexión con AWS, se me caía todo el tiempo hasta que lo he conseguido arreglar,

Al final lo arreglé forzando a Git a que los subiera:
```bash
git add -f lingo.py
git add -f juego.py
```

### Lío con las ramas y pull requests
Me costó pillar el flujo completo de Git. Creaba la rama pero luego me olvidaba de hacer push y claro, no aparecía nada en GitHub. Cuando hacía los pull requests desde la web, luego tenía que hacer `git pull origin main` en local para no tener conflictos después.

### Archivos basura en el repo
Tenía archivos como `lingo_backup.py` y otras copias que no pintaban nada en el repositorio. Los borré a mano y actualicé Git para dejarlo más limpio.

## Para ejecutar

Si quieres probar el juego:
```bash
python3 juego.py
```

---

## Explicación del código

### juego.py - Explicación línea por línea

```python
import lingo
```
Aquí importo el módulo `lingo.py` que tiene la función de las pistas. Lo hice así para separar la lógica del juego de la interfaz con el usuario.

```python
def jugar():
```
Creo la función principal del juego. Podría haberlo hecho todo suelto, pero me pareció mejor meterlo en una función para poder llamarla cuando quisiera.

```python
    secreta = "12345"
```
La palabra (o número en este caso) que hay que adivinar. Al principio dudé si poner esto como variable global o dentro de la función, pero lo dejé aquí porque si luego quiero hacer que sea aleatorio es más fácil cambiarlo.

```python
    intentos = 0
```
Contador de intentos. Empiezo en 0 y voy sumando cada vez que el usuario prueba.

```python
    print("Tienes 6 intentos para adivinar el numero de 5 cifras.")
```
Mensaje inicial para que el usuario sepa las reglas. Simple y directo.

```python
    while intentos < 6:
```
El bucle principal. Mientras no hayas llegado a 6 intentos, el juego sigue. Al principio pensé en hacer un `for` pero con `while` me resultaba más natural controlar cuándo parar.

```python
        print("Intento " + str(intentos + 1) + " de 6")
```
Muestro en qué intento vas. Aquí tuve que usar `str()` porque `intentos` es un número y no puedes concatenar números con texto directamente. El `+1` es porque empecé contando desde 0, pero para el usuario tiene más sentido ver "Intento 1" en vez de "Intento 0".

```python
        apuesta = input("Dime un numero: ")
```
Capturo lo que escribe el usuario. Python te lo da como string por defecto, así que no hace falta convertir nada.

```python
        if apuesta == secreta:
            print("¡Ole! Has acertado el numero.")
            return
```
Si acierta, le digo que ha ganado y salgo de la función con `return`. Al principio no ponía el `return` y el programa seguía pidiendo más intentos aunque hubieras ganado, así que tuve que añadirlo.

```python
        pista = lingo.las_pistas(secreta, apuesta)
```
Aquí llamo a la función del otro archivo (`lingo.py`) pasándole la palabra secreta y lo que ha escrito el usuario. Me devuelve las pistas en formato string.

```python
        print("Pistas: " + pista)
```
Muestro las pistas al usuario para que vea qué ha acertado.

```python
        intentos = intentos + 1
```
Sumo 1 al contador de intentos. Podría haber puesto `intentos += 1` pero me pareció más claro así.

```python
    print("Mal mal ... El numero era " + secreta)
```
Si sales del bucle sin haber acertado (llegas a 6 intentos), le dices al usuario que ha perdido y cuál era el número.

```python
if __name__ == "__main__":
    jugar()
```
Esto lo puse para que cuando ejecutes el archivo directamente se llame a la función `jugar()`. Si no lo pones, el código está ahí pero no se ejecuta nada. Lo aprendí porque al principio no lo tenía y no entendía por qué no pasaba nada al ejecutar.

---

### lingo.py - Explicación línea por línea

```python
def las_pistas(secreta, intento):
```
Función que recibe dos parámetros: la palabra secreta y el intento del usuario. Devuelve un string con las pistas.

```python
    pista = ""
```
Empiezo con un string vacío donde voy a ir añadiendo las pistas letra por letra.

```python
    for i in range(5):
```
Recorro las 5 posiciones (de 0 a 4). Uso `range(5)` porque el número tiene 5 cifras. Aquí `i` es el índice de la posición que estoy mirando.

```python
        if intento[i] == secreta[i]:
```
Primera comprobación: ¿la letra en la posición `i` del intento es igual que en la misma posición de la palabra secreta? Si sí, es un acierto total.

```python
            pista = pista + "[" + intento[i] + "]"
```
Añado la cifra entre corchetes `[X]` para indicar acierto exacto. Concateno el string anterior + corchete + la cifra + corchete.

```python
        elif intento[i] in secreta:
```
Si no es acierto exacto, compruebo si al menos la cifra está en la palabra secreta (aunque sea en otra posición). El `in` busca si ese carácter existe en algún sitio del string.

```python
            pista = pista + "(" + intento[i] + ")"
```
Añado la cifra entre paréntesis `(X)` para indicar que está pero en otro sitio.

```python
        else:
```
Si no cumple ninguna de las dos condiciones anteriores, significa que la cifra no está en la palabra.

```python
            pista = pista + intento[i]
```
Añado la cifra tal cual, sin corchetes ni paréntesis.

```python
    return pista
```
Devuelvo el string completo con todas las pistas. Este return es importante porque si no la función no te devuelve nada y en `juego.py` no tendrías las pistas para mostrar.

---

## Dudas que tuve al hacerlo

### ¿Por qué todo en strings?
Al principio quería trabajar con números usando `int()`, pero me di cuenta de que para acceder a cada cifra por separado (`intento[i]`) era mucho más fácil si era un string. Además `input()` ya te da un string, así que me evité conversiones raras.

### ¿Por qué dos archivos?
Podría haberlo hecho todo en uno, pero me pareció más limpio separar la lógica (las_pistas) de la interfaz (el bucle y los prints). Así si luego quiero cambiar cómo se muestran las cosas, no toco la lógica del juego.

### El uso de `in` para buscar letras
Me costó un poco entender cómo usar el `in`. Probé varias cosas con prints para ver qué devolvía y al final vi que funcionaba perfecto para saber si un carácter está en un string.

### El `return` en jugar()
Al principio cuando acertabas el número, el programa seguía pidiendo más intentos. Me di cuenta de que necesitaba un `return` para salir de la función en cuanto ganabas.
