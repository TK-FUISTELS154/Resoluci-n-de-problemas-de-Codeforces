letra = input()

mayusculas = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
minusculas = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}

max_mayusculas = len(set(letra) & mayusculas)
max_minusculas = len(set & minusculas)

if max_minusculas<max_mayusculas:
    print(letra.upper())
elif max_mayusculas<=max_minusculas:
    print(letra.lower())