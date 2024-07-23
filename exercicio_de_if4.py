n = int(input("Digite um valor:"))
if (n<500):
    print("O valor da compra com desconto é {}".format(n-(n*0.05)))
elif (n>=500):
    print("O valor da compra com desconto é {}".format(n-(n*0.1)))
else: print("Resposta inválida")