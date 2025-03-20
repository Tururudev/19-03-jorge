print("Digite uma palavra")
palavra = input()
cont_vogais = 0
cont_consoantes = 0

for letra in palavra:
    if letra in "aeiou":
        cont_vogais = cont_vogais + 1
    
    elif letra.isalpha(): 
        cont_consoantes = cont_consoantes + 1 
        
print("O numero de vogais e:",cont_vogais,",O numero de consoantes e:", cont_consoantes)   

