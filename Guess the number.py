# PROMPT   BUILDS   &    CONVERSION   EMBEDDED   IN   CONDITIONALS
""" Invoking All Needed Modules,
 Building Function In A Function...
       Where Lists Are Generated And Iterated """
#----------------------------------------------------------
import time
import random
#----------------------------------------------------------

def test(Lst):
    time.sleep(2)
    print 'List will now be shuffled...\n...'
    time.sleep(2)
    print 'Shuffling...\n ...'
    random.shuffle(Lst)
    time.sleep(3)
    print 'Shuffled!'
    time.sleep(2)
    print 'List = ',Lst
    time.sleep(2)
    print 'A number will now be chosen from the list...'
    time.sleep(2)
    print 'Choosing...'
    time.sleep(3)
    print 'Chosen!'
    time.sleep(2)
    print 'Now, can you guess ...?'
    time.sleep(4)
    choice = random.choice(Lst)
# Handles errors in players choices, must be a number!!
    while True:
        guess1 = raw_input('Player1 guess: ')
        valid1 = guess1.isdigit() is True
        if valid1 is False:
            print "You've entered alphabet(s),and so..."
            time.sleep(2)
            print 'An unexpected failure occured...'
            time.sleep(3)
            continue
        else:
            Player1 = int(guess1)
            break
    while True:
        guess2 = raw_input('Player2 guess: ')
        valid2 = guess2.isdigit() is True
        if valid2 is False:
            print "You've entered alphabet(s),and so..."
            time.sleep(2)
            print 'An unexpected failure occured...'
            time.sleep(3)
            continue
        else:
            Player2 = int(guess2)
            break     
    if  Player1 == choice and Player2 == choice:
        print 'Splendid!!'
        time.sleep(2)
        print 'Confirmation:',choice
        time.sleep(1.5)
        print 'Both player wins!!'
    elif Player1 == choice and Player2 != choice:
        print 'Player1 is Correct!\n...Player2 lost'
        time.sleep(2)
        print 'Confirmation:',choice
        time.sleep(1.5)
        print 'Player1 wins!!'
    elif Player1 != choice and Player2 == choice:
        print 'Player2 is Correct!\n...Player1 lost'
        time.sleep(2)
        print 'Confirmation:',choice
        time.sleep(1.5)
        print 'Player2 wins!!'
    elif Player1 != choice and Player2 != choice:
        print 'Wrong!'
        print 'Here it is...'
        time.sleep(1)
        print 'Choice:',choice
        time.sleep(1.5)
        print 'Both player lost'



# =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  = 



def Rng_cond(freq):
    if freq > 2 and freq <=  10:
        #creates a list and a dictionary... really needed, especially below.
        Lst = list()
        check = dict()
        while True:
            for lst in range(freq):
            #makes sure the elements in the list is never empty!
                try:
                    inp = int(raw_input("Enter number: "))
                    li = Lst.append(inp)
                except:
                    Lst = []
                    print 'Must be all numbers!'
                    print 'Start Again...'
                    break
            #checks each element in the list such that there is no repetition of numbers
            #by creating a dictionary and getting its values greater than 1! QED!!
            for each in Lst:
                if each not in check:
                    check[each] = 1
                else:
                    check[each] += 1
            doublecheck = check.values()
            for each in doublecheck:
                if each > 1:
                    print 'You cannot repeat a number\nStart Again!'
                    Lst = []
                    check = {}
            #breaks away from the infinite loop if and only if all elements in the list is valid!!
            if len(Lst) == freq:
                break
            else: continue
                       
        print 'Processing... '
        time.sleep(1)
        print 'Initial list...'
        time.sleep(2) 
        print Lst
        test(Lst)

#  FINAL   LOOP   EXECUTION
""" Indefinte Looping...
        Masked And Modified With Conditionals; As Well As Function Calls """

while True:
    Inp = raw_input("How many possible choices? : ")
    if len(Inp) == 0: continue
    elif Inp.lower() == 'close' or Inp.lower() == 'exit' or Inp.lower() == 'done': break    
    try:
        freq = int(Inp)
        if freq < 3 or freq > 10:
            print 'Can only process between 3 - 10 choices!'
            continue
        print 'Please enter ' + str(freq) + ' numbers'
    except:    
        print 'An unexpected failure occured...'
        time.sleep(2)
        print '...\nPlease enter a number'
        time.sleep(1)
        continue 
    # DETERMINE   THE   RANGE   AND   PRINT   THE   LIST
    Rng_cond(freq) 
    print 'Play again?'
    ans = raw_input('Yes/No: ')
    if ans.lower() == 'yes' or ans.lower() == 'y':
        continue
    elif ans.lower() == 'no' or ans.lower() == 'n':
        break
    else:
        while True:
            print 'Play again?'
            ans = raw_input('Yes/No: ')
            if ans.lower() == 'yes' or ans.lower() == 'y': break
            elif ans.lower() == 'no' or ans.lower() == 'n':
                break
        break
    
print 'Done!'
