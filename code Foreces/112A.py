primera = input().lower()
segunda = input().lower()

if len(primera)==len(segunda):
    if primera < segunda:
        print(-1)
    elif segunda< primera :
        print(1)
    elif primera == segunda:
        print(0)