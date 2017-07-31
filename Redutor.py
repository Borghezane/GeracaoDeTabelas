# -*- coding: utf-8 -*-

import os

def cls():
    #os.system('cls' if os.name=='nt' else 'clear')
    pass

def findIAction(vec):
	for i in range(len(vec)):
		if( vec[i] == "Acoes" ):
			return i


def imprimeTab(con, vec):
	#print str(con).replace("[","").replace("]","").replace("'","")
	#saida.write( str(con).replace("[","").replace("]","").replace("'","") + "\n" )
	for x in vec:
		
		for value in x[0]:
			#print value,
			print str.center( str(value) ,2),
		print " | ",
		for value in x[1]:
			#print value,
			print str.center( str(value) ,2),
		print ""

		#print str(x[0]).replace("[","").replace("]","").replace("'","").replace(","," ") + " ",
		#saida.write( str(x[0]).replace("[","").replace("]","").replace("'","") + "," + "," )
		#print str(x[1]).replace("[","").replace("]","").replace("'", "")
		#saida.write( str(x[1]).replace("[","").replace("]","").replace("'","")  + "\n" )

def findOneDiff(l1, l2, con, vec):
	indice = None
	diff = 0
	t1 = len( l1[1] )

	#print(l1)
	#print(l2)


	for i in range(t1):
		if( (l1[1])[i]  != (l2[1])[i] ):
			return None
	t2 = len( l1[0] )

	for i in range(1,t2):
		if( (l1[0])[i]  != (l2[0])[i]  ):
			if(diff == 1):
				return None
			diff = 1
			indice = i
	cls()
	imprimeTab(con, vec)
	print "\n\n"
	print "Essas regras serao fundidas\n"
	print str(l1[0]).replace("[","").replace("]","").replace("'","").replace(",","   ") + "  | " ,
	print str(l1[1]).replace("[","").replace("]","").replace("'","").replace(",","   ") 
	print str(l2[0]).replace("[","").replace("]","").replace("'","").replace(",","   ") + "  | " ,
	print str(l2[1]).replace("[","").replace("]","").replace("'","").replace(",","   ") + "\n\n"



	raw_input()
	

	(l1[0])[indice] = "NI"

	return l1

print u"Ações inseridas?"
if( raw_input("sim/nao\n") == "nao"):
	print u"\nExecute novamente após inserir as ações no arquivo 'saida.csv'"
	exit()


arq   = open("saida.csv"        , "r+" )
saida = open("saidaReduzida.csv", "w"  )



f = True

iAct = None

vec = []

con = None

for line in arq.readlines():
	if( f ):
		con = line.split(",")
		con[-1] = con[-1][0:-1]
		
		#
		#print con
		#raw_input("aaaaaaaaaaaaaaaaaa")
		#
		
		iAct = findIAction( con )
		f = False
	else:
		aux = line.split(",")
		aux[-1] = (aux[-1])[0:-1]
		
		#
		#print((aux[0:iAct]," ||  ",aux[iAct:]))
		#raw_input()
		#
		
		vec.append( (aux[0:iAct], aux[iAct+1:]) )

tam = len(vec)
j = None
i = 0
#for i in range(tam-1):
while(i < tam):
	#j = i + 1
	j = 0
	while( j < tam):
		if( i == j):
			j += 1
			continue
		#print i,j
		aux = findOneDiff( vec[i], vec[j], con, vec)
		if(aux != None):
			# now, to clear the screen
			vec[i] = aux
			#print(len(vec))
			vec.pop(j)
			#print(len(vec))
			#raw_input()
			j -= 1
			tam -= 1
		j += 1
	i += 1



#############################################################################
#
# 						Isso imprime a tabela
#  precisa de "con" e "vec", saida usada apenas para imprimir no arquivo.
#############################################################################


#print str(con).replace("[","").replace("]","").replace("'","")
saida.write( str(con).replace("[","").replace("]","").replace("'","") + "\n" )
cls()
for x in vec:
	#print str(x[0]).replace("[","").replace("]","").replace("'","") + ",",
	saida.write( str(x[0]).replace("[","").replace("]","").replace("'","") + "," + "," )
	#print str(x[1]).replace("[","").replace("]","").replace("'","")
	saida.write( str(x[1]).replace("[","").replace("]","").replace("'","")  + "\n" )

imprimeTab(con, vec)

arq.close()
saida.close()
