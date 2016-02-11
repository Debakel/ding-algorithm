# coding=utf8

import csv

from ding_algorithm import ding
from dwd import parser
from os import listdir
import os
# Daten
dirname = '/home/m/Dropbox/Studium/06_WS1516/04_Geodatenverarbeitung mit Python/Hausaufgabe/data/'
dataset = []

for root, dirs, files in os.walk(dirname):
    for name in dirs:
        dataset.extend(parser.read_dataset(os.path.join(root, name)))


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