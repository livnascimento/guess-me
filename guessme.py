print("*********************")
print("BEM-VINDE AO GUESS ME")
print("*********************")

random_number = 33
tries = 3

for round in range(1,tries + 1):

    print("Tentativa {} de {}".format(round, tries))   
    guess = int(input("Digite um número entre 1 e 100: "))
    
    hit = guess == random_number
    bigger = guess > random_number
    smaller = guess < random_number

    if (guess < 1 | guess >  100):
        print("Você digitou um número inválido :P")
        continue

    if(hit):
        print("Você acertou! <3")
        break
    else:
        if(bigger):
            print("uou, muito alto. Eu sou um pouco menor")
        elif(smaller):
            print("Você deveria chutar um pouco mais alto")

print("Fim de jogo. Te espero de novo!")