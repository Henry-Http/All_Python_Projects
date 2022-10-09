import random

random_guess = random.randint(1, 10)
counter = 4
count = 0
while count <= 3:
    user_input = int(input("Enter a number btw 1 and 10: "))

    if user_input < 0 or user_input > 10:
        print("Number out of range, try again!!!\n")
        continue
    if user_input == random_guess:
        print("You guessed right!!!")
        break
    if user_input != random_guess:
        print("wrong guess!!!")
        count += 1
        counter -= 1
        if user_input > random_guess:
            print("You guess was higher the no is: ", random_guess,)
        else:
            print("Your guess was lower the no is: ", random_guess)
        if counter == 1:
            print("You have", counter, "try left\n")
        elif counter == 0:
            print("Goodbye")
        else:
            print("You have", counter, "tries left\n")
