import random

print('Benvenuti nel simulatore di tornei')

ty_message = 'Grazie per aver giocato con noi'

flatten = lambda l: [item for sublist in l for item in sublist]

def classifica(torneo):
    return torneo.get('punti')

def goal(to_number, from_number = 0):
        return random.randint(from_number,to_number);

def get_squadra(squadre):

        return squadre[random.randint(0,len(squadre) -1)]['nome'];

def get_partita_giocata(squadra_one, squadra_two):
        return f"""{squadra_one}-{squadra_two}"""

def get_partite(squadre, partite_giocate):
    partite = set([get_squadra(squadre) for i in range(0, len(squadre))])
    partite = list(partite)
    if len(partite) %2 != 0:
        return get_partite(squadre, partite_giocate)
    # genera le possibili partite giocabili 
    partite_giocate_tmp = set(flatten([[get_partita_giocata(partite[i], partite[i + 1]), get_partita_giocata(partite[i + 1], partite[i])] for i in range(0, len(partite) - 1)]))
    # Make sure there are no duplicates between the one already played and the one calculated here
    partite_giocate_intersection = partite_giocate_tmp.intersection(partite_giocate)
    # Ripeti il calcolo se ci sono duplicati
    if len(partite_giocate_intersection) != 0:
        return get_partite(squadre, partite_giocate)

    return partite

game_on = None

def play(is_game_on = None):
    global game_on 
    if game_on is None and is_game_on is None:
        play_game = input('Iniziare la simulazione? Digita S per si, N per No (S/N)')
        game_on = play_game.lower() == 's'
    elif is_game_on is not None:
        game_on = is_game_on

    if game_on is False:
        print('Il torneo è incompleto, ma '+ty_message.lower())

    return game_on


def init_squadra():
    return {
            'nome' : input('Scegli il nome della prima squadra '),
            'punti' : 0,
            'partite' : 0,
            'gol_fatti' : 0,
            'gol_subiti' : 0,
            'differenza_reti' : 0
        }

torneo = {
    'squadre': []
}
giornata = 1
partite_giocate = []


# scegli un numero pari tra 2 e 10
for k in range(0, random.randrange(2, 10, 2)):
    torneo['squadre'].append({**init_squadra()})

