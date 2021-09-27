print("*********************")
print("BEM-VINDE AO GUESS ME")
print("*********************")

random_number = 33

guess = int(input("Digite um número: "))

true_guess = guess == random_number
guess_again = guess != random_number
bigger = guess > random_number
smaller = guess < random_number

print("você chutou", guess)

# while(guess_again):
if(true_guess):
    print("Você acertou! <3")
else:
    if(bigger):
        print("uou, muito alto. Eu sou um pouco menor")
    elif(smaller):
        print("Você deveria chutar um pouco mais alto")
