import itertools as it

a = raw_input("Digite o nome do arquivo\n")
#input()

arq = open( a ,"r+")

saida = open("saida.csv", "w")


con = []

for line in arq.readlines():
	con.append(line.replace("\n",""))

table = list(it.product(["V","F"], repeat = len(con) ) )

i = 1
maxC = len(max(con))
#print " "*3,
saida.write(" "*8 + " ,")

tam = len(str(2**len(con)))


for c in con:
	print str.center(c, maxC+4),
	saida.write(str.center(c, maxC+4) + " ," )
	#saida.write(c+",")

saida.write( str.center("Acoes, acao1, ...", maxC+4) )
#saida.write("Acoes, acao1,")

print ""
saida.write("\n")
for line in table:
	print str.ljust("R"+str(i), tam+1),
	##saida.write(str.ljust("R"+str(i) +",", tam+1))

	saida.write( "R" + str(i) + "," )
	for attr in line:
		print str.center(attr, maxC+4),
		##saida.write( str.center(attr + ",", maxC+4))
		saida.write( str(attr) + "," )
		#saida.write(attr+",")
	print ""
	saida.write("\n")
	i += 1


arq.close()
saida.close()
