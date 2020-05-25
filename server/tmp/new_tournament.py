#Simulatore di Tornei a 4 squadre - Versione 0.7
# Modifiche: Semplificando sistema di partite

import random

#Messaggi 
print('Benvenuti nel simulatore di tornei')
ty_message = 'Grazie per aver giocato con noi'

#Funzione con tutti i dati delle squadre
def classifica(torneo):
    return torneo.get('punti')

#Lista con i dati delle squadre
torneo = {
    'squadre' : [
        {
            'nome' : input('Scegli il nome della prima squadra '),
            'punti' : 0,
            'partite' : 0,
            'gol_fatti' : 0,
            'gol_subiti' : 0,
            'differenza_reti' : 0
        },
        {
            'nome' : input('Scegli il nome della seconda squadra '),
            'punti': 0,
            'partite': 0,
            'gol_fatti' : 0,
            'gol_subiti' : 0,
            'differenza_reti' : 0
        },
        {
            'nome' : input('Scegli il nome della terza squadra '),
            'punti' : 0,
            'partite' : 0,
            'gol_fatti' : 0,
            'gol_subiti' : 0,
            'differenza_reti' :0
        },
        {
            'nome' : input('Scegli il nome della quarta squadra '),
            'punti': 0,
            'partite' : 0,
            'gol_fatti' : 0,
            'gol_subiti' : 0,
            'differenza_reti' : 0
        }
    ]
    
}

#Printa una lista dei nomi delle squadre con un ciclo for
print('Le squadre che hai scelto sono:')
for k in range(0,4):
    lista_squadre = torneo['squadre'][k]['nome']
    print(lista_squadre)
    
#Creo una lista con le partite giocate
partite_giocate = []
    
    
play_game = input('Iniziare la simulazione? Digita S per si, N per No (S/N)')
if play_game.lower() == 's':
    game_on = True
else:       
    game_on = False
    print('Il torneo è incompleto, ma '+ty_message.lower())

#Numero della giornata
p = 1

