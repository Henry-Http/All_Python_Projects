if __name__ == '__main__':
    user_input = int(input("Enter your integer: "))
    total = 0

    for x in range(1, user_input):
        if user_input % x == 0:
            print("User input: ", user_input, " factor ", x)
            total += x
            # print("\nTotal == ", total)

    print("\nTotal sum == ", total)
    if total == user_input:
        print("This is a perfect number!")
    else:
        print("Not a perfect number")
