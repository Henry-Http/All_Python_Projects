class AssignmentOne:
    # No1
    @staticmethod
    def grade():
        grade = 90
        if grade >= 90:
            print(f'Congratulations! Your grade of {grade} earns you an A in this course')

    # No2
    @staticmethod
    def egg_count():
        egg = 28
        box = egg // 6
        rem_egg = egg % 6
        extra_box = 6 - rem_egg
        if rem_egg == 0:
            print(f'{box} boxes are needed.')
        else:
            print(f'{box} boxes are needed with a remainder of {rem_egg} eggs.')
            print(f'{extra_box} eggs are needed to complete the box.')

    # No3
    @staticmethod
    def bacteria():
        counter = 0
        hour = 15
        print("Hour \t  Number of bacteria")
        while counter < hour:
            bacteria = 200 * 2 ** counter
            counter = counter + 5
            print(f'{counter} \t\t\t {bacteria}')

    # No4
    @staticmethod
    def wage_calculator():
        salary = 10
        increase = salary((1 + 3) ** 5)

    # No 6
    @staticmethod
    def turing_test():
        input("What is your problem? ")
        user_input = input("Have you had this problem before (yes or no)? ")
        if user_input == "yes":
            print("Well, you have it again.")
        else:
            print("Well, you have it now.")

    # No8
    @staticmethod
    def equilateral_triangle():
        side_1 = int(input("Enter side 1: "))
        side_2 = int(input("Enter side 2: "))
        side_3 = int(input("Enter side 3: "))
        if side_1 == side_2 and side_2 == side_3:
            print('Equilateral triangle')
        else:
            print('Not an equilateral triangle')

    # No 10
    @staticmethod
    def palindrome_number():
        user_input = input("Enter any number: ")
        rev = user_input[::-1]
        if rev == user_input:
            print(user_input, " is a palindrome number")
        else:
            print(user_input, " is not a palindrome number")

    # No11
    @staticmethod
    def extract_integer():
        number = 100
        user_input = input("Enter any number: ")
        rev = user_input[::-1]
        print(rev)


if __name__ == '__main__':
    AssignmentOne.grade()
    AssignmentOne.egg_count()
    AssignmentOne.bacteria()
    AssignmentOne.turing_test()
    AssignmentOne.equilateral_triangle()
    AssignmentOne.palindrome_number()
    AssignmentOne.extract_integer()
