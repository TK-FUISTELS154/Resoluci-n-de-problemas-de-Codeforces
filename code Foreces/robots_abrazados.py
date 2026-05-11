def verificar_robots(robots):
    salida = robots
    while '[]' in salida or '{}' in salida:
        salida = salida.replace('{}', '')
        salida = salida.replace('[]', '')

    return True if salida == '' else False

robots = input()
if verificar_robots(robots):
    print("YES")
else:
    print("NO")
