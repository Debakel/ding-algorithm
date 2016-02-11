# coding=utf8

import csv
import os
# Spalten Metadaten
STATIONSHOEHE = 1
VON_DATUM = 4
BIS_DATUM = 5

# Spalten Tageswerte
STATIONS_ID = 0
MESS_DATUM = 1
LUFTTEMPERATUR = 3
REL_FEUCHTE = 7
NIEDERSCHLAGSFORM = 14

def read_csv(filename):
    DELIMETER = ';'
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=DELIMETER)
        row = reader.next()  # skip first row
        rows = []
        for row in reader:
            rows.append(row)
        return rows

def read_dataset(dirname, filename_metadaten=None, filename_tageswerte=None):
    # Metadaten in Stationsmetadaten_klima_stationen_00164_20140808_20160208.txt
    # Tageswerte in produkt_klima_Tageswerte_20140808_20160208_00164.txt
    if filename_metadaten is not None and filename_tageswerte is not None:
        metadaten = read_csv(filename_metadaten)
        tageswerte = read_csv(filename_tageswerte)
    else:
        files = os.listdir(dirname)
        for file in files:
            if file[0] is '.':
                continue # skip lockfiles, cache, etc...
            if 'Stationsmetadaten' in file:
                metadaten = read_csv(os.path.join(dirname, file))
            elif 'Tageswerte' in file:
                tageswerte = read_csv(os.path.join(dirname, file))

    data_set = []
    for messung in tageswerte:
        try:
            data_set.append({
                'STATIONS_ID': int(messung[STATIONS_ID]),
                'LUFTTEMPERATUR': float(messung[LUFTTEMPERATUR]),
                'MESS_DATUM': messung[MESS_DATUM],
                'REL_FEUCHTE': float(messung[REL_FEUCHTE]) / 100,
                'NIEDERSCHLAGSFORM': int(messung[NIEDERSCHLAGSFORM]),
                'STATIONS_HOEHE': int(metadaten[2][STATIONSHOEHE])
            })
        except:
            break

    return data_set
