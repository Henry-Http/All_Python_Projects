class TesterClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def set_name(name):
        return name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
