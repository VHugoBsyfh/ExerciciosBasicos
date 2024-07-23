#faça um programa que receba como dados de entrada o valor de uma compra e a quantidade de parcelas e mostre como resultado:
#a)compra com parcelas ate 3x, mostrar o valor da compra com juros de 3%
#b)compra com parcelas a cima de 3, mostrar o valor da compra com 10% de juros
#c)valor pago a vista, mostrar a compra com desconto de 5%


c = float(input("Qual o valor máximo da compra?"))
qp = int(input("Digite 1 para pagar a vista \nou a quantidade de parcelas desejadas:"))
calculo = 0
if(qp >= 2 and qp <= 3):
	calculo = c+(0.03*c)
	print("O valor final fica: {}".format(calculo))

elif(qp > 3):
	calculo = c+(0.1*c)
	print("O valor final fica: {}".format(calculo))

elif(qp == 1):
	calculo = c-(0.05*c)
	print("O valor final fica: {}".format(calculo))

else: print("opcao invalida")
