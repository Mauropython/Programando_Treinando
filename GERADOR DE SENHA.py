import random
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '@#$%&*()!-_'

#Soma todas as Strings e coloca apenas em uma linha (forpass)

for_pass = lower_case + upper_case + numbers + symbols

tamanho_da_senha = 8

password = "".join(random.sample(for_pass, tamanho_da_senha))
print('A senha gerada foi:', str(password))