import json

fd = open("lectura archivo/lista.json","w")

lst =[{"nombre":"juan","edad":25},
    {"nombre":"paola","edad":28},
    {"nombre":"mateo","edad":18},
    {"nombre":"jesus","edad":19},
    {"nombre":"sebastian","edad":21}]

json.dump(lst, fd)

fd.close()