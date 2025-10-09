import random

#'''''''''''''''''''''''''''''''
# Question #1 GUESS THE NUMBER
#'''''''''''''''''''''''''''''''
counter = 4
for i in range(5):
    random_no = random.randrange(1,1000)
    user_guess = input("Guess a number: ")
    if random_no== int(user_guess):
        print("You Won the Game")
        break
    else:
        print("Computers Selection : "+ str(random_no))
        print("Player's guess "+ str(user_guess)+ " is not right.Try again! ")
        print(i)
        print("")
        if i == counter:
            print("Better luck next time")
    #print (random_no)


#'''''''''''''''''''''''''''''''
# Question #2 WORD  SCRAMBLE
#'''''''''''''''''''''''''''''''

words = {"python","javascript","java","automation","pytest","guvi","selenium"}
selected_word = (words.pop())
#print(selected_word)
print("/n")
Myname = selected_word #"Sujatha"
scrambled_word = "".join(random.sample(Myname, len(Myname)))
print("Unscramble the word : " + scrambled_word.capitalize())
for j in range(3):
    users_answer = input("Enter your answer :  ")
    if (Myname.upper()) == (users_answer.upper()):
        print("Wohoo! You did it! Your answer is correct")
        break
    else:
        print("Oh no! Answer is incorrect. Try again!")
        print("/n")

