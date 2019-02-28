import grader

'''
Week 2: Programming Assignment 1

You should download this assignment and run this in your IDE (e.g. Visual Studio Code). Once you are done
modifying the code, you can run it on your terminal. Don't change any lines of code unless it says to.

The program currently returns an error! Please fix it so that it will return the right thing. You can 
solve this in two ways. Try both!
1. Change lines 22 and 23
2. Change line 25 and 26

sentence_1 should store "Sean scored 4th place at the coding competition!"
setnence_2 should store "Claire scored 5th place at the coding competition!"
'''

person_1 = "Sean"
person_2 = "Claire"

message = " place at the coding competition!"
fourth = str(4)   # Modify this line for solution 1
fifth = str(5)    # Modify this line for solution 1

sentence_1 = person_1 + " scored " + fourth + "th" + message   # Modify this line for solution 2
sentence_2 = person_2 + " scored " + fifth + "th" + message    # Modify this line for solution 2

# You can ignore this line! This is just for testing your code. :)
grader.grade2(sentence_1, sentence_2)