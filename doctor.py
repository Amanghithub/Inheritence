class doctor():
    def __init__(self):
        print("This is a doctor's class")
        
    def bmi(weight,height):
        bmi_var = weight/(height*height)
        print("Your BMI is: "+str(bmi_var))
        
    def heart(heart_rate):
        if (heart_rate>60 and heart_rate<100):
            print("Great! your heart rate is normal")
        else:
            print("Your heart rate does not seem normal. Visit a doctor")
            
class patient(doctor):
    def __init__(self,name,weight,height,heart_rate):
        self.name = name
        self.weight = weight
        self.height = height
        self.heart_rate = heart_rate
        
    def health_check(self):
        print("Patient name is: "+self.name)
        doctor.bmi(self.weight, self.height)
        doctor.heart(self.heart_rate)
        print("\n")
    
    
patient1 = patient("Rahul", 30, 0.91, 80)
patient1.health_check()

patient2 = patient("Nitin", 40, 1, 120)
patient2.health_check()