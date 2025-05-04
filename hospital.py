def hospital_expeert_system():
    
    print("Welcome to medical expert system.")
    print("Answer the following queations answer with yes or no.")
    
    fever=input("Do you have a fever?: ").lower()
    cough=input("Do you have a cough? : ").lower()
    breath=input("Do you have experience diffficulty in breathing : ").lower()
    chest_pain=input("Do you have chest_pain? : ").lower()
    headache=input("Do you have frequent headaches? : ").lower()
    stomach_pain=input("Do you have stomch-pain? : ").lower()
    
    if fever=="yes" and breath == "yes" and cough=="yes":
        print("Possible Condition:Covid-19 or Respiratory issue")
        print("Recommended Doctor: Pulmonologist")
        print("Hospital Addmission:Recommended\n")
        print("Thank you for using the Medical Expert System!")
    
    elif chest_pain=="yes" and breath == "yes" :
        print("Possible Condition: Heart realated issue")
        print("Recommended Doctor: Cardiologist")
        print("Hospital Addmission: Immediate attention ad=vised\n")
        print("Thank you for using the Medical Expert System!")
    
    elif stomach_pain=="yes":
        print("Possible Condition: Gastric or Digestive issue")
        print("Recommended Doctor: Gastoenterlogist")
        print("Hospital Addmission: visit clinic for check-up\n")
        print("Thank you for using the Medical Expert System!")
        
    elif headache=="yes" and fever== "yes":
        print("Possible Condition:Migraine or neurological issue ")
        print("Recommended Doctor: Neurogogist")
        print("Hospital Addmission:  Not required uless frequent\n")
        print("Thank you for using the Medical Expert System!")
        
    else:
        print("Condition is not match to the known rules")
        print("Recommended Action: General Physician consultation.\n")
        
        print("Thank you for using the Medical Expert System!")
 
hospital_expeert_system()       
