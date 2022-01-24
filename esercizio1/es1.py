import json

def es32(fname1):
    try:
        f = open(fname1, 'r')
    except FileNotFoundError:
        print('Errore, file non trovato:', fname1) # messaggio di errore se il file non esiste
        return # esce dalla funzione restituendo None
    lettura = json.load(f) # legge la lista dal file
    print(fname1 + ':', lettura)
    f.close() # chiude il file
    lista = []
    for ele in lettura:
        sommaP=0
        sommaD=0
        for cifra in ele:
            try:
                cifra_int = int(cifra)
            except ValueError:
                cifra_int = 0 # se l'elemento non fosse intero, viene posto = 0
            if cifra_int%2 == 0:
                sommaP+=cifra_int
            else:
                sommaD+=cifra_int
        lista.append((sommaD, sommaP))
    return lista

print('Lista ris:', es32('file1.json'))
print('')
print('Lista ris:', es32('file2.json'))