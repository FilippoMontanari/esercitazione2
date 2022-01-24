def fileToDict(fname):
    try:
        f = open(fname, 'r')
    except FileNotFoundError:
        print('Errore, file non trovato:', fname) # messaggio di errore se il file non esiste
        return # esce dalla funzione restituendo None
    lettura = f.read() # legge la stringa dal file
    f.close() # chiude il file
    # creazione di una lista contenente solo i numeri e i due punti (:)
    lista = []
    cont = 0
    for i, ele in enumerate(lettura):
        if(cont>0):
            cont-=1
            continue
        if ele not in [' ', '\n']:
            if ele!=':' and (i+1)<len(lettura):
                while lettura[i+cont+1] not in [' ', '\n', ':']:
                    ele+=lettura[i+cont+1]
                    cont+=1
                    if (i+cont+1) >= len(lettura):
                        break
            if ele!=':':
                try:
                    ele = int(ele)
                except ValueError:
                    ele = 0 # se l'elemento non fosse intero, viene posto = 0
            lista.append(ele)
    # print(lista)
    # creazione del dizionario chiavi (numeri interi) : valori (liste di interi)
    ris = {}
    for i, ele in enumerate(lista):
        flagKey = False
        if (i+1) < len(lista):
            if ele!=':' and lista[i+1]==':':
                chiave = ele
                ris[chiave] = []
                flagKey = True
        if ele!=':' and flagKey==False:
            ris[chiave].append(ele)
    return ris

print('ftesto10_1.txt :', fileToDict('ftesto10_1.txt'))
print('')
print('ftesto10_2.txt :', fileToDict('ftesto10_2.txt'))
print('')
print('ftesto10_3.txt :', fileToDict('ftesto10_3.txt'))