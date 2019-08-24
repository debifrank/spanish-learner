#!/usr/bin/python
# coding=utf-8

import random, sys
from nounsDictionary import nounsDict
from verbsDictionary import verbsDict
from questionsDictionary import questionsDict
from colorama import init

init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('SPANISH - LEARNER', font="slant"), "red")

def askQuestion(dictionary):
    thisQuestion, correctAnswer  = random.choice(list(dictionary.items()))
    while True:
        notQuestion1, wrongAnswer1 = random.choice(list(dictionary.items()))
        if wrongAnswer1 != correctAnswer:
            break
    while True:
        notQuestion2, wrongAnswer2 = random.choice(list(dictionary.items()))
        if wrongAnswer2 != correctAnswer and wrongAnswer2 != wrongAnswer1:
            break
    while True:
        notQuestion3, wrongAnswer3 = random.choice(list(dictionary.items()))
        if wrongAnswer3 != correctAnswer and wrongAnswer3 != wrongAnswer2 and wrongAnswer3 != wrongAnswer1:
            break
    
    print("What does '" + thisQuestion + "' mean in english?")
            
    correctNumber = random.randint(1,4)
            
    if correctNumber is 1:
        print("(1) : " + correctAnswer)
        print("(2) : " + wrongAnswer1)
        print("(3) : " + wrongAnswer2)
        print("(4) : " + wrongAnswer3)
    if correctNumber is 2:
        print("(1) : " + wrongAnswer1)
        print("(2) : " + correctAnswer)
        print("(3) : " + wrongAnswer2)
        print("(4) : " + wrongAnswer3)
    if correctNumber is 3:
        print("(1) : " + wrongAnswer1)
        print("(2) : " + wrongAnswer2)
        print("(3) : " + correctAnswer)
        print("(4) : " + wrongAnswer3)
    if correctNumber is 4:
        print("(1) : " + wrongAnswer1)
        print("(2) : " + wrongAnswer2)
        print("(3) : " + wrongAnswer3)
        print("(4) : " + correctAnswer)
    
    print("Answer: ")
    answer = int(input())
    if answer == correctNumber:
        print("Correct!")
    else:
        print("Incorrect! The Correct answer is '" + correctAnswer + "'.")
    print("----------------------------------------------------------------")         
 

while True:

    random.seed()
    
    print("Would you like to see a question (1), noun (2), or verb (3), or quit (0)?")

    choice = int(input())
     
    if choice is not 1 and choice is not 2 and choice is not 3:
        if choice is 0:
            cprint(figlet_format('GOODBYE!', font="slant"), "red")
            sys.exit()
        cprint(figlet_format("Error", font="slant"), "red")
    
    if choice is 1:
        askQuestion(questionsDict)
    if choice is 2:
        askQuestion(nounsDict)
    if choice is 3:
        askQuestion(verbsDict)       
