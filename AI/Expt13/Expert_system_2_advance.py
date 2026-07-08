import json

def load_knowledge_base():
    with open("knowledge_base.json", "r") as file:
        data = json.load(file)
    # Access emergency symptoms
    emergency_symptoms = data["emergency_symptoms"]
    # Access diseases
    knowledge_base = data["diseases"]
    return knowledge_base, emergency_symptoms

def get_best_question(asked_questions, knowledge_base):
    symptom_score = {}
    for disease in knowledge_base:
        symptoms = knowledge_base[disease]['symptoms']
        for symptom, weight in symptoms.items():
            if symptom not in asked_questions:
                if symptom not in symptom_score:
                    symptom_score[symptom] = 0
                symptom_score[symptom] += weight

    best_question = max(
        symptom_score,
        key=symptom_score.get
    )

    return best_question

def dynamic_diagnosis():
    disease_scores = {}
    matched_symptoms = {}
    asked_questions = set()
    knowledge_base, emergency_symptoms = load_knowledge_base()

    # Initialize scores
    for disease in knowledge_base:
        disease_scores[disease] = 0
        matched_symptoms[disease] = []
    max_questions = 15
    question_count = 0

    print("\n===== HEALTH EXPERT SYSTEM =====\n")

    while question_count < max_questions:
        question = get_best_question(asked_questions, knowledge_base)
        asked_questions.add(question)
        answer = input(f"Do you have {question}? (yes/no): ").strip().lower()

        while answer not in ['yes', 'no', 'y', 'n']:
            answer = input("Enter yes/no only: ").strip().lower()

        severity = 1

        # Ask severity only for YES
        if answer in ['yes', 'y']:
            severity = int(input("Severity (1-5): ").strip())

            # Emergency warning
            if question in emergency_symptoms:
                print("\n⚠ WARNING: Serious symptom detected.")

                print("Please consult a doctor immediately.\n")

        if answer in ['yes', 'y']:
            for disease in knowledge_base:
                symptoms = knowledge_base[disease]['symptoms']
                if question in symptoms:
                    weight = symptoms[question]
                    disease_scores[disease] += (weight * severity)
                    matched_symptoms[disease].append(question)
                else:
                    disease_scores[disease] -= 1

        # =================================================
        # NO RESPONSE
        # =================================================

        else:
            for disease in knowledge_base:
                symptoms = knowledge_base[disease]['symptoms']
                if question in symptoms:
                    weight = symptoms[question]
                    disease_scores[disease] -= weight
                else:
                    disease_scores[disease] += 0.5

        question_count += 1

        print("\nCurrent Ranking:\n")
        sorted_scores = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)

        for disease, score in sorted_scores:
            print(disease, "->", round(score, 2))
        print()

    for disease in knowledge_base:
        required = knowledge_base[disease]['required']
        for symptom in required:
            if symptom not in matched_symptoms[disease]:
                disease_scores[disease] -= 10

    print("\nFINAL DIAGNOSIS\n")

    sorted_scores = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)

    max_possible = max_questions * 6
    for disease, score in sorted_scores[:3]:

        if score > 0:
            probability = (score / max_possible) * 100
            print(disease.upper())
            print("Probability:", round(probability, 2), "%")
            print("Matched Symptoms:")

            for symptom in matched_symptoms[disease]:
                print("-", symptom)
            if knowledge_base[disease]['emergency']:
                print("⚠ Medical Attention Recommended")
            print()

if __name__ == "__main__":
    dynamic_diagnosis()