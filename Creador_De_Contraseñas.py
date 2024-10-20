import random

caracteres =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

contra = int(input("Introduce la longitud que deseas que tenga la contraseña:"))

newcontra = ""

for i in range(contra):
    a = random.choice(caracteres)
    newcontra = (newcontra+a)

print(f"Esta es tu contraseña: {newcontra}")
