from Part_1 import *
import time



# Computer chooses a word

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    bestScore = 0  
    bestWord = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if (score > bestScore):
                bestScore = score
                bestWord = word
  
    return bestWord

# Computer plays a hand
    
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalScore = 0
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word == None:
            break
        else :
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            else : 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                hand = updateHand(hand, word)
                print()
    print('Total score: ' + str(totalScore) + ' points.')
    
# Playing a game
    
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    ch1=''
    ch=''
    count=0
    prevhand=''
    while True:
        while(ch!='n' or ch!='r' or ch!='e'):
            ch=input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            if(ch=='n' or ch=='e'):
                break
            elif(ch=='r' and count==0):
                print("You have not played a hand yet. Please play a new hand first!")
            elif(ch=='r' and count!=0):
                break
            else:    
                print("Invalid input. Please try again.")
        while(ch1!='u' or ch1!='c'):
            if(ch=='e'):
                break
            ch1=input("Enter u to have yourself play, c to have the computer play: ")
            if(ch1=='u' or ch1=='c'):
                break
            print("Invalid input. Please try again.")
        if(ch=='e'):
            break
        if(ch=='n' and ch1=='u'):
            prevhand=dealHand(HAND_SIZE)
            playHand(prevhand, wordList, HAND_SIZE)
        if(ch=='r' and ch1=='u'):
            playHand(prevhand,wordList,HAND_SIZE)
        if(ch=='n' and ch1=='c'):
            prevhand=dealHand(HAND_SIZE)
            compPlayHand(prevhand,wordList,HAND_SIZE)
        if(ch=='r' and ch1=='c'):
            compPlayHand(prevhand,wordList,HAND_SIZE)
        count+=1
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


