# Inicializado no __init__.py da pasta functions
from functions import add

# apenas importação pelo caminho
from functions.sub_pkg.new_module import print_hello

print (add(5,5))
print_hello()