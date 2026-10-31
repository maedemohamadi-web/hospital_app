from data_access.patient_da import PatientDa

class PatientBl:
    def __init__(self):
        self.da=PatientDa()

    def save_patient(self,patient):
        if self.da.find_by_code(patient.code):
            raise ValueError("Patient Code Already Taken")
        self.da.save_patient(patient)

    def update(self,patient):
        self.da.update(patient)

    def delete_by_code(self,code):
        self.da.delete_by_code(code)

    def find_by_code(self,code):
        return self.da.find_by_code(code)

    def find_by_name_and_family(self,name,family):
        return self.da.find_by_name_and_family(name,family)

    def find_all(self):
        return self.da.find_all()
        