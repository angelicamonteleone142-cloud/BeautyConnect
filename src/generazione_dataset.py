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

# GENERAZIONE DEI DATI DEL CLIENTE

# creazione di una lista vuota che conterrà le informazioni dei clienti

clienti = []

for numero in range(1, numero_clienti + 1):

# Creazione dell'id cliente

identificativo = f"C{numero:04d}"

# Seleziono casualmente l'area geografica

zona = random.choice(zone_geografiche)

# seleziono casualmente la categoria di servizio

categoria = random.choice(categorie_servizio)

# popolo la lista dei clienti con le informazioni

clienti.append({
    "ID_cliente": identificativo,
    "Zona": zona,
    "Categoria_preferita": categoria
})

# Con l'utilizzo di Pandas creiamo una tabella dalla lista

dataset = pd.DataFrame(clienti)

# visualizziamo le prime righe della tabella

print(dataset.head())
