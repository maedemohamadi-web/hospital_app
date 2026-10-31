from data_access.medical_service_da import MedicalServiceDa
from model.doctor import Doctor
from model.medical_service import MedicalService
from business_logic.doctor_bl import DoctorBl

class MedicalServiceBl:
    def __init__(self):
        self.da=MedicalServiceDa()
        self.doctor_bl=DoctorBl()

    def save_medical_service(self,medical_service):
        doctorr=medical_service.doctor
        exist=self.doctor_bl.find_by_medical_council_number(doctorr.medical_council_number)
        if exist:
            if exist.the_name!=doctorr.the_name or exist.the_family!=doctorr.the_family:
                raise ValueError("This Medical Council Number Already Exists!")
            medical_service.doctor=exist
        else:
            self.doctor_bl.save_doctor(doctorr)

        if self.da.find_by_doctor_and_time(medical_service.doctor,medical_service.the_date):
            raise ValueError("Doctor is busy in this date and time!")
        self.da.save_medical_service(medical_service)

    def update(self,medical_service):
        self.da.update(medical_service)

    def delete_by_date(self,the_date):
        self.da.delete_by_date(the_date)

    def find_by_date(self,the_date):
        return self.da.find_by_date(the_date)

    def find_all(self):
        return self.da.find_all()
    
    def find_by_doctor_and_time(self,doctor:Doctor,the_date):
       return self.da.find_by_doctor_and_time (doctor,the_date)
       
        