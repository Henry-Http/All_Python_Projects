if __name__ == '__main__':
    take_input = int(input("Enter a number: "))
    count = 1
    sum_count = 0

    while count < take_input:
        if take_input % count == 0:
            print("The factor of ", take_input, " is ", count)
            sum_count = sum_count + count
        count = count + 1

    print("\nThe sum is: ", sum_count)
    if sum_count == take_input:
        print("It is a perfect Number")
    else:
        print("It is not a perfect numer")
