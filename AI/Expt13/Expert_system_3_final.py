import json
import os

def load_diseases():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "disease_symptoms.json")
    with open(json_path, "r") as file:
        knowledge_base = json.load(file)
    return knowledge_base

def get_best_question(possible_diseases, asked_questions, knowledge_base):
    symptom_frequency = {}

    for disease in possible_diseases:
        for symptom in knowledge_base[disease]:
            if symptom not in asked_questions:
                if symptom not in symptom_frequency:
                    symptom_frequency[symptom] = 0
                symptom_frequency[symptom] += 1

    if not symptom_frequency:
        return None
    best_symptom = max(symptom_frequency, key=symptom_frequency.get)
    return best_symptom

def dynamic_diagnosis():
    knowledge_base = load_diseases()
    disease_scores = {}

    for disease in knowledge_base:
        disease_scores[disease] = 0

    possible_diseases = list(knowledge_base.keys())
    asked_questions = set()
    max_questions = 10
    question_count = 0
    print("\nAnswer the following questions:\n")

    while question_count < max_questions and len(possible_diseases) > 1:
        question = get_best_question(possible_diseases, asked_questions, knowledge_base)
        if question is None:
            break
        asked_questions.add(question)
        answer = input(f"Do you have {question}? (yes/no): ").strip().lower()

        while answer not in ['yes', 'no', 'y', 'n']:
            answer = input("Please enter yes/no: ").strip().lower()

        question_count += 1

        # Update scores dynamically
        for disease in possible_diseases:
            if answer in ['yes', 'y']:
                if question in knowledge_base[disease]:
                    disease_scores[disease] += 2
                else:
                    disease_scores[disease] -= 2
            else:
                if question in knowledge_base[disease]:
                    disease_scores[disease] -= 2
                else:
                    disease_scores[disease] += 1
        
        #delete after testing
        print("\nCurrent Ranking:\n")
        sorted_scores = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)

        for disease, score in sorted_scores:
            print(disease, "->", round(score, 2))
        print()

        # Eliminate weak diseases dynamically
        max_score = max(disease_scores.values())
        updated_possible = []

        for disease in possible_diseases:
            # Keep diseases close to best score
            if disease_scores[disease] >= max_score - 3:
                updated_possible.append(disease)
        possible_diseases = updated_possible

        # Early stopping if one disease is strongly dominant
        if len(possible_diseases) == 1:
            break

    print("\n===== FINAL DIAGNOSIS =====\n")
    best_disease = max(disease_scores, key=disease_scores.get)
    if disease_scores[best_disease] <= 0:
        print("No disease strongly matches the symptoms.")
    else:
        print(f"You are having {best_disease}")

if __name__ == "__main__":
    print("=== Expert System for Disease Diagnosis ===")
    dynamic_diagnosis()