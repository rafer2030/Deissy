"""
    Muestra un reloj en tiempo real 
    y activa una alarma tras 5 segundos
"""

import time as t 

for x in range(5):
    print(t.strftime("%H:%M:%S"))
    t.sleep(1)

print("Alarma!")