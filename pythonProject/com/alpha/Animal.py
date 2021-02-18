class Animal:

    def __init__(self, type_of_animal="defaultValue", name="defaultValue", age=0):
        self.type = type_of_animal
        self.name = name
        self.age = age

    def get_type(self):
        return self.type

    def set_type(self, type_of_animal):
        self.type = type_of_animal

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
