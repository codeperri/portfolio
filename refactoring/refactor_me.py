"""
    Classes should be named camelcase and according to the name of the file
    methods should be lowercase and format with underscore instead of spaces
    There should be a __init__ method
    And consider at least PEP8 linter for the structure of the code
    Consider decorators for static methods
"""


class ParentClass:

    @staticmethod
    def get_first_name(fullname):
        return fullname.split(" ")[0]

    def hey(self, fullname):
        print("Hello " + self.get_first_name(fullname))


class ChildClass(ParentClass):

    def __init__(self, age):
        self.age = age

    def hey(self, fullname):
        if self.age and self.age < 18:
            print("What's up " + self.get_first_name(fullname) + "?")

        elif self.age and self.age > 18:
            super().hey(fullname)

        elif not self.age:
            super().hey(fullname)


if __name__ == "__main__":
    a = ParentClass()
    # Missed the age argument for the child
    b = ChildClass(22)

    c = ChildClass(14)

    a.hey("Alfredo Topete Escamilla")

    b.hey("Alfredo Topete Escamilla")

    c.hey("Alfredo Topete Escamilla")
