from data_access.doctor_da import DoctorDa

class DoctorBl:
    def __init__(self):
        self.da=DoctorDa()

    def save_doctor(self,doctor):
        if self.da.find_by_medical_council_number(doctor.medical_council_number):
            raise ValueError("Medical Council Number is unique and this Medical Council No is already taken!")
        self.da.save_doctor(doctor)

    def update(self,doctor):
        self.da.update(doctor)

    def delete_by_medical_number(self,medical_council_number):
        self.da.delete_by_medical_number(medical_council_number)
        
    def find_by_medical_council_number(self,medical_council_number):
        return self.da.find_by_medical_council_number(medical_council_number)

    def find_all(self):
        return self.da.find_all()
        
