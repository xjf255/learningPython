"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

def battle_recursive(lista_a: list[int], lista_b: list[int], accumulator = ""):
  if not lista_a and not lista_b:
    return accumulator

  a = lista_a[0]
  b = lista_b[0]

  accumulator_value = accumulator.split("a")[0] if "a" in accumulator else accumulator.split("b")[0]
  if accumulator_value:
    a += int(accumulator_value) if "a" in accumulator else 0
    b += int(accumulator_value) if "b" in accumulator else 0
  accumulator = "x"

  if a > b:
    accumulator = f"{a - b}a"
    return battle_recursive(lista_a[1:], lista_b[1:], accumulator)
  elif a < b:
    accumulator = f"{b-a}b"
    return battle_recursive(lista_a[1:], lista_b[1:], accumulator)
  else:
    return battle_recursive(lista_a[1:], lista_b[1:], accumulator)

def battle(lista_a: list[int], lista_b: list[int]) -> str:
  return battle_recursive(lista_a, lista_b, "")

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"
print(resultado)

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"
print(resultado)

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"