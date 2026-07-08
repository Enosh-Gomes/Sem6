import json
import os

def load_diseases():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "disease_symptoms.json")
    with open(json_path, "r") as file:
        knowledge_base = json.load(file)
    return knowledge_base

def get_discriminating_symptoms(candidates, diseases):
    if not candidates:
        return []
    symptom_scores = {}

    for symptom in set(s for d in candidates for s in diseases[d]):
        have_symptom = sum(1 for d in candidates if symptom in diseases[d])
        dont_have = len(candidates) - have_symptom

        if have_symptom > 0 and dont_have > 0:
            balance = min(have_symptom, dont_have) / len(candidates)
            symptom_scores[symptom] = balance

        elif have_symptom > 0:
            symptom_scores[symptom] = 0.01
        elif dont_have > 0:
            symptom_scores[symptom] = 0.01

    sorted_symptoms = sorted(symptom_scores.items(),key=lambda x: x[1], reverse=True)

    return [s[0] for s in sorted_symptoms]

def get_best_question(asked_questions, knowledge_base, disease_scores):
    candidates = []
    for disease in disease_scores:
        if disease_scores[disease] >= -2:
            candidates.append(disease)

    discriminating_symptoms = get_discriminating_symptoms(candidates, knowledge_base)

    for symptom in discriminating_symptoms:
        if symptom not in asked_questions:
            return symptom
    return None

def dynamic_diagnosis():
    knowledge_base = load_diseases()
    disease_scores = {}
    for disease in knowledge_base:
        disease_scores[disease] = 0

    asked_questions = set()
    max_questions = 10
    question_count = 0
    print("\nAnswer the following questions:\n")

    while question_count < max_questions:
        question = get_best_question(asked_questions, knowledge_base, disease_scores)
        if question is None:
            break
        asked_questions.add(question)
        answer = input(f"Do you have {question}? (yes/no): ").strip().lower()

        while answer not in ['yes', 'no', 'y', 'n']:
            answer = input("Please enter yes/no: ").strip().lower()
        question_count += 1

        if answer in ['yes', 'y']:
            for disease in knowledge_base:
                if question in knowledge_base[disease]:
                    disease_scores[disease] += 2
                else:
                    disease_scores[disease] -= 1
        else:
            for disease in knowledge_base:
                if question in knowledge_base[disease]:
                    disease_scores[disease] -= 2
                else:
                    disease_scores[disease] += 1

    print("\n===== FINAL DIAGNOSIS =====\n")
    best_disease = max(disease_scores, key=disease_scores.get)
    highest_score = disease_scores[best_disease]
    if highest_score <= 0:
        print("No disease strongly matches the symptoms.")
    else:
        print(f"You are having {best_disease}")

if __name__ == "__main__":
    print("=== Expert System for Disease Diagnosis ===")
    dynamic_diagnosis()