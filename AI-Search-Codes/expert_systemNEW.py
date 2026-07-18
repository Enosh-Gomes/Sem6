def get_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        print("Please answer with yes or no.")

def diagnose():
    print(" Simple Medical Expert System (with confidence)")
    print("---------------------------------------------")

    # Ask symptoms
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

    # Match counts (like confidence score)
    flu_score = sum([fever, cough, sore_throat, body_ache, fatigue])
    covid_score = flu_score + short_breath + loss_smell
    cold_score = sum([cough, sore_throat, runny_nose])
    allergy_score = sum([sneezing, itchy_eyes, runny_nose and not fever])

    # Print scores
    print("\n🧪 Match Confidence (higher is better):")
    print("Flu:", flu_score)
    print("COVID-19:", covid_score)
    print("Common Cold:", cold_score)
    print("Allergy:", allergy_score)

    # Decide based on highest score
    max_score = max(flu_score, covid_score, cold_score, allergy_score)

    if max_score == 0:
        print("\n No matching symptoms. Please consult a doctor.")
    elif max_score == covid_score:
        print("\n🩺 Diagnosis: Most likely COVID-19")
    elif max_score == flu_score:
        print("\n🩺 Diagnosis: Most likely Flu")
    elif max_score == cold_score:
        print("\n🩺 Diagnosis: Most likely Common Cold")
    else:
        print("\n🩺 Diagnosis: Most likely Allergy")

# Run it
diagnose()
