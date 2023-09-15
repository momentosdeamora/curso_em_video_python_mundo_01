medida = float(input("Uma distância em metros: "))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print("A medida de {0} em metros corresponde a: \n {1} km \n {2} hm \n {3} dam \n {4} dm \n {5} cm \n {6} mm".format(medida, km, hm, dam, dm, cm, mm))
