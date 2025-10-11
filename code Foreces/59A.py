letra = input()
mayusculas = sum(1 for c in letra if c.isupper())
minusculas = sum(1 for c in letra if c.islower())

if mayusculas > minusculas:
    print(letra.upper())
else:
    print(letra.lower())