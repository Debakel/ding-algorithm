# coding=utf8

import csv
import os
import argparse
import sys

from ding_algorithm import ding
from dwd import parser


def export(data_set, filename):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(('Stations ID', 'Datum','Lufttemperatur', 'Relative Feuchte', 'Stationshöhe', 'Niederschlagsform (gemessen)', 'Niederschlagsform (berechnet)'))
        for messwert in data_set:
            writer.writerow((messwert.stations_id, str(messwert.date), messwert.lufttemperatur, messwert.rel_feuchte,
                            messwert.stationshoehe, messwert.niederschlagsform, messwert.niederschlagsform_berechnet))

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("dataset", type=str, help="DWD Datensatz")
    argparser.add_argument("metadata", type=str, help="Stationsmetadaten")
    argparser.add_argument("-o", "--outfile", help="Writes result to file")

    args = argparser.parse_args()

    dataset = parser.read_dataset(filename_tageswerte=args.dataset, filename_metadaten=args.metadata)

    for messung in dataset:
        Nf = ding.ding(messung.stationshoehe, messung.lufttemperatur, messung.rel_feuchte)
        messung.niederschlagsform_berechnet = Nf
    if args.outfile:
        export(dataset, args.outfile)
