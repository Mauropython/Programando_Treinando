"""


print("1")

n = 0
while n < 10:
  n +=1
  print(n)

print("2")

"""

"""
# não imprimi pois o valor de x não é igual a 25
x = 25
if(x==24):
  print('x é igual a 25 ?')

"""
"""
a = int(input("Digite '1' para está vermelho e digite '2' para está verde:"))
if(a==1): # Se
  print("Você disse que está vermelho !")



else:
  if(a== 2):
    print("Você disse que está verde !")

  else:
    print("O sinaleiro não está nem 'vermelho' e nem 'verde'! VERIFIQUE:")

"""

"""

variavel = '56765576757'
numbers = 30
lista = ['izalu','maurício','lola']

if 'carlos' in lista:
  print('yes')

elif variavel == 'maurício':
  print('Opa, é o maurício')


else:
  print('no')

if numbers >= 40:
  print('numbers é maior')

else:
  print('numbers não é maior')


print('Passou direto para cá!')

# Elif é o else: com if

"""

"""

# Teste de condições IF com FOR

lista = ['izalu','maurício','lola', 'tommy']

for nome in lista:
  if nome == 'maurício':
    print('É o maurício')
  else:
    print('Não é o maurício')

"""

#Classificação de ordem

ordens = ['100','200','300','400','500','47384', '549393', '3434583']

for ordem in ordens:
  if ordem[0] == '2':
    print(f'A ordem {ordem} é uma manutenção preventiva')
  elif ordem[0] == '3':
    print(f'A ordem {ordem} é uma manutenção corretiva')
  elif ordem[0] == '4':
    print(f'A ordem {ordem} é uma manutenção nativa')
  else:
    print(f'A ordem {ordem} é uma manutenção preditiva')
