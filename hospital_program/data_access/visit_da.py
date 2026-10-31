from model.visit import Visit
from model.patient import *

class VisitDa:
    def __init__(self):
        self.visit_list=[]

    def save_visit(self,visit):
        self.visit_list.append(visit)

    def update(self,visit):
        raise NotImplementedError("Update Not Implemented")

    def delete_by_patient(self,patient):
        raise NotImplementedError("Delete Not Implemented")

    def find_by_patient(self,patient):
        visits=[]
        for visit in self.visit_list:
            if visit.patient==patient:
                visits.append(visit)
        return visits


    def find_all(self):
        return self.visit_list
        
    def find_by_patient_code_and_med_serve_time(self,code,the_date):
        visit:Visit
        patient:Patient
        for visit in self.visit_list:
            if visit.patient.code==code and visit.medical_service.the_date==the_date:
                return visit
        return None
        