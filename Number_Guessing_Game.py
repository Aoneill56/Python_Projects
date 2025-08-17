import random # Import the random module

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter a low number to guess / start with : ")) # converts to integer and accepts input
high = int(input("Enter a higher number to guess between the lower number you previously entered: ")) # Same as above

print(f"You have 7 guesses to guess between the {low} and the {high} numbers you previously entered") #F string to add variables low and high

num = random.randint(low, high) # The actual random number within the range of low and high they have to guess
ch = 7 # Total number of chances 
guess_counter = 0 # w will increment this on every failed guess
guesses_left = 7 # Total number of guesses left


while guess_counter < ch: # loop through this condition, until the Guess counter is lower than chanches, run the code below
    guess_counter +=1 # On every loop / interation increment the variable by 1
    guess = int(input("Please enter your guess using numeric digits: ")) # Input for taking a guess at the number / converted to an interger
    guesses_left -= 1 # Like the guess_counter it does the opposite and counts down on every loop


    if guess == num: # if statement for flow control combined with a comparison operator - if guess variable is equal to the num variable (I.E you guess right)
        print("That's correct!, great job!, you win!") # Then print this string
        break # Break the Loop if you guess right, otherwise it will keep going through the elif flow control statements

    elif guess_counter >= ch and guess != num: # Incase it's something else, i.e G_C is less then or equal to chances and Guess is not equal to num then print below
        print("Sorry, you lose, re-run the program and try again!")

    elif guess > num: # if the guess it higher then the randomly generated number, print below
        print(f"That's too high, try a lower guess + you have {guesses_left} guesses left")
    
    elif guess < num: # If it's too low, print below
        print(f"That's too low of a guess, try again + you have {guesses_left} guesses left")
