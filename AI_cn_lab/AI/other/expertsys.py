diseases = {
    "flu": ["body aches", "high fever", "dry cough", "extreme fatigue", "chills"],
    "cold": ["runny nose", "sneezing", "nasal congestion", "watery eyes", "sore throat"],
    "covid": ["loss of taste", "shortness of breath", "persistent dry cough", "fatigue", "high fever"],
    "diabetes": ["increased thirst", "frequent urination", "blurred vision", "unexplained weight loss", "slow healing wounds"],
    "malaria": ["chills", "sweating", "headache", "nausea", "muscle pain"],
}
print("Answer the following questions with 'yes' or 'no':")
matched = {}
symptoms_checked = set()

for disease, symptoms in diseases.items():
    match_count = 0
    for symptom in symptoms:
        if symptom in symptoms_checked:
            continue
        print(f"Do you have {symptom}? (y/n)")
        response = input().strip().lower()
        if response not in {"y", "n"}:
            print("Invalid response. Please answer with 'yes' or 'no'.")
            continue
        symptoms_checked.add(symptom)
        if response == "y":
            match_count += 1
    if match_count > 0:
        matched[disease] = match_count

most_probable_disease = None
max_count = 0
for disease, count in matched.items():
    if count > max_count:
        max_count = count
        most_probable_disease = disease
if most_probable_disease:
    print(f"The most probable disease is {most_probable_disease} with {max_count} matching symptoms.")
else:
    print("No matching disease found.")
