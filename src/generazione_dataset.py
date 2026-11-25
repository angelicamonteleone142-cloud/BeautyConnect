# Importazione delle librerie necessarie, pandas per organizzare i dati in tabelle, Numpy per generare valori numerici, datetime per lacorare
# con le date e calcolare intervalli di tempo.
# random permette di generare valori casuali, come ad esempio per assegnare categorie o caratteristiche di un cliente.

import pandas as pd 
import numpy as np

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
# In questa prima fa i dati vengono generati in maniera del tutto causuale, senza assegnare ai clienti dei profili prestabiliti.
# senza assegnare ai clienti nessun profilo
# l'obiettivo è generare un dataset di partenza da utilizzare per generare i target
# i valori vengono generati inizialmente in modo indipendete, ma questo tipo di implementazione permette di evidenziare ed osservare
#delle anomalie, e incoerenze nel risultato.
# in seguito verranno introdotti dei criteri senza però definire anticipatamente i segmenti dei clienti. 

for numero in range(1, numero_clienti + 1):

# Creazione dell'id cliente

                identificativo = f"C{numero:04d}"

# Seleziono casualmente l'area geografica

                zona = random.choice(zone_geografiche)

# seleziono casualmente la categoria di servizio

                categoria = random.choice(categorie_servizio)

                giorni_dal_inizio = random.randint(0, 365 * 3)

                data_iscrizione = data_riferimento - timedelta(days=giorni_dal_inizio)

                numero_prenotazioni = random.randint(1,22)
                totale_speso = round(random.uniform(10,1800), 2)
                giorni_ultima_prenotazione = random.randint(0, 365 * 3)

# popolo la lista dei clienti con le informazioni

                clienti.append({
    "ID_cliente": identificativo,
    "Zona": zona,
    "Categoria_preferita": categoria,
    "Data_Iscrizione": data_iscrizione.strftime("%Y-%m-%d"),
    "Numero_Prenotazioni": numero_prenotazioni,
    "Totale_Speso": totale_speso,
    "Giorni_Ultima_Prenotazione": giorni_ultima_prenotazione
})

# Con l'utilizzo di Pandas creiamo una tabella dalla lista

dataset = pd.DataFrame(clienti)

print("Dimensioni del dataset", dataset.shape)
# visualizziamo le prime righe della tabella

print(dataset.head())

print("\nDimensioni del dataset:", dataset.shape)
print("\nInformazioni sul dataset")
print(dataset.info())
print("\nStatistiche descrittive:")
print(dataset.describe())

dataset.to_csv("data/dataset_clienti_iniziale.csv", index=False, encoding = "utf-8-sig")

print("\n Dataset salvato")