def ask_symptom(symptom):
    while True:
        response = input(f"Do you have {symptom}? (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return response == "yes"
        print("Please answer 'yes' or 'no'.")

def diagnose_disease():
    print("Welcome to the Medical Diagnosis Expert System")
    print("Please answer the following questions about your symptoms.\n")

    if ask_symptom("fever"):
        if ask_symptom("cough"):
            if ask_symptom("body aches"):
                if ask_symptom("fatigue"):
                    return "Influenza (Flu)", "A viral infection. Rest, fluids, and sometimes antiviral meds are needed."
                else:
                    return "Mild Viral Infection", "Rest and fluids are recommended."
            elif ask_symptom("sore throat"):
                return "Strep Throat", "A bacterial infection. Consult a doctor for antibiotics."
            else:
                return "Bronchitis", "Inflammation of airways. Rest and fluids help recovery."
        elif ask_symptom("headache"):
            if ask_symptom("nausea"):
                return "Migraine with Fever", "Rest in a dark, quiet room and consult a doctor."
            else:
                return "Sinus Infection", "Inflammation of sinuses. May need antibiotics."
        elif ask_symptom("abdominal pain"):
            if ask_symptom("diarrhea"):
                return "Stomach Flu (Gastroenteritis)", "An intestinal infection. Stay hydrated and rest."
            else:
                return "Appendicitis", "Inflammation of the appendix. Seek immediate medical attention."
        else:
            return "Low-grade Fever", "Monitor temperature and rest. Consult doctor if it persists."

    else:
        if ask_symptom("sore throat"):
            if ask_symptom("runny nose"):
                if ask_symptom("cough"):
                    return "Common Cold", "A viral infection. Rest and hydration are usually enough."
                else:
                    return "Seasonal Allergies", "Try over-the-counter antihistamines."
            else:
                return "Throat Irritation", "Could be due to dryness or irritants. Stay hydrated."
        elif ask_symptom("nausea"):
            if ask_symptom("vomiting"):
                return "Food Poisoning", "Usually caused by contaminated food. Stay hydrated."
            else:
                return "Indigestion", "Try antacids and avoid spicy or fatty foods."
        elif ask_symptom("headache"):
            return "Tension Headache", "Often caused by stress. Rest and over-the-counter pain relievers may help."
        else:
            return "Unknown", "No clear diagnosis based on symptoms. Monitor and consult a doctor if concerned."
def main():
    disease, description = diagnose_disease()
    print(f"\n Diagnosis : {disease}")
    print(f"Description : {description}")

if __name__=="__main__":
   main()

