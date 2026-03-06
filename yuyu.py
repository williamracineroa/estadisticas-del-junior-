

print("-------ESTADISTICAS DEL YUYU---------")
partidos_jugados = int (input("Ingrese el número de partidos jugados: ")) 
gf= 0
gc= 0
puntos = 0
pg=0
pe=0
pp=0
for i in range (partidos_jugados):
    i == 0
    print("Partido", i+1)
    goles_favor = int (input("Ingrese el número de goles a favor en el partido: "))
    goles_contra = int (input("Ingrese el número de goles en contra en el partido: "))
    if goles_favor < goles_contra:
        pp += 1
        print("PERDIO.")
    elif goles_favor > goles_contra:
        puntos += 3
        pg += 1
        print("GANO.")
    else:
        puntos += 1
        pe += 1
        print("EMPATE.")
    gf += goles_favor
    gc += goles_contra




print("-----ESTADISTICAS -----")


print("Puntos:", puntos)
print("PJ:", partidos_jugados)
print("PG:",pg)
print("PE:",pe)
print("PP:",pp)
print("GF:",gf)
print("GC:",gc)
print("DG:",gf - gc)

