from graphics import *;
from random import randint


wordList = []
file = open("words.txt")
for x in file:
    wordList.append(x)
constant = 2
lineNum = randint(0,283)
wordSelect = wordList[lineNum]

#Code For scramble 
deletedWord = wordSelect
scramble = ''
i = 0
for x in range(len(wordSelect)-1):
    length = len(wordSelect) - (constant + i)
    charPos = randint(0,length)
    letter = deletedWord[charPos]
    deletedWord = deletedWord[:charPos] + deletedWord[charPos+1:]
    scramble = scramble + letter
    i = i + 1

#Code For Attaching Each Letter Of The Selected Word Into One String
officalWord = ''
for x in range(len(wordSelect)-1):
    pie = wordSelect[x]
    officalWord = officalWord + pie

#Code For Printing Scrambled Word + User Guessing
print(scramble)
print(officalWord)

window = GraphWin("Window", 500,500);
window.setBackground('OldLace')
scramble = Text(Point(250,150),scramble)
scramble.setTextColor('RosyBrown4');
scramble.setFace('times roman')
scramble.setStyle('bold')
scramble.setSize(36)
scramble.draw(window)

won = Text(Point(250,460),'Correct!')
won.setTextColor('RosyBrown3');
won.setFace('times roman')
won.setStyle('bold')
won.setSize(28)
lost = Text(Point(250,460),'Try Again!')
lost.setTextColor('RosyBrown3');
lost.setFace('times roman')
lost.setStyle('bold')
lost.setSize(28)

#print(officalWord)
while(True):
    entryBox = Entry(Point(250,420),30)
    entryBox.setFill('white')
    entryBox.draw(window)
    window.getMouse();
    answer = entryBox.getText()
    lost.undraw()
    if(answer == officalWord):
        won.draw(window)
        break;
    else:
        lost.draw(window)
        
window.getMouse();
window.close();


        
