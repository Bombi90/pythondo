#Prima Bozza Torneo a 4 squadre
import random


def torneo():
    
    print('Benvenuti nella simulazione di un torneo a 4 squadre')
    
    #Definiamo i nomi delle squadre facendoli scegliere all'utente
    team1 = [input('Inserisci il nome della prima squadra '),0,0]

    def squadra1(nome, punti, partite):
        
        squadra1(team1[0], team1[1], team1[2])
    
    team2 = [input('Inserisci il nome della seconda squadra '),0,0]

    def squadra2(nome, punti, partite):
        
        squadra2(team2[0], team2[1], team2[2])
    
    team3 = [input('Inserisci il nome della terza squadra '),0,0]

    def squadra3(nome, punti, partite):
        
        squadra3(team3[0], team3[1], team3[2])
    
    team4 = [input('Inserisci il nome della quarta squadra '),0,0]

    def squadra4(nome, punti, partite):
        
        squadra4(team4[0], team4[1], team4[2])
    
    print('Le squadre che hai scelto si chiamano '+ team1[0]+', '+team2[0]+', '+team3[0]+', '+team4[0])
    
    #Inizio della simulazione se l'utente
    play_game = input('Iniziare la simulazione? Digita S per si, N per No (S/N)')
    if play_game.lower() == 's':
        game_on = True
    else:        
        game_on = False
        print('Grazie per aver giocato con noi')
        
    #Inizio del torneo    
    if game_on:
        #Giornata 1
        print('Giornata 1 | Partita 1')
        print(team1[0]+ ' vs '+ team2[0])
        play_match = input('Simulare '+team1[0]+' vs '+team2[0]+ ' ? Digita S per Si, N per NO (S/N)')
        if play_match.lower() == 's':
            match = True
        else:
            match = False
            
        if match:
            
            ris1 = random.randint(0,4)
            ris2 = random.randint(0,4)
            print(team1[0]+ ' '+ str(ris1)+ ' - '+team2[0]+ ' '+str(ris2))
            
            if ris1 > ris2:
                team1[1] = team1[1]+3
                
            elif ris1 == ris2:
                team1[1] = team1[1]+1
                team2[1] = team2[1]+1
                
            else:
                team2[1] = team2[1]+3
            
        print('Giornata 1 | Partita 2')
        print(team3[0]+ ' vs '+ team4[0])
        play_match = input('Simulare '+team3[0]+' vs '+team4[0]+ ' ? Digita S per Si, N per NO (S/N)')
        if play_match.lower() == 's':
            match = True
        else:
            match = False
            
        if match:
            
            ris3 = random.randint(0,4)
            ris4 = random.randint(0,4)
            print(team3[0]+ ' '+ str(ris3)+ ' - '+team4[0]+ ' '+str(ris4))
            
            if ris3 > ris4:
                team3[1] = team3[1]+3
                
            elif ris3 == ris4:
                team3[1] = team3[1]+1
                team4[1] = team4[1]+1
                
            else:
                team4[1] = team4[1]+3
            
            #aggiungo le partite giocate ai team
            team1[2] = team2[2] = team3[2] = team4[2] = team1[2]+1
            #prova di classifica ordinata | classifica = [team1[1], team2[1], team3[1], team4[1]]
            #prova di classifica ordinata | classifica.sort(reverse = True)
            #Classifica dopo la prima giornata
            
            print('Classifica: \n'+team1[0]+' '+str(team1[1])+' punti \n'+team2[0]+' '+str(team2[1])+' punti \n'
            +team3[0]+' '+str(team3[1])+' punti \n'+team4[0]+' '+str(team4[1])+' punti ')
            
            #Giornata 2
            
            print('Giornata 2 | Partita 1')
            print(team1[0]+ ' vs '+ team3[0])
            play_match = input('Simulare '+team1[0]+' vs '+team3[0]+ ' ? Digita S per Si, N per NO (S/N)')
            if play_match.lower() == 's':
                match = True
            else:
                match = False
            
            if match:
            
                ris1 = random.randint(0,4)
                ris2 = random.randint(0,4)
                print(team1[0]+ ' '+ str(ris1)+ ' - '+team3[0]+ ' '+str(ris2))
            
                if ris1 > ris2:
                    team1[1] = team1[1]+3
                
                elif ris1 == ris2:
                    team1[1] = team1[1]+1
                    team3[1] = team3[1]+1
                
                else:
                    team3[1] = team3[1]+3
            
            print('Giornata 2 | Partita 2')
            print(team2[0]+ ' vs '+ team4[0])
            play_match = input('Simulare '+team2[0]+' vs '+team4[0]+ ' ? Digita S per Si, N per NO (S/N)')
            if play_match.lower() == 's':
                match = True
            else:
                match = False
            
            if match:
            
                ris3 = random.randint(0,4)
                ris4 = random.randint(0,4)
                print(team2[0]+ ' '+ str(ris3)+ ' - '+team4[0]+ ' '+str(ris4))
            
                if ris3 > ris4:
                    team2[1] = team2[1]+3
                
                elif ris3 == ris4:
                    team2[1] = team2[1]+1
                    team4[1] = team4[1]+1
                
                else:
                    team4[1] = team4[1]+3
            
                #aggiungo le partite giocate ai team
                team1[2] = team2[2] = team3[2] = team4[2] = team1[2]+1
                #Classifica dopo la seconda giornata
            
                print('Classifica: \n'+team1[0]+' '+str(team1[1])+' punti \n'+team2[0]+' '+str(team2[1])+' punti \n'
                +team3[0]+' '+str(team3[1])+' punti \n'+team4[0]+' '+str(team4[1])+' punti ')
                
                
                
                #Giornata 3
            
                print('Giornata 3 | Partita 1')
                print(team1[0]+ ' vs '+ team4[0])
                play_match = input('Simulare '+team1[0]+' vs '+team4[0]+ ' ? Digita S per Si, N per NO (S/N)')
                if play_match.lower() == 's':
                    match = True
                else:
                    match = False

                if match:

                    ris1 = random.randint(0,4)
                    ris2 = random.randint(0,4)
                    print(team1[0]+ ' '+ str(ris1)+ ' - '+team4[0]+ ' '+str(ris2))

                    if ris1 > ris2:
                        team1[1] = team1[1]+3

                    elif ris1 == ris2:
                        team1[1] = team1[1]+1
                        team4[1] = team4[1]+1

                    else:
                        team4[1] = team4[1]+3

                print('Giornata 3 | Partita 2')
                print(team2[0]+ ' vs '+ team3[0])
                play_match = input('Simulare '+team2[0]+' vs '+team3[0]+ ' ? Digita S per Si, N per NO (S/N)')
                if play_match.lower() == 's':
                    match = True
                else:
                    match = False

                if match:

                    ris3 = random.randint(0,4)
                    ris4 = random.randint(0,4)
                    print(team2[0]+ ' '+ str(ris3)+ ' - '+team3[0]+ ' '+str(ris4))

                    if ris3 > ris4:
                        team2[1] = team2[1]+3

                    elif ris3 == ris4:
                        team2[1] = team2[1]+1
                        team3[1] = team3[1]+1

                    else:
                        team3[1] = team3[1]+3

                    #aggiungo le partite giocate ai team
                    team1[2] = team2[2] = team3[2] = team4[2] = team1[2]+1
                    #Classifica finale dopo la terza giornata

                    print('Classifica finale: \n'+team1[0]+' '+str(team1[1])+' punti in '+str(team1[2])+' partite \n'+
                    team2[0]+' '+str(team2[1])+' punti in '+str(team2[2])+' partite \n'+
                    team3[0]+' '+str(team3[1])+' punti in '+str(team3[2])+' partite \n'+
                    team4[0]+' '+str(team4[1])+' punti in '+str(team4[2])+' partite \n')
                    
                    print('Grazie per aver giocato')
                    
                    #IMPLEMENTAZIONI DA FARE:
                        #FONDAMENTALE: Classifica ordinata per punti
                        #NON FONDAMENTALE MA MOLTO UTILE: sorteggio random degli incroci senza ovviamente doppie partite
                        #FACILI DA AGGIUNGERE IN SEGUITO: Gol fatti/subiti e differenza reti
                        #DA AMPLIARE EVENTUALMENTE N. DELLE SQUADRE E/O POSSIBILITA' DI FAR SCEGLIERE ALL'UTENTE IL NUMERO
                    
        