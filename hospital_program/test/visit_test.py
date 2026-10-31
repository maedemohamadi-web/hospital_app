from model.visit import Visit
from datetime import datetime
from model.patient import Patient
from model.medical_service import MedicalService
from model.doctor import Doctor
from data_access.visit_da import VisitDa
from business_logic.patient_bl import PatientBl
from business_logic.medical_service_bl import MedicalServiceBl
from business_logic.visit_bl import VisitBl

first_patient=Patient("Rose","Holand",888,4,"female")
first_doctor=Doctor("soha","miri","Pediatrics","760932")
service_date=datetime(2027,2,22,19)
first_medical_service=MedicalService(first_doctor,service_date,"Vaccination",100000)
visit1=Visit(first_patient,first_medical_service)
print(visit1)
print("_________________________")

#The model(Visit) test passed
#______________________________________
patient_business_logic=PatientBl()
medical_serve_bl=MedicalServiceBl()

patient_business_logic.save_patient(first_patient)

second_patient=Patient("Nil","sea",878,22,"female")

patient_business_logic.save_patient(second_patient)

medical_serve_bl.save_medical_service(first_medical_service)

medical_service_2=MedicalService(first_doctor,service_date,"X-Ray",300000)

#medical_serve_bl.save_medical_service(medical_service_2)

visit_da_1=VisitDa()
visit_da_1.save_visit(visit1)
print(visit_da_1.find_by_patient(first_patient))
print("_________________________")

visit2=Visit(second_patient,first_medical_service)
visit_da_1.save_visit(visit2)
print(visit_da_1.find_all())
print("_________________________")
print(visit_da_1.find_by_patient(second_patient))
print("_________________________")

#Visit Data Access Test passed
#______________________________________________

visit_business_logic=VisitBl()
visit_business_logic.save_visit(visit1)

my_date=datetime(2026,12,22,11)
my_med_ser=MedicalService(first_doctor,my_date,"CT",900000)
visit3=Visit(first_patient,my_med_ser)

visit_business_logic.save_visit(visit3)
visit_business_logic.save_visit(visit2)
print(visit_business_logic.find_all())

#Visit Business Logic Test Passed
#______________________________________________
