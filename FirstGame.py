# Snake,Water,Gun game using python
Computer = -1
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

Youstr = input("Enter Your Choice (s for snake, w for water, g for gun): ")
you = youDict[Youstr]

print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[Computer]}")
if Computer == you:
    print("match draw")
else:
    if (Computer == -1 and you == 1):
        print("You win!")
    elif (Computer == -1 and you == 0):
        print("You loss!")
    elif (Computer == 1 and you == -1):
        print("You loss!")
    elif (Computer == 1 and you == 0):
        print("You win!")
    elif (Computer == 0 and you == 1):
        print("You loss!")
    elif (Computer == 0 and you == -1):
        print("You win!")
