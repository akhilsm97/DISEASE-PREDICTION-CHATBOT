from django.shortcuts import render
from django.http import JsonResponse
import joblib
import os
from .questions import DISEASE_QUESTIONS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, 'model_assets/model.pkl'))
symptoms = joblib.load(os.path.join(BASE_DIR, 'model_assets/symptoms.pkl'))
encoder = joblib.load(os.path.join(BASE_DIR, 'model_assets/encoder.pkl'))
# SYMPTOM TO DISEASE MAP

SYMPTOM_TO_DISEASE = {
    "fever": "FLU",
    "cough": "CHRONIC BRONCHITIS",
    "headache": "MIGRAINE",
    "stomach pain": "APPENDICITIS",
    "vomiting":"FOOD_POISONING",
    "chest pain": "HEART_ATTACK",
    "fatigue": "ANEMIA",
    "sore throat": "TONSILLITIS",
    "shortness of breath": "ASTHMA",
    "nausea": "FOOD_POISONING",
    "joint pain": "ARTHRITIS",
    "skin rash": "DENGUE",
    "muscle pain": "MALARIA",
    "sneezing": "COMMON_COLD",
    "vomiting": "GASTRITIS",
    "blurred vision": "GLAUCOMA"
}

def get_chat_stage(session):
    return session.get("stage", "INTRO")

def set_chat_stage(session, stage):
    session["stage"] = stage
    session.modified = True

def chat_view(request):
    
    return render(request, "chatbot/chat.html")

def get_next_question(request):
    if request.method == "POST":
        user_input = request.POST.get("message", "").strip().lower()

        if user_input in ["clear chat", "reset chat"]:
            # Clear session data (reset the stage and any stored responses)
            request.session.flush()
            set_chat_stage(request.session, "INTRO")
            return JsonResponse({"response": "🧹 Chat cleared. You can start fresh. Say 'start' to begin."})

        

        stage = get_chat_stage(request.session)

        # INTRO
        if stage == "INTRO":
            if any(word in user_input for word in ["yes", "start", "hi", "hello", "ok"]):
                set_chat_stage(request.session, "BASIC_INFO")
                request.session["basic_answers"] = []
                return JsonResponse({"response": DISEASE_QUESTIONS["INTRO"][0]["q"]})
            else:
                return JsonResponse({"response": "Okay, say 'start' to begin."})

        # BASIC INFO
        elif stage == "BASIC_INFO":
            basic = request.session.get("basic_answers", [])
            basic.append(user_input)
            request.session["basic_answers"] = basic

            if len(basic) < len(DISEASE_QUESTIONS["BASIC_INFO"]):
                next_q = DISEASE_QUESTIONS["BASIC_INFO"][len(basic)]["q"]
                return JsonResponse({"response": next_q})
            else:
                set_chat_stage(request.session, "SYMPTOM_CATEGORY")
                return JsonResponse({"response": DISEASE_QUESTIONS["SYMPTOM_CATEGORY"][0]["q"]})

        # SYMPTOM CATEGORY
        elif stage == "SYMPTOM_CATEGORY":

            matched_key = SYMPTOM_TO_DISEASE.get(user_input.lower())
            print("MATCHED KEY IS ", matched_key)

            # Print symptoms for the matched disease
            if matched_key:
                print(f"Symptoms for {matched_key}: {[q.get('symptom') for q in DISEASE_QUESTIONS[matched_key]]}")
            if matched_key in DISEASE_QUESTIONS:
                request.session["disease_guess"] = matched_key
                request.session["symptom_answers"] = []
                set_chat_stage(request.session, "SYMPTOM_FLOW")
                return JsonResponse({"response": DISEASE_QUESTIONS[matched_key][0]["q"]})
            else:
                return JsonResponse({
                    "response": "❗Sorry, I didn't understand that. Try something like 'fever', 'cough', or 'fatigue'."
                })

        # SYMPTOM FLOW
        elif stage == "SYMPTOM_FLOW":
            disease_key = request.session.get("disease_guess")
            answers = request.session.get("symptom_answers", [])
            answers.append(user_input)
            request.session["symptom_answers"] = answers

            if len(answers) < len(DISEASE_QUESTIONS[disease_key]):
                next_q = DISEASE_QUESTIONS[disease_key][len(answers)]["q"]
                return JsonResponse({"response": next_q})
            else:
                feature_vector = [0] * len(symptoms)
                for q, ans in zip(DISEASE_QUESTIONS[disease_key], answers):
                    symptom = q.get("symptom")
                    if symptom and symptom in symptoms and "yes" in ans.lower():
                        feature_vector[symptoms.index(symptom)] = 1

                prediction = model.predict([feature_vector])[0]
                print(f"PREDICTION RESULT {prediction}")
                predicted_disease = encoder.inverse_transform([prediction])[0]

                response_text = f"✅ Based on your symptoms, you may have *{predicted_disease}*. Please consult a doctor."
                return JsonResponse({"response": response_text})

    return JsonResponse({"response": "Invalid request."})
