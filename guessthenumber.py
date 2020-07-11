#guess the number and win the game
num=4
chance=1
n1=int(input("Enter the number of guesses given to user"))
while(chance<=n1):
    n = int(input("Enter the number which is guessed by the user-"))
    if(n>num):
        print("thoda ghatao")
    elif(num>n):
        print("thoda badhao")
    else:
        print("got it")
        print("The chances used:",chance)
        if(n1>=chance):
            print("The chances left:",n1-chance)
            chance=n1+1
    chance=chance+1
else:
    print("game over")
if(n1+1==chance):
    print("you don't guess correctly ")