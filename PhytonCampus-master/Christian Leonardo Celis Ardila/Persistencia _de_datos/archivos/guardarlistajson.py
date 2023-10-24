#metodos de json :  open, close, dump, load

import json

fd = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/lista.json","w")

lst = [{"nombre":"Paola","edad":27},{"nombre":"carlos","edad":25},{"nombre":"juan","edad":15},{"nombre":"mateo","edad":22},{"nombre":"Patricia","edad":24}]

json.dump(lst,fd)

fd.close()