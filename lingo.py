def las_pistas(secreta,intento)

pista=""
for i in range(5):
    if intento[i] == secreta[i]:
        pista = pista + "[" + intento[i] + "]"
    elif intento [i] in secreta:
        pista = pista + "(" + intento[i] + ")"
    else:
        pista = pista + intento[i]
return pista