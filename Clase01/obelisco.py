grosor_billete = 0.11 * 0.001
altura_obelisco = 67.5
num_billetes = 1
dia = 1

while num_billetes * grosor_billete <= altura_obelisco:
	print(dia, num_billetes, num_billetes * grosor_billete)
	dia = dia + 1
	num_billetes = num_billetes * 2
	
print('cantidad de dias', dia)
print('cantidad de billetes', num_billetes)
print('altura final', num_billetes * grosor_billete)

