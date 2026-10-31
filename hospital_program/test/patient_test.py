from model.patient import Patient
from data_access.patient_da import *
from business_logic.patient_bl import *

patient1=Patient("Rose","Holand",888,54,"female")
print(patient1)
print("____________________________")

patient1.gender="male"
patient1.name="bob"
print(patient1)
print("____________________________")

print(patient1.age)
print("____________________________")

patient1.age=78
patient1.family="deer"
print(patient1)
print("____________________________")

#The model(Patient) test passed

#_________________________
#Patient Data Access Test passed
patient2=Patient("Hana","Rahmati",890,30,"female")
my_patient_da=PatientDa()

my_patient_da.save_patient(patient1)
my_patient_da.save_patient(patient2)

print (my_patient_da.find_all())
print("____________________________")
print (my_patient_da.find_by_code(890))
print("____________________________")
print(my_patient_da.find_by_name_and_family("b","d"))
print("____________________________")

#__________________________
#Bussiness Logic test
patient_bl=PatientBl()
patient_bl.save_patient(patient1)
patient_bl.save_patient(patient2)