import random

print("*********************")
print("BEM-VINDE AO GUESS ME")
print("*********************")

random_number = random.randrange(1,101)
level_check = False

while (level_check == False):
    
    print("Escolha o nível de dificuldade\n")
    print("[ 1 ] FÁCIL")
    print("[ 2 ] INTERMEDIÁRIO")
    print("[ 3 ] DIFÍCIL")

    level = int(input(""))

    if (level == 1):
        tries = 20 
        level_check = True
    elif (level == 2):
        tries = 10
        level_check = True
    elif (level == 3):
        tries = 5
        level_check = True
    else:
        print("esse nível não existe :P")
        continue       

for round in range(1,tries + 1):

    print("Tentativa {} de {}".format(round, tries))   
    guess = int(input("Digite um número entre 1 e 100: "))
    
    hit = guess == random_number
    bigger = guess > random_number
    smaller = guess < random_number

    

    if(hit):
        print("Você acertou! Te espero de novo <3")
        break
    else:
        if(guess < 1 or guess >  100):
            print("Você digitou um número inválido :P")
            continue
        elif(smaller):
            print("Você deveria chutar um pouco mais alto")
        elif (bigger):
            print("uou, muito alto. Eu sou um pouco menor")

if(hit == False): 
    print("Fim de jogo. O número secreto era {}. Te espero de novo!".format(random_number))