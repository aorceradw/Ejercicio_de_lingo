
# El juego lingo

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
* Aquí he metido el bucle de los 6 intentos, la parte que interactúa con el usuario y los mensajes con logging para que quede más profesional.

La rama `main` tiene todo junto ya funcionando.

## Problemas que tuve

Me pasaron varias cosas durante el desarrollo que me hicieron perder bastante tiempo:

### El .gitignore me ocultaba los archivos
Cuando intentaba subir `lingo.py` y `juego.py` a GitHub, Git me decía que no existían. Resulta que el `.gitignore` estaba configurado para ignorar archivos `.py` o tenía los nombres de mis archivos.

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

### juego.py

```python
import lingo
```
Traigo el archivo `lingo.py` para poder usar su función. Al principio no sabía que había que hacer esto para usar código de otros archivos.

```python
def jugar():
    secreta = "12345"
    intentos = 0
```
Creo la función del juego. La palabra a adivinar es "12345" y empiezo contando los intentos desde 0.

```python
    while intentos < 6:
        print("Intento " + str(intentos + 1) + " de 6")
        apuesta = input("Dime un numero: ")
```
Mientras no llegues a 6 intentos, sigue jugando. El `str()` lo puse porque sino da error al mezclar números con texto. El `+1` es porque si no sale "Intento 0" al usuario.

```python
        if apuesta == secreta:
            print("¡Ole! Has acertado el numero.")
            return
```
Si acierta, le digo que ganó y paro ahí con `return`. Sin el `return` seguía pidiendo intentos aunque ganaras.

```python
        pista = lingo.las_pistas(secreta, apuesta)
        print("Pistas: " + pista)
        intentos = intentos + 1
```
Llamo a la función del otro archivo para que me dé las pistas, las muestro y sumo un intento.

```python
    print("Mal mal ... El numero era " + secreta)
```
Si saliste del bucle sin ganar, perdiste.

```python
if __name__ == "__main__":
    jugar()
```
Esto hace que cuando ejecutes el programa se llame a la función. Sin esto el código no hace nada.

---

### lingo.py

```python
def las_pistas(secreta, intento):
    pista = ""
```
Función que compara las dos palabras. Empiezo con `pista` vacío para ir llenándolo.

```python
    for i in range(5):
        if intento[i] == secreta[i]:
            pista = pista + "[" + intento[i] + "]"
```
Recorro las 5 posiciones. Si la letra coincide exactamente, le pongo corchetes `[X]`.

```python
        elif intento[i] in secreta:
            pista = pista + "(" + intento[i] + ")"
```
Si no coincide pero la letra está en la palabra, le pongo paréntesis `(X)`. El `in` busca si existe esa letra.

```python
        else:
            pista = pista + intento[i]
```
Si no está, la dejo sin nada.

```python
    return pista
```
Devuelvo todas las pistas juntas. Sin esto la función no te da nada de vuelta.

---

## Cosas que me liaron

**¿Por qué strings y no números?**
Probé con `int()` pero era un lío acceder a cada cifra. Con strings puedo hacer `intento[0]` para la primera cifra y ya está.

**¿Qué hace el `in`?**
Tardé en pillarlo. Básicamente busca si una letra está dentro de una palabra, no importa dónde.

**El `return` en jugar()**
Al principio cuando ganabas seguía pidiendo más intentos. Me faltaba el `return` para salir de la función.
