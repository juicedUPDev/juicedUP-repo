import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Service Layer
class FirebaseService:
    @staticmethod
    def add_prompt(prompt_data):
        prompts_ref = db.collection('prompts')
        prompts_ref.add(prompt_data)

    @staticmethod
    def get_prompt(prompt_id):
        prompts_ref = db.collection('prompts').document(prompt_id)
        return prompts_ref.get().to_dict() if prompts_ref.exists else None

    @staticmethod
    def track_cost(cost_data):
        costs_ref = db.collection('cost_tracking')
        costs_ref.add(cost_data)

    @staticmethod
    def add_consultation(consultation_data):
        consultations_ref = db.collection('consultations')
        consultations_ref.add(consultation_data)