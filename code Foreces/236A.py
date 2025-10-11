abecedario = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}


usuario = set(input())
if len(abecedario & usuario)%2==0:
    print ("CHAT WITH HER!")
else:
    print( "IGNORE HIM!")