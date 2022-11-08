# Arnold Avalos Torres
# No. Control: 18420428


def postal():
    archivo = open("CPdescarga.txt","r")
    cadena = archivo.read()
    lista = cadena.split("\n")
    archivo.close()
    cp = set()
    for pos in lista[2:]:
        pos1 = pos.split("|")
        tup = (pos1[0], pos1[1],  pos1[13])
        cp.add(tup)
    return cp


def municipio(mun):
    pos = postal()
    munici = []

    for i in pos:
        if mun == i[]:
            dicnum = {}
            dicnum["Codigo Postal"] = i[0]
            dicnum["Asentamiento"] = i[1]
            dicnum["Zona"] = i[13]
            munici.append(dicnum)
    return munici

print(municipio("Jiquilpan"))




