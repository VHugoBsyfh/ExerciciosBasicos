#faça um programa que receba como entrada 3 numeros inteiros
#e mostre como resultado qual é o maior dos 3
n1=int(input("Primeiro numero:"))
n2=int(input("Segundo numero:"))
n3=int(input("terceiro numero:"))
if(n1>n2 and n1>n3):
    print("{} é o maior numero".format(n1))
if(n2>n1 and n2>n3):
    print("{} é o maior numero".format(n2))
if(n3>n2 and n3>n1):
    print("{} é o maior numero".format(n3))

