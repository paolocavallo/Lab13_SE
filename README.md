# Lab 13 - Simulazione d'Esame (gene_small)

---
> **❗ ATTENZIONE:** 
>  Ricordare di effettuare il **fork** del repository principale, quindi clonare su PyCharm il **repository personale** 
> (https://github.com/my-github-username/Lab13_SE) e non quello principale.
> 
> In caso di dubbi consultare la guida caricata nel lab02: 
> https://github.com/Programmazione-Avanzata-2025-26/Lab02/blob/main/Guida.pdf

---
**DURATA DELLA PROVA**: 2 h

---

Si consideri il database `genes_small.sql`, estratto da un database del genoma umano originariamente creato per una 
challenge internazionale di biological data mining. I geni codificano le proteine che si localizzano in diverse parti 
della cellula e interagiscono fra di loro per eseguire le funzioni vitali della cellula stessa. Il database contiene le
seguenti tabelle:
- `classificazione`: contiene le informazioni sulla localizzazione dei geni (e delle rispettive proteine):
  - **id_gene**
  - localizzazione
- `interazione`: contiene le informazioni sul tipo e intensità del rapporto di interazione:
  - **id_gene1**
  - **id_gene2**
  - tipo
  - correlazione
- `gene`: contiene le informazioni sui geni e sulla funzione da loro espressa:
  - **id**
  - **funzione**
  - essenziale
  - cromosoma

![relazione_db.png](img/relazione_db.png)

Si intende costruire un’applicazione FLET che permetta di svolgere le seguenti funzioni: 

## PUNTO 1
1. All’avvio del programma, si crei un grafo semplice, pesato e orientato i cui vertici siano tutti i cromosomi 
(tabella gene, colonna `cromosoma`, considerando solo i valori diversi da 0). 
2. Un arco collega due cromosomi diversi solo se i due cromosomi contengono due geni (uno per cromosoma) che compaiono 
(nello stesso ordine) nella tabella `interazione`. Si noti che, per ciascun cromosoma, possono esistere più geni, e 
ciascuno di essi potrebbe essere presente più volte (associato a funzioni, colonna `funzione`, diverse). 
3. Il peso di ciascun arco dovrà essere calcolato come la somma algebrica della correlazione (tabella `interazione`, 
colonna `correlazione`), facendo attenzione a contare ogni coppia di geni una sola volta. Nell’esempio seguente, il peso 
dell’arco tra il cromosoma 3 ed il cromosoma 4 sarà pari a 0.917953134. 

    | Cromosoma1 | Cromosoma2 | Gene1   | Gene2   | Correlazione |                |
    |------------|------------|---------|---------|--------------|----------------|
    | 3          | 4          | G234167 | G234317 | 0.307833642  | OK             |
    | 3          | 4          | G237463 | G238857 | 0.610119492  | OK             |
    | 3          | 4          | G237463 | G238857 | 0.610119492  | DUPLICATO      |
    | 4          | 3          | G238035 | G238033 | 0.703242256  | ORDINE DIVERSO |

4. Si visualizzi, nella GUI, il numero di vertici ed archi del grafo, ed i valori minimo e massimo dei pesi degli archi.
5. Permettere all’utente di inserire un valore soglia (S), verificando che tale valore sia compreso nell’intervallo 
[3,7]. 
6. Alla pressione del bottone “Conta Archi” stampare il numero di archi il cui peso è <S, ed il numero di archi il cui 
peso è >S.

Esempio interfaccia grafica: 
![layout.png](img/layout.png)

## PUNTO 2
1. A partire dal grafo calcolato al punto precedente, alla pressione del tasto “Ricerca Cammino”, si avvii una 
procedura di ricerca ricorsiva per determinare il cammino di vertici (cromosomi) del grafo che massimizza il costo 
complessivo, calcolato come somma dei costi associati agli archi (o ai vertici) che sia composto esclusivamente da 
archi di peso >S. Il costo del cammino sarà valutata dalla somma dei pesi degli archi incontrati.
2. Si visualizzi nella GUI la sequenza di cromosomi dal peso massimo così ottenuto.

Nella realizzazione del codice, si lavori a partire dalle classi e dal database contenuti nel progetto di base. 
È ovviamente permesso aggiungere o modificare classi e metodi. 

Tutti i possibili errori di immissione, validazione dati, accesso al database, ed algoritmici devono essere gestiti, 
non sono ammesse eccezioni generate dal programma.

-----

#### ESEMPIO DI RISULTATI PER CONTROLLARE LA PROPRIA SOLUZIONE: 
![result.png](img/result.png)

-----
## Materiale Fornito
Il repository del Lab13_SE è organizzato con la struttura ad albero mostrata di seguito e contiene tutto il necessario 
per svolgere l'esame:

```code
Lab13_SE/
├── database/
│   ├── __init__.py
|   ├── connector.cnf 
|   ├── DB_connect.py 
│   └── dao.py (DA MODIFICARE) 
│
├── model/ (AGGIUNGERE ULTERIORI CLASSI SE NECESSARIE) 
│   ├── __init__.py
│   └── model.py (DA MODIFICARE) 
│
├── UI/
│   ├── __init__.py
│   ├── alert.py
│   ├── controller.py (DA MODIFICARE)
│   └── view.py
│
├── genes_small.sql (DA IMPORTARE)
└── main.py (DA ESEGUIRE)
 ```
