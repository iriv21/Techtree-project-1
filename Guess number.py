
print("Welcome to the GUESSING game!\n")


import random


def lets_play():
    from statistics import mode
    from statistics import median
    
    ready_player = input("Do you want to play the guessing game? Y/N: ")
    guess_count_list = []
    while ready_player == "y":
        random_number = random.randint(1,100)
        name = input("To begin, enter a name: ")
        guess_count = 0
        while lets_play != random_number:
            try:
                guess = int(input("Hi {}, guess a number between 1-100: ".format(name)))
                guess_count +=1
                pass
            except ValueError as err:
                print("Invalid answer. Try again.")
            if guess < random_number:
                print("This number is too low, try again.")
            elif guess > random_number:
                print("This number is too high, try again.")
            elif guess == random_number:
                print("\n{}, you beat the GUESSING game!".format(name))
                break    
        print("It took you", guess_count, "tries to beat the game.\n")
        ready_player = input("Do you want to play the guessing game? Y/N: ")
        if ready_player == "n":
            guess_count_list.append(guess_count)
            mean = sum(guess_count_list)// len(guess_count_list)
            print("The mean of your game is ", mean)
            median = median(guess_count_list)
            print("The median of your game is ", median)
            mode_player = mode(guess_count_list)
            print("The mode of your game is ", mode_player)
    else:
        print("Aww sad to see you go. Goodbye {}".format(name))
        
    
lets_play()

