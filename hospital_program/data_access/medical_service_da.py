from model.medical_service import MedicalService
from model.doctor import Doctor
from datetime import datetime

class MedicalServiceDa:
    def __init__(self):
        self.medical_service_list=[]

    def save_medical_service(self,medical_service):
        self.medical_service_list.append(medical_service)

    def update(self,medical_service):
        raise NotImplementedError("Update Not Implemented")

    def delete_by_date(self,the_date):
        raise NotImplementedError("Delete Not Implemented")

    def find_by_date(self,the_date):
        for medical_service in self.medical_service_list:
            if medical_service.the_date==the_date:
                return medical_service

    def find_all(self):
        return self.medical_service_list
    
    def find_by_doctor_and_time(self,doctor:Doctor, the_date:datetime):
        for service in self.medical_service_list:
            service: MedicalService
            if service.doctor.medical_council_number==doctor.medical_council_number and service.the_date==the_date:
               return service
        return None
