Example of inheritance for OOP in python

This code defines two classes: ParentClass and ChildClass. ChildClass is a subclass of ParentClass and inherits its methods and attributes. Let's break down the code and explain its functionality:

    ParentClass:
        It has a static method get_first_name that takes a fullname string and returns the first name by splitting the string at the space character.
        It has an instance method hey that takes a fullname string as an argument and prints a greeting message with the first name obtained from get_first_name.

    ChildClass:
        It inherits from ParentClass and extends its functionality.
        It has an initializer (__init__) that takes an age argument and assigns it to the age attribute of the instance.
        It overrides the hey method inherited from ParentClass.
            If age is provided and less than 18, it prints a customized greeting.
            If age is provided and greater than 18, it calls the hey method of the parent class using the super() function.
            If age is not provided (None), it also calls the hey method of the parent class using super().

    In the main block:
        An instance of ParentClass is created and assigned to a.
        An instance of ChildClass is created with an age of 22 and assigned to b.
        Another instance of ChildClass is created with an age of 14 and assigned to c.
        The hey method is called on each instance with a fullname argument to print the appropriate greeting message based on the age.

Overall, this code demonstrates inheritance and method overriding in Python. The ChildClass overrides the hey method from the parent class and adds additional behavior based on the age attribute.