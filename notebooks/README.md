Qui abbiamo le infotmazioni utilizzate per l'esplorazione dei dati, l'analisi e la segmentazione dei clienti.

Fase 1 - Generazione del DataSet iniziale

OBIETTIVO - Creare un dataset composto da 50 clienti per simulare le attivita degli utenti della piattaforma.
Non contiene dati reali, ed è generato tramite Payton. 

Struttura: sono state definite le seguenti variabili
- ID, Zona, Categoria preferita, Data di iscrizione, Numero di prenotazioni, totale speso, Giorni dall'ultima prenotazione.

Per la generazione dei dati sono state utilizzate le librerie: Pandas, NumPy, Random e Datetime

Ho impostato un random seed pari a 2026 per garantire la riproducibilità dei risultati. 

Nella prima versione ho generato i valori casualmente senza assegnare prima i parametri per generare i profili. 

Risultato: questa generazione ha prodotto il dataset di 500 clienti, con le 7 variabili di cui sopra, trasformato in csv.

Analisi: ci sono delle piccole incoerenze dovute alla generazione randomica, possibili clienti iscritti da poco con un numero elevato di prenotazioni, importi non coerenti con il numero di prestazioni, e anche prenotazioni antecedenti alla data di iscrizione. 

Aggiornare e modificare: prima di tutto vado a fare un'analisi più approfondita sul dataset iniziale, e l'dea è quella di introdurre alcuni vincoli e relazioni logiche tra variabili, mantenedo comunque la generazione casuale.


