# coding=utf8

import csv

from ding_algorithm import ding
from dwd import parser
# Daten
dirname = '/home/m/Dropbox/Studium/06_WS1516/04_Geodatenverarbeitung mit Python/Hausaufgabe/data/tageswerte_KL_00164_akt/'
filename_tageswerte = dirname + 'produkt_klima_Tageswerte_20140808_20160208_00164.txt'
filename_metadaten = dirname + 'Stationsmetadaten_klima_stationen_00164_20140808_20160208.txt'

dataset = parser.read_dataset(filename_metadaten, filename_tageswerte)

row = 0
for messung in dataset:
    row += 1

    Td = messung['LUFTTEMPERATUR']    # Mittlere Tagestemperatur [°C] (Td)
    datum = messung['MESS_DATUM']     # YYYYMMDD
    RH = messung['REL_FEUCHTE']       # Relative Luftfeuchte [%] (RH)
    z = messung['STATIONS_HOEHE']      # Stationshöhe [m]

    Nf = ding.ding(z, Td, RH)
    Nf_DWD = messung['NIEDERSCHLAGSFORM']

    print str(row) + ' ' + str(Nf) + ' (Nf) ' + str(Nf_DWD) + ' (Nf DWD) ' + str((Nf == Nf_DWD))