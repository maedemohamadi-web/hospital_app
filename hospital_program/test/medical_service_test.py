from model.medical_service import MedicalService
from datetime import datetime
from model.doctor import Doctor
from data_access.medical_service_da import MedicalServiceDa
from business_logic.medical_service_bl import MedicalServiceBl

first_doctor=Doctor("saba","hami","Neurology","190999")
the_service_date=datetime(2027,7,6,16,30,0)
my_medical_service=MedicalService(first_doctor,the_service_date,"Surgery",50000000)
#print(my_medical_service)
my_medical_service.doctor=Doctor("Sara","Jamshidi","Cardiology","180999")
#print(my_medical_service)

my_medical_service.service_type="CT"
my_medical_service.the_date=datetime(2026,12,9,8)
my_medical_service.price=100000000
print(my_medical_service)
print("_____________________")

second_doctor=Doctor("Sohrab","Majidi","Emergency Medicine","678900")
the_med_service_date=datetime(2026,12,2,15,30)
my_second_medical_service=MedicalService(second_doctor,the_med_service_date,"Emergency Care",10000000)
print (my_second_medical_service)
print("_____________________")

#The model(Medical Service) test passed
#_______________________________________

medical_service_da_1=MedicalServiceDa()
medical_service_da_1.save_medical_service(my_medical_service)
medical_service_da_1.save_medical_service(my_second_medical_service)
print(medical_service_da_1.find_all())
print("_____________________")
print(medical_service_da_1.find_by_date(datetime(2026,12,2,15,30)))
print("_____________________")

#Medical Service Data Access Test passed 
#________________________________________

medical_service_bl_1=MedicalServiceBl()


third_doctor=Doctor("gita","saremi","Neurology","123456")
third_date=datetime(2027,1,1,9)
third_medical_service=MedicalService(third_doctor,third_date,"MRI",200000)

fourth_doctor=Doctor("gita","saremi","Neurology","123456")
fourth_date=datetime(2027,1,1,11)
fourth_medical_service=MedicalService(fourth_doctor,fourth_date,"Surgery",20000000)

medical_service_bl_1.save_medical_service(third_medical_service)
medical_service_bl_1.save_medical_service(fourth_medical_service)
#medical_service_bl_1.delete_by_date(datetime(2027,1,1,10))
print(medical_service_bl_1.find_by_date(datetime(2027,1,1,9)))
print("_____________________")
print(medical_service_bl_1.find_by_date(datetime(2027,1,1,11)))
print("_____________________")
print(medical_service_bl_1.find_all())

fifth_doctor=Doctor("abas","azimi","Oncology","600923")
fifth_date=datetime(2027,1,1,11)
fifth_medical_service=MedicalService(fifth_doctor,fifth_date,"Laboratory Test",1000000)
medical_service_bl_1.save_medical_service(fifth_medical_service)

#Medical Service Business Logic Test Passed
#___________________________________________