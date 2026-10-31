from model.doctor import Doctor
from data_access.doctor_da import DoctorDa
from business_logic.doctor_bl import DoctorBl

doctor1=Doctor("saba","hami","Neurology","190999")
print (doctor1)
print("_________________________________________________")

doctor1.medical_council_number="56678"
print(doctor1.specialization)
print("_________________________________________________")
doctor1.the_family="moheb ahari"
doctor1.the_name="Sara"
print(doctor1)
print("_________________________________________________")

doctor2=Doctor("shima","ahmadi","Physical Medicine","120999")

#The model(Doctor) test passed
#_______________________________________________________

doctor_da_1=DoctorDa()
doctor_da_1.save_doctor(doctor1)
doctor_da_1.save_doctor(doctor2)
print(doctor_da_1.find_all())
print("_________________________________________________")
print(doctor_da_1.find_by_medical_council_number("56678"))
print("_________________________________________________")
print(doctor_da_1.find_by_medical_council_number("120999"))

#Doctor Data Access Test Passed
#_______________________________________________________

doctor_bl_1=DoctorBl()
doctor_bl_1.save_doctor(doctor1)
doctor_bl_1.save_doctor(doctor2)
print(doctor_bl_1.find_all())

#Doctor Business Logic Test Passed
