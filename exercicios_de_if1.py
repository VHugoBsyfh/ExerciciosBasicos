#pergunte a idade do usuário e mostre se é maior de idade ou não
n = int(input("Digite sua idade meu consagrado:"))
if (n >= 18):
    print("Você é maior de idade")
elif (n < 18 and n >= 0):
    print("Você é menor de idade")

else: print("numero inválido")

