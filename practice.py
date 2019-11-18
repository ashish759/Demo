secret_number  = 9
guess_count = 0
maximum_guess = 3

while (guess_count < maximum_guess):
    guess = int(input("Guess ?"))
    guess_count +=1
    if guess==secret_number:
        print("you won")
        break
    else :
        print("try again")
    
        

