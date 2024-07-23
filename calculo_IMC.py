peso = float(input("informe seu peso:"))
altura = float(input("informe sua altura"))
imc = peso/(altura*altura)

if (imc < 18.5):
    print("seu IMC eh {} ou seja, voce esta a baixo do peso!".format(imc))

elif (imc <= 25):
    print("seu IMC eh {} ou seja, voce esta com o peso normal!".format(imc))

elif (imc <= 30):
    print("seu IMC eh {} ou seja, voce esta a cima do peso!".format(imc))

if (imc > 30):
    print("seu IMC eh {} ou seja, voce esta OBESO!".format(imc))