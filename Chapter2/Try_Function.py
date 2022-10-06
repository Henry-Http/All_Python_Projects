from Chapter2.First_Class import TesterClass


# def tester(age, name):
#     age = 38
#     name = "Johnson"


if __name__ == '__main__':

    new_tester = TesterClass("john", 87)
    new_tester.set_name("holly")
    new_tester.set_age(5)
    print(new_tester.get_name())
    print(new_tester.get_age())

    # print(tester(45, "Olof"))

