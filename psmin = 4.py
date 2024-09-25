psmin = 4
psmax = 100
perfectsquares =5
onswitch = True
psmax = int(input("up to what number do you want?"))
while ((psmin < perfectsquares <psmax) & onswitch):
    print(perfectsquares*perfectsquares)
    perfectsquares = perfectsquares +1
    if (perfectsquares*perfectsquares) > psmax:
        onswitch = False
        

