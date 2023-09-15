nome = input("Qual é seu nome? ")
print("Prazer em te conhecer {:>20}!".format(nome)) #Justificado à direita
print("Prazer em te conhecer {:<20}!".format(nome)) #Justificado à esquerda
print("Prazer em te conhecer {:^20}!".format(nome)) #Centralizado
print("Prazer em te conhecer {:=^20}!".format(nome)) #Centralizado com o simbolo "=" em volta

n1 = int(input("Escreva um valor: "))
n2 = int(input("Escreva outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#print("A soma vale {}".format(n1+n2))
print("A soma é {}, \n o produto é {} e \n a divisão é {:.3f}".format(s,m,d), end=" ")
print("Divisão inteira {} e potência {}".format(di,e))