n1concatenar = input("Digite um valor: ")
n2concatenar = input("Digite outro valor: ")
sconcatenar = n1concatenar + n2concatenar
print(type(n1concatenar))
print("A soma vale", sconcatenar)

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
print(type(n1))
# print("A soma vale", s)
print("A soma entre {} e {} vale {}".format(n1, n2, s))

n = input ("Digite um valor: ")
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.isupper())
