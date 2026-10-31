from model.patient import Patient

class PatientDa:
    def __init__(self):
        self.patient_list=[]
    
    def save_patient(self,patient):
        self.patient_list.append(patient)

    def update(self,patient):
        raise NotImplementedError("Update Not Implemented")

    def delete_by_code(self,code):
        raise NotImplementedError("Delete Not Implemented")

    def find_by_code(self,code):
        for patient in self.patient_list:
            if patient.code==code:
                return patient

    def find_by_name_and_family(self,name,family):
        patient_list=[]
        for patient in self.patient_list:
            if patient.name.startswith(name)and patient.family.startswith(family):
                patient_list.append(patient)
        return patient_list

    def find_all(self):
        return self.patient_list
        