# coding=utf8

import math

# Niederschlagsformen
KEIN_N = 0
NICHT_BEKANNT = 4
REGEN = 6 # 1 vor 1979
SCHNEEREGEN = 8
SCHNEE = 7

def ding(z, Td, RH):
    # Sättigungsdampfdruck [kPa]
    saettigungsdampfdruck = 0.611 * math.exp(17.3 * Td / (Td + 237.3)) # Magnus Formel

    # Steigung der e* - T Beziehung [kPa/°C]
    steigung_e_t = (2508.3 / (Td + 237.3)**2) * math.exp(17.3*Td / (Td + 237.3))

    # Luftdruck [kPa]
    luftdruck = 101.3 * math.exp(-0.00013 * z)

    # Feuchttemperatur [°C] (Tf)
    Tf = Td - ((saettigungsdampfdruck * (1 - RH)) / (steigung_e_t + 0.000643 * luftdruck))

    # T[0] berechnen
    T_null = -5.87 - 1.042*(10**-4)*z + 8.85*(10**-8)*z**2 + 16.06*RH - 9.614*(RH**2)

    # Schwellenwerte berechnen (Schnee/Schneeregen T_min/T_max)
    if RH > 0.78:
        T_min = T_null + 11.756 - 23.1*RH + 10.289*(RH**2)
        T_max = 2*T_null - T_min
    else:
        T_min = T_null
        T_max = T_null

    # Niederschlagsform bestimmen
    if Tf <= T_min:
        Nf = SCHNEE
    elif T_min < Tf < T_max:
        Nf = SCHNEEREGEN
    elif T_max <= Tf:
        Nf = REGEN
    else:
        Nf = KEIN_N

    return Nf