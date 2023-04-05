def estadisticas(muestra):
    n = len(muestra)
    media = sum(muestra) / n
    varianza = sum((x - media) ** 2 for x in muestra) / (n - 1)
    desviacion_tipica = varianza ** 0.5
    return {"media": media, "varianza": varianza, "desviacion_tipica": desviacion_tipica}

print(estadisticas([1,2,3,4,5]))