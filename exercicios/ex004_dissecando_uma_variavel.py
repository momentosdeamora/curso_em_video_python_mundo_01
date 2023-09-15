algo = input("Digite algo: ")
print("O tipo primitivo deste valor é {0}".format(type(algo)))
print("Só tem espaços? {0}".format(algo.isspace()))
print("É um número? {0}".format(algo.isnumeric()))
print("É alfabético? {0}".format(algo.isalpha()))
print("É alfanumérico? {0}".format(algo.isalnum()))
print("Está em maiúscula? {0}".format(algo.isupper()))
print("Está em minúscula? {0}".format(algo.islower()))
print("Está capitalizada? {0}".format(algo.istitle()))

#Capitalizada é a primeira letra ser maiúscula e as demais minúsculas
