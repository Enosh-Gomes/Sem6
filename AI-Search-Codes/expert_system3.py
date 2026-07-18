def get_yes_no(question):
    answer=input(question+"yes/no:").strip().lower()
    if answer in ['yes','no']:
        return answer=='yes'
    print("please enter yes/no")
    
def diagnose():
    print("Medical Expert System ")
    print("-------------------------")
    
    fever = get_yes_no("Do you have a fever?")
    cough = get_yes_no("Do you have a cough?")
    sore_throat = get_yes_no("Do you have a sore throat?")
    runny_nose = get_yes_no("Do you have a runny nose?")
    body_ache = get_yes_no("Do you have body aches?")
    fatigue = get_yes_no("Are you feeling fatigued?")
    short_breath = get_yes_no("Are you experiencing shortness of breath?")
    loss_smell = get_yes_no("Have you lost your sense of taste or smell?")
    sneezing = get_yes_no("Are you sneezing frequently?")
    itchy_eyes = get_yes_no("Do you have itchy or watery eyes?")
    
    if fever and cough and sore_throat and body_ache and fatigue:
        if short_breath and loss_smell:
             print("\n Diagnosis: You may have COVID-19.")
        else:
            print("\n Diagnosis: You may have the Flu.")
    elif cough and runny_nose and sore_throat:
        print("\n Diagnosis: You may have the Common Cold.")
        
    elif sneezing and itchy_eyes and runny_nose and not fever:
         print("\n Diagnosis: You may have Allergy.")
        
    else:
        print("\n Diagnosis: Symptoms do not match a known condition.")
        print("Please consult a healthcare professional.")
        
        
    flu_score=sum([fever,cough,sore_throat,body_ache,fatigue])
    covid_score=flu_score+loss_smell+short_breath
    cold_score=sum([cough,runny_nose,sore_throat])
    allergy_score=sum([sneezing,itchy_eyes,runny_nose and not fever])
    
    max_score=max(flu_score,covid_score,cold_score,allergy_score)
    
    # Print scores
    print("\n🧪 Match Confidence (higher is better):")
    print("Flu:", flu_score)
    print("COVID-19:", covid_score)
    print("Common Cold:", cold_score)
    print("Allergy:", allergy_score)
    
    if max_score==0:
        print("\n Diagnosis: Symptoms do not match a known condition.")
        print("Please consult a healthcare professional.")
    elif max_score == covid_score:
        print("\n🩺 Diagnosis: Most likely COVID-19")
    elif max_score == flu_score:
        print("\n🩺 Diagnosis: Most likely Flu")
    elif max_score == cold_score:
        print("\n🩺 Diagnosis: Most likely Common Cold")
    else:
        print("\n🩺 Diagnosis: Most likely Allergy")
        
diagnose()
        
    