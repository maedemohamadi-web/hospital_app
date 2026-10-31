from tools.validation import *

class Doctor:
    def __init__(self,the_name,the_family,specialization,medical_council_number):
        self.the_name=the_name
        self.the_family=the_family
        self.specialization=specialization
        self.medical_council_number=medical_council_number

    @property
    def the_name(self):
        return self.__the_name

    @the_name.setter
    def the_name(self,value):
        the_name_validator(value)
        self.__the_name=value

    @property
    def the_family(self):
        return self.__the_family

    @the_family.setter
    def the_family(self,value):
        the_family_validator(value)
        self.__the_family=value

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self,value):
        specialization_validator(value)
        self.__specialization=value

    @property
    def medical_council_number(self):
        return self.__medical_council_number

    @medical_council_number.setter
    def medical_council_number(self,value):
        medical_council_number_validator(value)
        self.__medical_council_number=value


    def __repr__(self):
        return f"Doctor({self.__dict__})"