while game_on:
    
    #Giornata
    print('Giornata '+ str(p))      

    
    #Creo una lista con i soli nomi delle squadre con il ciclo for
    squadre_random = []
    for k in range(0,4):
        squadre_random.append(torneo['squadre'][k]['nome'])
    
    
    #### NUOVE CONDIZIONI PER I SORTEGGI
    
    
    #Nuove variabili per le partite e i gol
    new_partite = [squadre_random[random.randint(0,3)], squadre_random[random.randint(0,3)], squadre_random[random.randint(0,3)], squadre_random[random.randint(0,3)], ]
    new_goals = [random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4)]

    #Verifico che non siano state sorteggiate squadre uguali nè partite uguali
    while len(new_partite) > len(set(new_partite)):
            new_partite = [squadre_random[random.randint(0,3)], squadre_random[random.randint(0,3)], squadre_random[random.randint(0,3)], squadre_random[random.randint(0,3)], ]
            while new_partite[0]+' - '+new_partite[1] in partite_giocate or new_partite[1]+' - '+new_partite[0] in partite_giocate or new_partite[2]+' - '+new_partite[3] in partite_giocate or new_partite[3]+' - '+new_partite[2] in partite_giocate:
                new_partite = [squadre_random[random.randint(0,3)], squadre_random[random.randint(0,3)], squadre_random[random.randint(0,3)], squadre_random[random.randint(0,3)], ]
    
    #Aggiorno la lista vuota delle partite giocate
    partite_giornata = [new_partite[0]+' - '+new_partite[1], new_partite[2]+' - '+new_partite[3]]
    partite_giocate.extend(partite_giornata)
    
    #Partite della giornata
    print('Partite della giornata: \n'+partite_giornata[0]+'\n'+partite_giornata[1])
    
    #Inizio della giornata da far scegliere all'utente
    play_match = input('Simulare la giornata numero '+str(p)+'? Digita S per Si, N per NO (S/N)')
    if play_match.lower() == 's':
        match = True
    else:
        match = False

    if not match:
        game_on = False
        print('Il torneo è incompleto, ma '+ty_message.lower())
        
    else:
        #Risultati delle partite
        partite_end = [partite_giornata[0]+' '+str(new_goals[0])+' - '+str(new_goals[1]), partite_giornata[1]+' '+str(new_goals[2])+' - '+str(new_goals[3])]

        #Stampo i risultati delle partite
        print('Risultati della giornata: \n'+partite_end[0]+'\n'+partite_end[1])
        
        #Assegno le partite giocare
        for x in range(0,4):
            torneo['squadre'][x]['partite'] = torneo['squadre'][x]['partite']+1
            
        #Condizioni per assegnare i punti, i gol e la differenza reti
        for m in range(0,4):
            for n in range(0,4):
                if m == 0:
                    o = 1
                elif m == 1:
                    o = 0
                elif m == 2:
                    o = 3
                else:
                    o = 2

                if new_partite[m] == torneo['squadre'][n]['nome']:
                    
                    #Assegno i gol alle squadre
                    torneo['squadre'][n]['gol_fatti'] = torneo['squadre'][n]['gol_fatti'] + new_goals[m]
                    torneo['squadre'][n]['gol_subiti'] = torneo['squadre'][n]['gol_subiti'] + new_goals[o]
                    
                    #Assegno la differenza reti
                    torneo['squadre'][n]['differenza_reti'] = torneo['squadre'][n]['gol_fatti'] - torneo['squadre'][n]['gol_subiti']
                    
                    #Assegno i punti alle squadre
                    if new_goals[m] > new_goals[o]:
                        torneo['squadre'][n]['punti'] = torneo['squadre'][n]['punti']+3

                    elif new_goals[m] == new_goals[o]:
                        torneo['squadre'][n]['punti'] = torneo['squadre'][n]['punti']+1

                    else:
                        pass
    
    
    ### FINE NUOVE CONDIZIONI PER I SORTEGGI
    
   
        #Titolo classifica
        if torneo['squadre'][0]['partite'] == 3:
            print('Classifica finale')
        else:
            print('Classifica dopo la giornata numero '+str(p))

        #Ciclo per ordinare la classifica in ordine di punti
        for i in range(0,4):
            torneo['squadre'].sort(key=classifica, reverse=True)

            nome_squadra = torneo['squadre'][i]['nome']
            punti_squadra = torneo['squadre'][i]['punti']
            partite_squadra = torneo['squadre'][i]['partite']
            fatti_squadra = torneo['squadre'][i]['gol_fatti']
            subiti_squadra = torneo['squadre'][i]['gol_subiti']
            diff_reti = torneo['squadre'][i]['differenza_reti']

            print(nome_squadra+' '+str(punti_squadra)+' punti in '+str(partite_squadra)+' partite con '+str(fatti_squadra)+' gol fatti e '+str(subiti_squadra)+' gol subiti e differenza reti di '+"%+d" % (diff_reti))
            

        #Aumento il numero della giornata
        p = p+1

        #Condizioni per la fine del torneo
        if torneo['squadre'][0]['partite'] == 3:
            
            #Verifico che non ci siano squadre a pari punti
            if torneo['squadre'][0]['punti'] != torneo['squadre'][1]['punti']:
                vincitore_singolo = True
                vincitore = torneo['squadre'][0]['nome']
                punti_vincitore = torneo['squadre'][0]['punti']  

            else:
                vincitore_singolo = False
                pari_merito = [torneo['squadre'][0]['nome']]
                punti_vincitore = torneo['squadre'][0]['punti']
                for z in range(1,4):
                    if torneo['squadre'][0]['punti'] == torneo['squadre'][z]['punti']:
                        pari_merito.append(torneo['squadre'][z]['nome'])
            
            #Se c'è solo un vincitore
            if vincitore_singolo:
                print(vincitore+' vince il torneo con '+str(punti_vincitore)+' punti')
            
            #Se ci sono più squadre allo stesso punteggio
            else:
                if len(pari_merito) == 2:
                    print('2 squadre hanno vinto il torneo:')
                    print(pari_merito[0]+' e '+pari_merito[1]+' hanno vinto con '+str(punti_vincitore)+' punti')
                    #Chiede se effettuare uno spareggio
                    spareggio = input('Due squadre sono prime a pari merito. Premi S per procedere con uno spareggio, N per terminare il torneo in parità (S/N)')
                    if spareggio.lower() == 'n':
                        game_on = False
                    else:
                        print('La finale è tra '+pari_merito[0]+' e '+pari_merito[1])
                        #Conferma di disputa della finale
                        finale = input('Disputare la finale spareggio? Premi S per si, N per no (S/N)')
                        if finale.lower() == 's':
                            #Gol della finale
                            finale_goals = [random.randint(0,4), random.randint(0,4)]
                            while finale_goals[0] == finale_goals[1]:
                                finale_goals = [random.randint(0,4), random.randint(0,4)]
                            #Printa il risultato della finale
                            print('La finale è terminata: '+pari_merito[0]+' - '+pari_merito[1]+' '+str(finale_goals[0])+' - '+str(finale_goals[1]))
                            #Decreto il vincitore
                            if finale_goals[0] > finale_goals[1]:
                                print('Il vincitore del torneo è '+pari_merito[0]+' dopo aver battuto in finale '+pari_merito[1])
                                game_on = False
                            else:
                                print('Il vincitore del torneo è '+pari_merito[1]+' dopo aver battuto in finale '+pari_merito[0])
                                game_on = False
                    
            
                        
                        else:
                            game_on = False

                        
                    
                    
                    
                elif len(pari_merito) == 3:
                    print('3 squadre hanno vinto il torneo:')
                    print(pari_merito[0]+', '+pari_merito[1]+' e '+pari_merito[2]+' hanno vinto con '+str(punti_vincitore)+' punti')
                else:
                    print('Tutte le squadre hanno lo stesso punteggio:')
                    print(pari_merito[0]+', '+pari_merito[1]+', '+pari_merito[2]+' e '+pari_merito[3]+' hanno vinto con '+str(punti_vincitore)+' punti')
                    
            #Messaggio di fine indipendentemente dall'esito
            print('Fine del torneo')
            game_on = False
            print(ty_message)
        else:
            #Proseguire o meno il torneo con la giornata successiva
            going_on = input('Proseguire con la giornata numero '+str(p)+'? Digita S per Si, N per NO (S/N)')
            if going_on.lower() == 's':
                game_on = True
            else:
                game_on = False
                print('Il torneo è incompleto, ma '+ty_message.lower())
                match = False


                

                

### PROSSIME FUNZIONI DA IMPLEMENTARE ###
#Spareggio se una o più squadre sono a pari punti - FATTO solo per pari merito di 2 squadre
#Differenza reti - FATTO
#Numero di squadre definito dall'utente (4 o 8 o 16 max)
#Gironi + Eliminazione diretta?
