knowledge_base = {
    'malaria': ['fever', 'chest pain', 'vomiting', 'fatigue', 'sweating', 'headache'],
    'dengue': ['fever', 'pain behind the eyes', 'headache', 'joint pain', 'rash'],
    'typhoid': ['fever', 'abdominal pain', 'diarrhea', 'constipation'],
    'flu': ['fever', 'cough', 'sore throat', 'body aches'],
    'yellow fever': ['fever', 'nausea', 'jaundice', 'muscle pain', 'loss of appetite']
}

def inference_engine(user_symptoms):
    probability = {}
    for disease in knowledge_base.keys():
        count = 0
        for symptom in knowledge_base[disease]:
            if symptom in user_symptoms:
                count += 1
        probability[disease] = count / len(knowledge_base[disease])
    
    max_probability = max(probability.values())
    most_probable_diseases = [disease for disease, prob in probability.items() if prob == max_probability]
    
    if max_probability == 1:
        print("\nBased on the symptoms you provided, you are most likely suffering from " + ", ".join(most_probable_diseases))
    elif max_probability > 0:
        print("\nBased on the symptoms you provided, you may be suffering from " + ", ".join(most_probable_diseases) + " with a probability of " + str(max_probability * 100) + "%")
    else:
        print("\nBased on the symptoms you provided, it is unlikely that you are suffering from any of the diseases in our knowledge base.")

def ask_symptoms():
    user_symptoms = []
    questions = []
    
    for disease in knowledge_base.keys():
        questions += knowledge_base[disease]
    
    questions = list(set(questions))
    print("\nAnswer the following questions:")
    
    for question in questions:
        answer = input("Do you have " + question + "? (yes/no): ").strip().lower()
        if answer == 'yes':
            user_symptoms.append(question)
    return user_symptoms

def decision():
    max_questions = 2
    questions_asked = 0
    user_symptoms = []
    
    while questions_asked < max_questions:
        user_symptoms = ask_symptoms()
        questions_asked += 1
        
        if user_symptoms:
            inference_engine(user_symptoms)
            return
    
    if questions_asked >= max_questions:
        print("Maximum number of questions reached. Unable to make a decision based on the given information.")

if __name__ == "__main__":
    print("Welcome to the Expert System for Disease Diagnosis!")
    decision()