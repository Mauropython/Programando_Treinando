
"""
print("Alo Mundo!")

if True:
    print("tchau")

print("oi"); print("tchau");

#variáveis

a = 10
print(a)
b = 25
print(b)
print(a + b)
texto = "todo texto é uma String"
print(texto)

#Saber o tipo de variável (modelo da variável)

n1 = 23

print(type(n1))
print(type(a))
print(type(texto))

dinheiro = 100.15
print(type(dinheiro))

#Nomenclatura dos objetos

#Manipulação de dados

num_int = 5
num_dec = 7.3
val_str = "qualquer texto"

#Formas de print de num_int

print("o valor é:", num_int)
print("o valor é: %i" %num_int)
print("o valor é: " + str(num_int))

#Ponto flutuante

print("contatendo decimal:", num_dec)
print("contatendo decimal: %.10f" %num_dec)
print("contatendo decimal:" + str(num_dec))

print("contatendo strings", val_str)
print("contatendo strings %s" % val_str)
print("contatendo strings" + val_str)


#Entrada de dados

login = input("login:")
senha = input("senha:")
print("o usuário informado foi: %s, e a senha digitada foi: %s" %(login, senha))



print(type(10 + 10))
print(10+(50+50))

#Treinamento


dados = (input("Informar seus dados completos:"))
cpf = (input("informar a numeração:"))
print(dados + cpf)


operacao = input("Digite a operacao desejada (soma, sub, mult, div): ")
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")



O termo IF em inglês significa SE e ELSE significa SENÃO.
Eles são utilizados para controlar o fluxo do programa, e
decidir se uma parcela de código precisa ou não ser executada.
== significa comparação entre as operações.



if operacao == "soma":
    resultado = int(numero1) + int(numero2)
if operacao == "sub":
    resultado = int(numero1) - int(numero2)
if operacao == "mult":
    resultado = int(numero1) * int(numero2)
if operacao == "div":
    resultado = int(numero1) / int(numero2)
else:
    resultado = "Operação não suportada"

print("O resultado da operação é: " + str(resultado))


#Módulo de divisão, ou seja entre a % não a sobras no 6 (RESTO DE DIVISÃO)

div = 6 % 2
div2 = 5 % 2
div3 = 7 % 3.1
print(div)
print(div2)
print(type(div3))


# % resto da divisão

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
divisao = num1 / num2
resto = num1 % num2
print()
print(num1, "dividido por", num2, "é igual a: ", divisao)
print("O resto da divisão entre ", num1, "e", num2, "é igual a:", resto)

#Potenciação e radiciação


potencia = 5 ** 2
potencia2 = 2 ** 8
print(potencia)
print(potencia2)

import math
dir(math)
math.pi



Operadores relacionais

Operadores de igualdade

Exemplos abaixo:

= igualdade
!= diferente
x == y / x é igual a y
x != y / x é diferente de y



a = 100 == 100
print(a)
b = "a" == "a"
print(b)
c = "a" == "b"
print(c)
d = "a" != "a"
print(d)
e = "a" != "c"
print(e)
f = False == False
print(f)
g = False != True
print(g)



Operadores diferenciais

> maior que:
< menor que:
>= maior ou igual que:
<= menor ou igual que:



a = 10 > 5
b = 100 < 250
c = 10 >= 30
d = 123 <= 12
e = (5 < 5.1) or (5 == 5.1)
print(a, b, c, d)
print(e)

#Exercícios


nome = ("Maurício Gonçalves Portella")
print(nome)

nome1 = (input("O seu nome é: "))
idade = (input("Sua idade é:"))
print(nome1, idade)

n5 = 30
print(n5)

numeros = (input("Informe um número: "))
print("O número digitado foi", (numeros))




n10 = int(input("Digite o primeiro número:"))
n20 = int(input("Digite o segundo número:"))
n30 = int(input("Digite o terceiro número:"))

print("A soma total é:", (n10 + n20 + n30))

x = int(input("Digite o primeiro número:"))
y = int(input("Digite o segundo número:"))

print("A soma entre x e y é igual a: ", (x + y))




p1 = float(input("Prova 1:"))
p2 = float(input("Prova 2:"))
p3 = float(input("Prova 3:"))
p4 = float(input("Prova 4:"))

media = p1 + p2 + p3 + p4 / 4

print("A média das provas é: ", media)




metro = float(input("Informe um valor em metros:"))
resultado = metro * 100
print(metro,"metros equivale a ", resultado, "cm")


dias = int(input("Digite a quantidade de dias:"))
horas = float(input("Digite a quantidade de horas:"))


acao = int(input("Digite '1'para sim e '2' para não:"))
if acao == 1:
    print("Você disse que sim!")
else:
    if acao ==2:
        print("Você disse que não!")
    else:
        print("O número digitado não é nem '1'e nem '2'!!!")



idade = int(input("Digite a sua idada:"))
if idade <=0:
    print("Sua idade não pode ser 0 ou menor do que 0!")
elif idade>150:
    print("A sua idade não pode ser superior a 150 anos !!")
elif idade<18:
    print("Você precisa ter mais do que 18 anos !!")





num1 = (input('Digite o primeiro número:'))
num1 = int(num1)

num2 = (input("Digite o segundo número:"))
num2 = int(num2)

if num1==num2: # operador de igualdade
    print('O numero %d é igual a %d.'% (num1, num2))
if num1!=num2: # operador de diferença
    print('O numero %d é diferente de %d.'% (num1, num2))
if num1<num2: # operador menor
    print("O numero %d é menor que %d."% (num1, num2))
if num1>num2: # operador maior
    print("O numero %d é maior que %d."% (num1, num2))
if num1<=num2: # operador menor ou igual que
    print("O numero %d é menor ou igual que %d."% (num1, num2))
if num1>=num2: # operador maior ou igual que
    print("O numero %d é maior ou igual que %d."% (num1, num2))



v = 2<4 and 8!=8
a = not(40<50)
s = (1==1 and 2!=1 or 1<2 and 1>3)
b = (450 + 850 == 500 - 800) or (500 * 5 > 400 * 7)
print(v, a, s, b)

"""

n1 = int(input('Digite o numero:'))
if(n1 > 10):
    if(n1<=15):
        print('O valor é maior do que 10, mas menor do que 15')
    else:
        if(n1<=50):
            print('O valor é maior do que 10, mas menor que 50!')
        else:
            print('O valor é maior do que 50!')
    print('O numero é maior do que 10!')
else:
    if(n1>5):
        print('O numero é menor do que 10 mas maior do que 5!')
        if(n1==7):
            print('o numero é igual a 7.')
            if(n1!=7):
                print('O numero é diferente de 7!')
            else:
                print('O numero não é difetente de 7!')

    else:
        print('O valor é menor do que 5.')

