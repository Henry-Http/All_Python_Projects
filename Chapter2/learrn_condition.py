def first_func():
    count = 0
    while count < 3:
        user_input = int(input("Enter Grade: "))
        grade = user_input
        if 90 <= grade <= 100:
            print("A")
        elif 70 <= grade <= 89:
            print("B")
        elif 50 <= grade <= 69:
            print("C")
        elif 40 <= grade <= 49:
            print("D")
        elif 30 <= grade <= 39:
            print("E")
        elif 0 <= grade <= 29:
            print("\nYOU FAILED : ZERO TALENT")
        else:
            print("enter a valid grade")
        count += 1

        if count == 3:
            print("bye")
            break


if __name__ == '__main__':
    first_func()
