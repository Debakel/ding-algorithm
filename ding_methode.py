# z Stationshöhe [m]
# Td Tagesmitteltemperatur [°C]
# RH relative Luftfeuchte [Dezimalbruch]

# Tf Feuchttemperatur [°C]

import math

def Tf(Td):
    pass

def saettigungsdampfdruck(Td):
    return 0.611 * math.exp((17.3 * Td / (Td + 237,3))) # Magnus Formel

def steigung(Td):
    return (2508.3 / (Td + 237.3)**2) * math.exp(17.3*Td / (Td + 237.3))

def luftdruck(z):
    return 101.3 * math.exp(-0.00013 * z)

T_
