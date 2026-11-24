# Importazione delle librerie necessarie, pandas per organizzare i dati in tabelle, Numpy per generare valori numerici, datetime per lacorare
# con le date e calcolare intervalli di tempo.
# random permette di generare valori casuali, come ad esempio per assegnare categorie o caratteristiche di un cliente.

import panda as pd 
import numpy as numpy

from datetime import datetime, timedelta
import random

# IMPOSTAZIONI GENERALI DEL DATASET

# Numero totale dei clienti da generare

numero_clienti = 500

# Impostiamo un seed casuale per ottenere sempre gli stessi risultati
# ogni volta che usaimo il programma. 

random.seed(2026)
np.random.seed(2026)

#data di riferimento per silulare l'attività dei clienti e calcolare i giorni dall'ultima prenotazione.
data_riferimento = datetime(2026,11,24)

# Definizioni delle aree geografiche

zone_geografiche = ["Nord", "Centro", "Sud e Isole"]

#Definizione Categorie di servizi offerti sulla piattaforma

categorie_servizio = ["Hair Styling", "Hair Coloring", "Nail Care", "Skincare", "Beauty Treatments"]
