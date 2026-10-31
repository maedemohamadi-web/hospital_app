from model.medical_service import MedicalService
from model.patient import Patient
from tools.validation import *

class Visit:
    def __init__(self,the_patient:Patient,the_medical_service:MedicalService):
        self.patient=the_patient
        self.medical_service=the_medical_service

    @property
    def the_patient(self):
        return self.__the_patient

    @the_patient.setter
    def the_patient(self,value):
        the_patient_validator(value)
        self.__the_patient=value

    @property
    def the_medical_service(self):
        return self.__the_medical_service

    @the_medical_service.setter
    def the_medical_service(self,value):
        the_medical_service_validator(value)
        self.__the_medical_service=value

    def __repr__(self):
        return f"Visit({self.__dict__})"