import random

def comp_turn():
    elements = ['snake', 'water', 'gun']
    computer = random.choice(elements)
    return (str(computer))
def your_turn():
    choose = input("Choose whether you want to be Snake, Water or Gun: ").lower()
    return choose

print("Welcome to our Snake, Water and Rock game.".center(80,"!"))
sum = 0
w = 0
n = 1
while True:
    b = your_turn()
    a = comp_turn()
    print("Computer: ", a)

    if(a == b):
        print("Its a draw in this round")
        i= 0
    elif((a == "snake" and b=="water")or (a == "water" and b=="gun") or (a == "gun" and b=="snake")):
        print("Computer wins. Sorry, you lost!")
        i= -1
    elif((b == "snake" and a=="water")or (b == "water" and a=="gun") or (b == "gun" and a=="snake")):
        print("Congrats! you have won")
        i= 1
        w += 1
    else:
        print("Invalid word send.")
        continue
    sum += i 
    q = input("Do you want to continue or Quit: ").lower()
    if(q == "quit"):
        break
    else:
        n += 1

print(f"Thank you for playing our game today. The number of times you have played is {n} and won {w} games. Your total points earned is {sum}.")
