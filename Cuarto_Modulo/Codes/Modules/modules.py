"""
* Un módulo es un archivo de python cuyos objetos, funciones, variables, etc. pueden ser accedidos desde otro archivo.
"""

import datetime as dt
from datetime import time
from datetime import *
import sys

print(dir(dt))

print("\n" , dt.date.__doc__)

print(dt.date.today())

print(dt.date(2032, 11, 12))

print(time(12, 26, 34, 5))
a = time(12, 26, 34, 5)
print(a.hour)

print("\n\n")

for file in sys.path:
    print(file)