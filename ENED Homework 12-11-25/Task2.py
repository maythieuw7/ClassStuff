import random as r
def play():
    #make varidables
    wins, init, pred, value = 0, 0, "", ""
    n = int(input("Enter the number of rounds:"))
    #check to make sure the integer is valid
    while n < 1:
        print("Please enter a valid integer")
        n = int(input("Enter the number of rounds:"))
        #make the initial roll
        init = r.randint(1,6)
        #start main loop
    for i in range(n):
        print(f"The Initial Roll is {init}")
        #get the prediction from the user and then make sure it is valid
        pred = input("Enter Predicition for next roll (High, Tie, Low)\n").lower()
        while True:
            if pred in ["high", "tie", "low"]:
                break
            else:
                print("Please enter a valid value")
                pred = input("Enter Predicition for next roll (High, Tie, Low)\n").lower()
        #generate the roll for the next turn
        curr = r.randint(1,6)
        #make a value that can be compared (this could prob be simplified but my though was that I need a value I can compared a string to)
        if curr > init:
            value = "high"
        elif curr == init:
            value = "tie"
        else:
            value = "low"
        #now compare and make a score
        if (value == pred):
            wins += 1
            print("Correct")
        else:
            print("Incorrect")
        init = curr
    #print the stats
    print(f"Number of rounds: {n}")
    print(f"Percent Wins: {((wins / n)*100):.2f}%")
play()
#I have added the comments after typing this because I realized my code is so unreadable