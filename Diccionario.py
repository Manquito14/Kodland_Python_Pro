diccionario={
    "JUICIOSO":"persona responsable",
    "CHIMBA":"algo que las espectativas o algo bonito",
    "CRISPETAS":"también conocidas como , rosas, pochoclos, cabritas",
    "AGUACATE":"también conocido como palta"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

#print(diccionario.keys())
if word in diccionario.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(diccionario[word])
    
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esa palabra no se encuentra en el diccionario.")
