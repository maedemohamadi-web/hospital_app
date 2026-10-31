from model.doctor import Doctor

class DoctorDa:
    def __init__(self):
        self.doctor_list=[]

    def save_doctor(self,doctor):
        self.doctor_list.append(doctor)

    def update(self,doctor):
        raise NotImplementedError("Update Not Implemented")

    def delete_by_medical_number(self,medical_council_number):
        raise NotImplementedError("Delete Not Implemented")

    def find_by_medical_council_number(self,medical_council_number):
        for doctor in self.doctor_list:
            if doctor.medical_council_number==medical_council_number:
                return doctor

    def find_all(self):
        return self.doctor_list
        