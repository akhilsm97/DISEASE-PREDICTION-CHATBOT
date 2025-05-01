DISEASE_QUESTIONS = {
    "INTRO": [
        {"q": "👋 Hello! I'm your virtual health assistant.\nWould you like to begin the symptom check? (yes/no)"}
    ],
    "BASIC_INFO": [
        {"q": "Great! May I know your age?", "symptom": "age"},
        {"q": "And your gender? (male/female/other)", "symptom": "gender"},
        {"q": "How long have you had these symptoms?", "symptom": "duration"}
    ],
    "SYMPTOM_CATEGORY": [
        {"q": "What symptom is bothering you the most right now?\n(e.g., fever, headache, cough, stomach pain, fatigue, chest pain, etc.)", "symptom": "primary_symptom"},
        {"q": "Do you have any additional symptoms?", "symptom": "secondary_symptom"}
    ],
    "FLU": [
        {"q": "Do you have a fever? (yes/no)", "symptom": "fever"},
        {"q": "Is the fever high-grade? (yes/no)", "symptom": "high_fever"},
        {"q": "Do you have a cough? (yes/no)", "symptom": "cough"},
        {"q": "Is it a dry cough? (yes/no)", "symptom": "dry_cough"},
        {"q": "Are you feeling tired or fatigued? (yes/no)", "symptom": "fatigue"}
    ],
    "DIABETES": [
        {"q": "Do you feel thirsty frequently? (yes/no)", "symptom": "excess_thirst"},
        {"q": "Are you urinating more than usual? (yes/no)", "symptom": "frequent_urination"},
        {"q": "Have you lost weight recently without trying? (yes/no)", "symptom": "weight_loss"}
    ],
    "MIGRAINE": [
        {"q": "Do you experience headaches often? (yes/no)", "symptom": "headache"},
        {"q": "Is the pain throbbing or pulsating? (yes/no)", "symptom": "throbbing_pain"},
        {"q": "Do you feel nauseous during headaches? (yes/no)", "symptom": "nausea"}
    ],
    "DENGUE": [
        {"q": "Do you have a sudden high fever? (yes/no)", "symptom": "high_fever"},
        {"q": "Are you experiencing severe headaches? (yes/no)", "symptom": "headache"},
        {"q": "Do you feel pain behind your eyes? (yes/no)", "symptom": "pain_behind_eyes"}
    ],
    "TYPHOID": [
        {"q": "Do you have prolonged fever? (yes/no)", "symptom": "fever"},
        {"q": "Are you feeling abdominal pain? (yes/no)", "symptom": "abdominal_pain"},
        {"q": "Do you have diarrhea or constipation? (yes/no)", "symptom": "diarrhea"}
    ],
    "GASTRITIS": [
        {"q": "Do you feel burning pain in the stomach? (yes/no)", "symptom": "stomach_burning"},
        {"q": "Does the pain get worse after eating? (yes/no)", "symptom": "pain_after_eating"},
        {"q": "Do you feel bloated or nauseous? (yes/no)", "symptom": "bloating"}
    ],
    "FOOD_POISONING": [
        {"q": "Have you had vomiting or diarrhea recently? (yes/no)", "symptom": "vomiting"},
        {"q": "Did you eat outside food recently? (yes/no)", "symptom": "outside_food"},
        {"q": "Are you experiencing stomach cramps? (yes/no)", "symptom": "stomach_cramps"}
    ],
    "APPENDICITIS": [
        {"q": "Do you have lower right abdominal pain? (yes/no)", "symptom": "abdominal_pain"},
        {"q": "Are you experiencing nausea? (yes/no)", "symptom": "nausea"},
        {"q": "Do you have a fever? (yes/no)", "symptom": "fever"},
        {"q": "Have you lost your appetite? (yes/no)", "symptom": "loss_of_appetite"},
        {"q": "Are you constipated? (yes/no)", "symptom": "constipation"}
    ],
    "SINUSITIS": [
        {"q": "Do you feel pressure around your nose or eyes? (yes/no)", "symptom": "facial_pressure"},
        {"q": "Do you have nasal congestion? (yes/no)", "symptom": "nasal_congestion"},
        {"q": "Is your mucus thick and discolored? (yes/no)", "symptom": "thick_mucus"}
    ],
    "TENSION_HEADACHE": [
        {"q": "Do you feel pressure like a band around your head? (yes/no)", "symptom": "head_pressure"},
        {"q": "Is the pain mild but persistent? (yes/no)", "symptom": "persistent_pain"},
        {"q": "Have you felt stressed or anxious recently? (yes/no)", "symptom": "stress"}
    ],
    "ASTHMA": [
        {"q": "Do you feel shortness of breath? (yes/no)", "symptom": "shortness_of_breath"},
        {"q": "Are you wheezing? (yes/no)", "symptom": "wheezing"},
        {"q": "Do you feel chest tightness? (yes/no)", "symptom": "chest_tightness"}
    ],
    "PNEUMONIA": [
        {"q": "Do you have chest pain while breathing? (yes/no)", "symptom": "chest_pain"},
        {"q": "Are you coughing up mucus? (yes/no)", "symptom": "cough_with_mucus"},
        {"q": "Do you have a fever or chills? (yes/no)", "symptom": "fever"}
    ],
    "CHRONIC BRONCHITIS": [
        {"q": "Are you coughing up mucus? (yes/no)", "symptom": "cough_with_mucus"},
        {"q": "Is your cough worse at night? (yes/no)", "symptom": "persistent_cough"},
        {"q": "Do you feel tired or short of breath? (yes/no)", "symptom": "fatigue"}
    ],
    "HYPERTENSION": [
        {"q": "Do you often have headaches? (yes/no)", "symptom": "headache"},
        {"q": "Do you feel dizzy or have blurred vision? (yes/no)", "symptom": "dizziness"},
        {"q": "Have you been told you have high blood pressure before? (yes/no)", "symptom": "known_hypertension"}
    ],
    "ANEMIA": [
        {"q": "Do you often feel tired or weak? (yes/no)", "symptom": "fatigue"},
        {"q": "Is your skin pale or yellowish? (yes/no)", "symptom": "pale_skin"},
        {"q": "Do you feel short of breath easily? (yes/no)", "symptom": "breathlessness"}
    ],
    "URINARY_TRACT_INFECTION": [
        {"q": "Do you feel a burning sensation while urinating? (yes/no)", "symptom": "burning_urine"},
        {"q": "Do you feel the need to urinate frequently? (yes/no)", "symptom": "frequent_urination"},
        {"q": "Do you have lower abdominal pain? (yes/no)", "symptom": "lower_abdominal_pain"}
    ],
    "THYROID_DISORDER": [
        {"q": "Have you noticed weight changes without reason? (yes/no)", "symptom": "weight_change"},
        {"q": "Do you feel unusually hot or cold? (yes/no)", "symptom": "temperature_sensitivity"},
        {"q": "Have you had mood changes or anxiety recently? (yes/no)", "symptom": "mood_swings"}
    ],
    "HEART_ATTACK": [
        {"q": "Do you feel pressure or tightness in your chest? (yes/no)", "symptom": "chest_pain"},
        {"q": "Are you experiencing shortness of breath? (yes/no)", "symptom": "shortness_of_breath"},
        {"q": "Do you feel pain in your left arm or shoulder? (yes/no)", "symptom": "left_arm_pain"},
        {"q": "Do you feel dizzy or lightheaded? (yes/no)", "symptom": "dizziness"},
        {"q": "Do you feel nauseous? (yes/no)", "symptom": "nausea"}
    ]
}
