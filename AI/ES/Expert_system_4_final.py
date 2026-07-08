import json
import os

def load_diseases():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "disease_symptoms.json")

    with open(json_path, "r") as file:
        knowledge_base = json.load(file)
    return knowledge_base

def get_best_question(asked_questions, candidate_diseases, knowledge_base):
    symptom_frequency = {}
    # Count symptoms only among candidate diseases
    for disease in candidate_diseases:
        for symptom in knowledge_base[disease]:
            if symptom not in asked_questions:
                if symptom not in symptom_frequency:
                    symptom_frequency[symptom] = 0
                symptom_frequency[symptom] += 1

    if not symptom_frequency:
        return None
    # Best symptom = closest to half split
    total = len(candidate_diseases)
    best_symptom = None
    best_difference = total

    for symptom, frequency in symptom_frequency.items():
        difference = abs((total / 2) - frequency)
        if difference < best_difference:
            best_difference = difference
            best_symptom = symptom
    return best_symptom

def dynamic_diagnosis(knowledge_base=None):
    if knowledge_base is None:
        knowledge_base = load_diseases()
    disease_scores = {}
    matched_symptoms = {}

    # Initialize disease scores
    for disease in knowledge_base:
        disease_scores[disease] = 0
        matched_symptoms[disease] = []

    # Initially all diseases are candidates
    candidate_diseases = list(knowledge_base.keys())

    asked_questions = set()
    max_questions = 10
    question_count = 0
    print("\nAnswer the following questions:\n")

    while (question_count < max_questions and len(candidate_diseases) > 1):
        question = get_best_question(asked_questions, candidate_diseases, knowledge_base)
        if question is None:
            break
        asked_questions.add(question)
        answer = input(f"Do you have {question}? (yes/no): ").strip().lower()

        while answer not in ['yes', 'no', 'y', 'n']:
            answer = input("Please enter yes/no: ").strip().lower()
        question_count += 1

        if answer in ['yes', 'y']:
            new_candidates = []
            for disease in candidate_diseases:
                if question in knowledge_base[disease]:
                    disease_scores[disease] += 2
                    matched_symptoms[disease].append(question)
                    new_candidates.append(disease)
                else:
                    disease_scores[disease] -= 1
            # Keep matching diseases
            if new_candidates:
                candidate_diseases = new_candidates
        else:
            new_candidates = []
            for disease in candidate_diseases:
                if question in knowledge_base[disease]:
                    disease_scores[disease] -= 2
                else:
                    disease_scores[disease] += 1
                    new_candidates.append(disease)
            # Keep diseases without symptom
            if new_candidates:
                candidate_diseases = new_candidates

        print("\nPossible Diseases:")
        for disease in candidate_diseases:
            print("-", disease)

        # EARLY STOPPING
        best_disease = max(disease_scores, key=disease_scores.get)
        best_score = disease_scores[best_disease]
        second_best = sorted(disease_scores.values(), reverse=True)[1]

        # If confidence gap large enough
        if best_score - second_best >= 6:
            print("\nDiagnosis confidence is high.")
            break

    print("\n===== FINAL DIAGNOSIS =====\n")
    sorted_scores = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)
    best_disease, highest_score = sorted_scores[0]

    if highest_score <= 0:
        print( "No disease strongly matches the symptoms.")
    else:
        print( f"Most probable disease: {best_disease}")
        print( f"Confidence Score: {highest_score}")
        print("\nMatched Symptoms:")
        for symptom in matched_symptoms[best_disease]:
            print("-", symptom)
        print("\nTop Possible Diseases:")
        for disease, score in sorted_scores[:3]:
            print(f"{disease} -> Score: {score}")

if __name__ == "__main__":
    print("=== Expert System for Disease Diagnosis ===")
    dynamic_diagnosis()