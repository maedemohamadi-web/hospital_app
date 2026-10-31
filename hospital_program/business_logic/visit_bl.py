from model.visit import Visit
from data_access.visit_da import VisitDa
from business_logic.patient_bl import PatientBl
from business_logic.medical_service_bl import MedicalServiceBl

class VisitBl:
    def __init__(self):
        self.da=VisitDa()
        self.patient_bl=PatientBl()
        self.medical_service_bl=MedicalServiceBl()

    def save_visit(self,visit):
        patient_code=visit.patient.code
        serve_time=visit.medical_service.the_date
        if self.da.find_by_patient_code_and_med_serve_time(patient_code,serve_time):
            raise ValueError("This patient has another appoinment in this date and time")
        self.da.save_visit(visit)

    def update(self,visit):
        self.da.update(visit)
        

    def delete_by_patient(self,patient):
        self.da.delete_by_patient(patient)

    def find_by_patient(self,patient):
        return self.da.find_by_patient(patient)


    def find_all(self):
        return self.da.find_all()
        