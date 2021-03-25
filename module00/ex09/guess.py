from random import randint

lucky_number = randint(1, 99)

print(lucky_number)


def game_prompt():
    num = 0
    n = 0
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    print("")
    while True:
        print("What's your guess between 1 and 99?")
        num = input(">> ")
        if num == "exit":
            print("Goodbye!")
            exit(0)
        else:
            if num.isdigit():
                num = int(num)
            else:
                print("That's not a number.")
        if num == lucky_number:
            if lucky_number == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if n == 0:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in {n} attempts!".format(n=n))
            exit(0)
        n += 1


game_prompt()
