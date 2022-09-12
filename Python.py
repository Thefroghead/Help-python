
import random

num = random.randint(100,999)



print("              ~~~ Welcome to mastermind Game ~~~")
print("Hi gamer, welcome to the Mastermind game")
gname = input("What is your name gamer: ")
print("Hello,"+gname+", Please follow the given instructions to play the game.")

print("")
print("              ~~~GAME INSTRUCTION~~~   ")
print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("When i say:     That means:")
print(" Yellow          One digit is correct but in the wrong position.")
print(" Green           One digit is correct and in the right position.")
print(" Red             No digit is correct.")
print("")
print(""" For example, if the secret number was 346 and your guess was 843, the
 clues would be Green Yellow.""")

print("I have thought up of a number.")
print(" You have 10 guesses to get it.")


n = int(input("Guess 1:"))

if n == num:
    print("Great you have guessed the correct number.")
else:
    
    ctr = 0 
    
    while (n!=num):
        ctr += 1
        
        
        count = 0
        n = int(n)
        
        num = int(num)
        correct = []
          
          # for loop runs 4 times since the number has 4 digits.     
        for i in range(0,9): 
              # checking for equality of digits
              if(n[i] == num[i]): 
                  # number of digits guessed correctly increments
                  count += 1    
                  # hence, the digit is stored in correct[].
                  correct.append(n[i])     
              else:
                  continue
  
          # when not all the digits are guessed correctly.
              if (count < 9) and (count != 0): 
                  print("Not quite the number. But you did get ",count," digit(s) correct!")
                  print("Also these numbers in your input were correct.")
                    
                  for k in correct:
                      print(k, end=' ')
      
                  print('\n')
                  print('\n')
                  n = int(input("Enter your next choice of numbers: "))
      
          # when none of the digits are guessed correctly.
              elif(count == 0):         
                  print("None of the numbers in your input match.")
                  n=int(input("Guess "+ctr+":")) 
      
              if n==num:                
                  print("You've become a Mastermind!")
                  print("It took you only",ctr,"tries.")
            
