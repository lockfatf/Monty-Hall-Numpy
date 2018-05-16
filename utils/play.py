
import numpy as np
import utils.strat as st

def play_game(strategie, nbtours):

    # Génération des portes 
    portes = np.array([[0, 1, 2]]*nbtours)

    # Random pour les bonnes portes
    bonne_porte = np.random.randint(0, 3, nbtours)
    bonne_porte = np.vstack(bonne_porte)
    
    # Random pour les premiers choix
    premier_choix = np.random.randint(0, 3, nbtours)
    premier_choix = np.vstack(premier_choix)

    #On enlève les premiers choix des portes restantes
    portes = portes[portes != premier_choix]
    portes = np.reshape(portes, (nbtours, 2))
    
    #On stocke les parties gagnantes au premier choix
    bon_premier_choix = (premier_choix == bonne_porte)
    
    
    # Le deuxieme choix depend de la strategie
    #Changement deuxième choix en fonction de la stratégie
    if strategie == st.Strategie.CHANGER:
        deuxieme_choix = portes[:,0]
        deuxieme_choix = np.vstack(deuxieme_choix)
        
        #On stocke les parties gagnantes aux deuxièmes choix
        bon_deuxieme_choix = (deuxieme_choix == bonne_porte)
        
        #On retourne le tableau des parties (True = gagné, False = Perdu)
        return (bon_premier_choix | bon_deuxieme_choix)
    
    elif strategie == st.Strategie.GARDER:
        
        #Si la stratégie est de garder, on peut donc dire que les resultats du premier choix sont définitifs
        return(bon_premier_choix)
    else:
        raise ValueError("Stratégie non reconnue!")
        
   