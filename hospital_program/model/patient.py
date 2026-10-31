from tools.validation import *

class Patient:
    def __init__(self,name,family,code,age,gender):
        self.name=name
        self.family=family
        self.__code=code
        self.age=age
        self.gender=gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        name_validator(value)
        self.__name=value

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self,value):
        family_validator(value)
        self.__family=value

    @property
    def code(self):
        return self.__code

    #@code.setter
    #def code(self,value):
    #    code_validator(value)
     #   self.__code=value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        age_validator(value)
        self.__age=value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self,value):
        gender_validator(value)
        self.__gender=value

    def __repr__(self):
        return f"Patient({self.__dict__})"
