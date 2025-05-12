import sys
import os

# Agregar al path la carpeta 'modulo' que está un nivel arriba
modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulo'))
sys.path.append(modulo_path)

# Importar la función saludo desde el archivo modulo.py
from modulo import saludo

# Llamar a la función
saludo()
