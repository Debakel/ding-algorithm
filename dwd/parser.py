# coding=utf8

import csv
import os
import datetime

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

# Niederschlagsformen
KEIN_NIEDERSCHLAG = 0
NICHT_BEKANNT = 4
REGEN = 6
REGEN_VOR1979 = 1 # 1 vor 1979
SCHNEEREGEN = 8
SCHNEE = 7


class Messwert():
    stations_id = None
    date = None
    lufttemperatur = None
    rel_feuchte = None
    niederschlagsform = None
    stationshoehe = None

def read_csv(filename):
    DELIMETER = ';'
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=DELIMETER)
        row = reader.next()  # skip first row
        rows = []
        for row in reader:
            rows.append(row)
        return rows


def read_dataset(dirname=None, filename_metadaten=None, filename_tageswerte=None):
    # Read csv file
    if filename_metadaten is not None and filename_tageswerte is not None:
        metadaten = read_csv(filename_metadaten)
        tageswerte = read_csv(filename_tageswerte)
    elif dirname is not None:
        files = os.listdir(dirname)
        for file in files:
            if file[0] is '.':
                continue # skip lockfiles, cache, etc...
            if 'Stationsmetadaten' in file:
                metadaten = read_csv(os.path.join(dirname, file))
            elif 'Tageswerte' in file:
                tageswerte = read_csv(os.path.join(dirname, file))
    else:
        return []

    # Loop rows
    data_set = []
    for messung in tageswerte:
        try:
            m = Messwert()
            m.date = datetime.datetime.strptime(messung[MESS_DATUM], '%Y%m%d')
            m.stations_id = int(messung[STATIONS_ID])
            m.lufttemperatur = float(messung[LUFTTEMPERATUR])
            m.rel_feuchte = float(messung[REL_FEUCHTE]) / 100
            m.niederschlagsform = int(messung[NIEDERSCHLAGSFORM])
            if m.niederschlagsform is REGEN_VOR1979:
                m.niederschlagsform = REGEN

            # Metadateneintrag wählen (nach Datum)
            for i in range(1 ,metadaten.__len__()):
                row = metadaten[i]
                von = datetime.datetime.strptime(row[VON_DATUM], '%Y%m%d')
                try:
                    bis = datetime.datetime.strptime(row[BIS_DATUM], '%Y%m%d')
                except:
                    bis = bis = datetime.datetime.now()
                if von <= m.date <= bis:
                    break

            m.stationshoehe = int(metadaten[i][STATIONSHOEHE])

            data_set.append(m)
        except:
            pass

    return data_set

