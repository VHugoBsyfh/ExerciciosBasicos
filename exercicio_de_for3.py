#Faça um programa que receba como dado de entrada 2 notas de 5 alunos e mostre como resultado:
#A)qual foi a maior media da turma?
#B)qual foi a media da turma

maxmedia = 0  # media maxima
mediat = 0  # media total
for i in range(1,6):
	nome_aluno=input("Nome do aluno {}:".format(i))
	n1= float(input("Qual foi a sua primeira nota?"))
	n2= float(input("Qual foi a sua segunda nota?"))
	media=(n1+n2)/2
	mediat+=media
	if(media > maxmedia):
		maxmedia = media
print("A maior media da turma é {}".format(maxmedia))
print("A media da turma é {}".format(mediat/5))


