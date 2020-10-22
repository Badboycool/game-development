#My first Game
import random
head=["s","w","g"]

chances=10
num_of_chance=0
your_point=0
computer_point=0

print("----Snake----Water-----Gun-----Game!")
print("Please choose your move below")
print("s for snake \nw for water \ng for gun")

while chances>num_of_chance:
    _input= input("Snake,Water,Gun:  ")
    _random= random.choice(head)
    
    if _input==_random:
        print("It's a Tie ")
    
    elif _input=="s" and _random=="w":
        your_point=your_point+1
        print(F'Your guessed : {_input} and computer guessed: {_random}')
        print(f"You win!  and your points are: {your_point}")
        
        
    
    elif _input=="w" and _random=="s":
        computer_point=computer_point+1
        print(F'Your guessed: {_input} and computer guesses: {_random}')
        print(f"You loose,  computer points are: {computer_point}")
       
    
    elif _input=="g" and _random=="s":
        your_point=your_point+1
        print(F'Your guessed: {_input} and computer guesses: {_random}')
        print(f"You win!  and your points are: {your_point}")
        
    elif _input=="w" and _random=="g":
        your_point=your_point+1
        print(F'Your guessed: {_input} and computer guesse: {_random}')
        print(f"You win!  and your points are: {your_point}")
       
    
    elif _input=="s" and _random=="g":
        computer_point=computer_point+1
        print(F'Your guessed: {_input} and computer guesses: {_random}')
        print(f"You loose,  computer points are: {computer_point}")
        
    elif _input=="g" and _random=="w":
        computer_point=computer_point+1
        print(F'Your guessed: {_input} and computer guessed: {_random}')
        print(f"You loose,  computer points are: {computer_point}")
        
    else:
        print("Your given choice is invalid")
    num_of_chance=num_of_chance+1
    print(f"{chances-num_of_chance} chances are left out of {chances}")
    

if computer_point==your_point:
  print(f"Your points are {your_point} and computer points are {computer_point}")
  print(" Ooops! Match Draw")
elif your_point<computer_point:
  print(f"Your total point are: {your_point} and computer total points are:  {computer_point}")
  print("Bad Luck, You loose ")    
else:
   print(f"Your total point are {your_point} and computer total points are:  {computer_point}")
   print("Congratulations! You Won ")
print('Game over')