while play():
    print(f"""Giornata {giornata}""")
    #Creo una lista con i soli nomi delle squadre con il ciclo for
    squadre_random = []
    squadre = torneo['squadre']
    squadre_length = len(squadre)

    for k in range(0,squadre_length):
        squadre_random.append(squadre[k]['nome'])

    new_partite = get_partite(squadre, partite_giocate)
    new_goals = [goal(random.randint(3, 6)) for i in range(0, squadre_length)]
    print(new_goals)
    #Aggiorno la lista vuota delle partite giocate
    partite_giornata = [get_partita_giocata(new_partite[i], new_partite[i + 1]) for i in range(0, int(len(new_partite) / 2))]
    partite_giocate.extend(partite_giornata)

    #Partite della giornata
    print('Partite della giornata: \n'+partite_giornata[0] )#+'\n'+partite_giornata[1])

    #Inizio della giornata da far scegliere all'utente
    play_match = input(f"""Simulare la giornata numero {giornata}? Digita S per Si, N per NO (S/N)""")
    match = play_match.lower() == 's'

    if not match:
        play(False)
    else:
        partite_end = [f"""{partite_giornata[i]} {new_goals[i]} - {new_goals[i+1]}""" for i in range(0, len(partite_giornata))]
        #Stampo i risultati delle partite
        print('Risultati della giornata: \n'+partite_end[0])#+'\n'+partite_end[1])

        #Assegno le partite giocare
        for squadra in squadre:
            squadra['partite'] = squadra['partite']+1
        
        #Condizioni per assegnare i punti, i gol e la differenza reti

        # DA METTERE APPOSTO 

        # for m in range(0,4):
        #     for n in range(0,4):
        #         if m == 0:
        #             o = 1
        #         elif m == 1:
        #             o = 0
        #         elif m == 2:
        #             o = 3
        #         else:
        #             o = 2

        #         if new_partite[m] == torneo['squadre'][n]['nome']:
                    
        #             #Assegno i gol alle squadre
        #             torneo['squadre'][n]['gol_fatti'] = torneo['squadre'][n]['gol_fatti'] + new_goals[m]
        #             torneo['squadre'][n]['gol_subiti'] = torneo['squadre'][n]['gol_subiti'] + new_goals[o]
                    
        #             #Assegno la differenza reti
        #             torneo['squadre'][n]['differenza_reti'] = torneo['squadre'][n]['gol_fatti'] - torneo['squadre'][n]['gol_subiti']
                    
        #             #Assegno i punti alle squadre
        #             if new_goals[m] > new_goals[o]:
        #                 torneo['squadre'][n]['punti'] = torneo['squadre'][n]['punti']+3

        #             elif new_goals[m] == new_goals[o]:
        #                 torneo['squadre'][n]['punti'] = torneo['squadre'][n]['punti']+1

        #             else:
        #                 pass


         ### FINE NUOVE CONDIZIONI PER I SORTEGGI



    prima_squadra = squadre[0]

    if prima_squadra['partite'] == squadre_length -1:
            print('Classifica finale')
    else:
            print(f"""Classifica dopo la giornata numero {giornata}""")

    squadre.sort(key=classifica, reverse=True)

    for squadra in squadre:
            nome_squadra = squadra['nome']
            punti_squadra = squadra['punti']
            partite_squadra = squadra['partite']
            fatti_squadra = squadra['gol_fatti']
            subiti_squadra = squadra['gol_subiti']
            diff_reti = squadra['differenza_reti']
            print(nome_squadra+' '+str(punti_squadra)+' punti in '+str(partite_squadra)+' partite con '+str(fatti_squadra)+' gol fatti e '+str(subiti_squadra)+' gol subiti e differenza reti di '+"%+d" % (diff_reti))
    
    #Aumento il numero della giornata
    giornata = giornata+1

    

    #Condizioni per la fine del torneo
    if prima_squadra['partite'] == squadre_length -1:

        #Verifico che non ci siano squadre a pari punti
        if prima_squadra['punti'] != squadre[1]['punti']:
            vincitore_singolo = True
            vincitore = prima_squadra['nome']
            punti_vincitore = prima_squadra['punti']  
        else:
            vincitore_singolo = False
            pari_merito = [prima_squadra['nome']]
            punti_vincitore = prima_squadra['punti']
            for z in range(1,squadre_length):
                if prima_squadra['punti'] == squadre[z]['punti']:
                    pari_merito.append(squadre[z]['nome'])

        pari_merito_length = len(pari_merito)
        #Se c'è solo un vincitore
        if vincitore_singolo:
            print(vincitore+' vince il torneo con '+str(punti_vincitore)+' punti')
        #Se ci sono più squadre allo stesso punteggio
        else:
            if pari_merito_length == 2:
                print('2 squadre hanno vinto il torneo:')
                print(pari_merito[0]+' e '+pari_merito[1]+' hanno vinto con '+str(punti_vincitore)+' punti')
                # per adesso, da rimuovere
                #Chiede se effettuare uno spareggio
                # spareggio = input('Due squadre sono prime a pari merito. Premi S per procedere con uno spareggio, N per terminare il torneo in parità (S/N)')
                # if spareggio.lower() == 'n':
                #     play(False)
                # else:
                #     print('La finale è tra '+pari_merito[0]+' e '+pari_merito[1])
                #     #Conferma di disputa della finale
                #     finale = input('Disputare la finale spareggio? Premi S per si, N per no (S/N)')
                #     if finale.lower() == 's':
                #         #Gol della finale
                #         finale_goals = [random.randint(0,4), random.randint(0,4)]
                #         while finale_goals[0] == finale_goals[1]:
                #             finale_goals = [random.randint(0,4), random.randint(0,4)]
                #         #Printa il risultato della finale
                #         print('La finale è terminata: '+pari_merito[0]+' - '+pari_merito[1]+' '+str(finale_goals[0])+' - '+str(finale_goals[1]))
                #         #Decreto il vincitore
                #         if finale_goals[0] > finale_goals[1]:
                #             print('Il vincitore del torneo è '+pari_merito[0]+' dopo aver battuto in finale '+pari_merito[1])
                #             play(False)
                #         else:
                #             print('Il vincitore del torneo è '+pari_merito[1]+' dopo aver battuto in finale '+pari_merito[0])
                #             play(False)
                
        
                    
                #     else:
                #         play(False)
            elif pari_merito_length < squadre_length:
                print(f"""{pari_merito_length} squadre hanno vinto il torneo:""")
                # print(pari_merito[0]+', '+pari_merito[1]+' e '+pari_merito[2]+' hanno vinto con '+str(punti_vincitore)+' punti')
            else:
                print('Tutte le squadre hanno lo stesso punteggio:')
                # print(pari_merito[0]+', '+pari_merito[1]+', '+pari_merito[2]+' e '+pari_merito[3]+' hanno vinto con '+str(punti_vincitore)+' punti')
            #Messaggio di fine indipendentemente dall'esito
                print('Fine del torneo')
                play(False)
                print(ty_message)
    else:
        #Proseguire o meno il torneo con la giornata successiva
        going_on = input(f"""Proseguire con la giornata numero {giornata}? Digita S per Si, N per NO (S/N)""")
        if going_on.lower() == 's':
            play(True)
        else:
            play(False)
            print('Il torneo è incompleto, ma '+ty_message.lower())
            match = False