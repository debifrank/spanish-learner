#!/usr/bin/python
# coding=utf-8

from appJar import gui
import sys, random
from nounsDictionary import nounsDict
from verbsDictionary import verbsDict
from questionsDictionary import questionsDict

correctAnswer = ""

def createQuestionWindow(dictionaryToUse):
    if dictionaryToUse == "nouns":
        thisDict = nounsDict
    if dictionaryToUse == "verbs":
        thisDict = verbsDict
    if dictionaryToUse == "propositions":
        thisDict = questionsDict
    global correctAnswer
    thisQuestion, correctAnswer = random.choice(list(thisDict.items()))
    while True:
        notQuestion1, wrongAnswer1 = random.choice(list(thisDict.items()))
        if wrongAnswer1 != correctAnswer:
            break
    while True:
        notQuestion2, wrongAnswer2 = random.choice(list(thisDict.items()))
        if wrongAnswer2 != correctAnswer and wrongAnswer2 != wrongAnswer1:
            break
    while True:
        notQuestion3, wrongAnswer3 = random.choice(list(thisDict.items()))
        if wrongAnswer3 != correctAnswer and wrongAnswer3 != wrongAnswer2 and wrongAnswer3 != wrongAnswer1:
            break

    correctNumber = random.randint(1,4)

    app.startSubWindow("questions-answers", modal=True)
    app.setSize(400,400)
    app.setBg("gray")
    app.addLabel("question-posed", "What is '" + thisQuestion + "' in english?")
    
    if correctNumber is 1:
        app.addRadioButton("answers", correctAnswer)
        app.addRadioButton("answers", wrongAnswer1)
        app.addRadioButton("answers", wrongAnswer2)
        app.addRadioButton("answers", wrongAnswer3)
    if correctNumber is 2:
        app.addRadioButton("answers", wrongAnswer1)
        app.addRadioButton("answers", correctAnswer)
        app.addRadioButton("answers", wrongAnswer2)
        app.addRadioButton("answers", wrongAnswer3)
    if correctNumber is 3:
        app.addRadioButton("answers", wrongAnswer1)
        app.addRadioButton("answers", wrongAnswer2)
        app.addRadioButton("answers", correctAnswer)
        app.addRadioButton("answers", wrongAnswer3)
    if correctNumber is 4:
        app.addRadioButton("answers", wrongAnswer1)
        app.addRadioButton("answers", wrongAnswer2)
        app.addRadioButton("answers", wrongAnswer3)
        app.addRadioButton("answers", correctAnswer)

    app.addButton("Submit Answer", checkAnswer)
    app.stopSubWindow()
    app.showSubWindow("questions-answers")

def startQuestions(name):
    if name == "Nouns":
        createQuestionWindow("nouns")
    if name == "Verbs":
        createQuestionWindow("verbs")
    if name == "Propositions":
        createQuestionWindow("propositions")

def exitProgram():
    sys.exit()

def checkAnswer(name):
    app.hideSubWindow("questions-answers")
    answerChosen = app.getRadioButton("answers")
    app.startSubWindow("result-window", modal=True)
    app.setSize(200,200)
    if answerChosen == correctAnswer:
        app.setBg("green")
        app.addLabel("result-lb", "CORRECT!!")
    else:
        app.setBg("red")
        app.addLabel("result-lb", "Incorrect.")
        app.addLabel("answer-box1", "The correct answer was:")
        app.addLabel("answer-box2", correctAnswer)
    app.addButton("Close", closeResultBox)
    app.stopSubWindow()
    app.destroySubWindow("questions-answers")
    app.showSubWindow("result-window")

def closeResultBox():
    app.destroySubWindow("result-window")

app = gui("Spanish-Learner")

app.setBg("gray")
app.setFont(12)

app.setResizable(True)

app.addLabel("lb1", "Select a category")

app.addButtons(["Nouns","Verbs","Propositions"], startQuestions)

app.addButton("Quit", exitProgram)
app.go()
