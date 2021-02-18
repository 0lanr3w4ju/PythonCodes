import Animal


class Cat(Animal):

    def __init__(self, name="defaultValue", age=0):
        self.name = name
        self.age = age
        self.type = "cat"

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def do_cat(self):
        return "{0} purrs".format(self.type)
