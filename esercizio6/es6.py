import json

def esercizio_6(fname1, fname2):
    try:
        f = open(fname1, 'r')
    except FileNotFoundError:
        print('Errore, file non trovato:', fname1) # messaggio di errore se il file non esiste
        return # esce dalla funzione restituendo None
    lettura = json.load(f) # legge la lista di liste dal file
    # print(fname1 + ':', lettura)
    f.close() # chiude il file
    
    # creazione di un insieme contenente i simboli che compaiono nel quadrato latino
    simboli = set()
    for riga in lettura:
        for simbolo in riga:
            simboli.add(simbolo) # set non accetta valori duplicati, quindi non c'è bisogno di fare controlli
    
    # completamento righe (con l'aggiunta di una colonna)
    for i, riga in enumerate(lettura):
        flag = [False for i in range(len(simboli))] # inizializza tutti i flag a False
        # trova i simboli già usati nella riga
        for colonna in riga:
            for pos, simbolo in enumerate(simboli):
                if colonna==simbolo:
                    flag[pos] = True # se il simbolo è già stato utilizzato nella riga, il flag corrispondente diventa True
        # trova e aggiunge simbolo mancante nella riga
        for pos, simbolo in enumerate(simboli):
            if not flag[pos]:
                lettura[i].append(simbolo)
    
    # completamento colonne (con l'aggiunta di una riga)
    lettura.append([])
    for j in range(len(lettura)):
        flag = [False for i in range(len(simboli))] # inizializza tutti i flag a False
        # trova i simboli già usati nella colonna j
        for riga in lettura:
            if len(riga) < len(lettura):
                break
            for pos, simbolo in enumerate(simboli):
                if riga[j]==simbolo:
                    flag[pos] = True # se il simbolo è già stato utilizzato nella riga, il flag corrispondente diventa True
        # trova e aggiunge simbolo mancante nella colonna
        for pos, simbolo in enumerate(simboli):
            if not flag[pos]:
                lettura[len(lettura)-1].append(simbolo)
                
    # salvataggio del quadrato latino completo nel secondo file
    with open(fname2, 'w') as fw:
        json.dump(lettura, fw)
    
    return simboli # restituisce l'insieme dei simboli che compaiono nel quadrato latino

print('Simboli utilizzati (file3.json):', esercizio_6('file3.json', 'file3_completo.json'))
print('Simboli utilizzati (file4.json):', esercizio_6('file4.json', 'file4_completo.json'))