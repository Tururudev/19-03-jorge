print("Digite um numero")
numero = input()

soma_digito = 0

for digito in numero:
    if digito.isdigit():
        soma_digito += int(digito)

print("A soma dos digitos foi:", soma_digito)  
    