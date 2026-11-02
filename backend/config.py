import os
from typing import Any, Dict, List, Optional

import firebase_admin
from firebase_admin import credentials, firestore


def _init_firebase() -> Optional[firestore.Client]:
    """Initialize Firebase Admin SDK using env-based credentials when available."""
    if firebase_admin._apps:
        return firestore.client()

    credentials_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
    if credentials_path:
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)
        return firestore.client()

    try:
        firebase_admin.initialize_app()
        return firestore.client()
    except Exception:
        return None


db = _init_firebase()


class FirestoreService:
    """Thin service wrapper for Firestore collections used by the API."""

    def __init__(self, collection_name: str):
        if db is None:
            raise RuntimeError(
                "Firebase Firestore is not configured. Set FIREBASE_CREDENTIALS_PATH "
                "or provide application default credentials."
            )
        self.collection_name = collection_name

    @property
    def collection(self):
        return db.collection(self.collection_name)

    def create(self, document_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.collection.document(document_id).set(payload)
        return self.get(document_id) or payload

    def get(self, document_id: str) -> Optional[Dict[str, Any]]:
        doc = self.collection.document(document_id).get()
        if not doc.exists:
            return None
        return doc.to_dict()

    def list(self, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
        docs = (
            self.collection.order_by("created_at", direction=firestore.Query.DESCENDING)
            .offset(skip)
            .limit(limit)
            .stream()
        )
        return [doc.to_dict() for doc in docs]

    def count(self) -> int:
        return len(list(self.collection.stream()))

    def delete(self, document_id: str) -> None:
        self.collection.document(document_id).delete()


class FirebaseService:
    """Backward-compatible service entry point for older code paths."""

    @staticmethod
    def add_prompt(prompt_data):
        service = FirestoreService("prompts")
        prompt_id = str(prompt_data.get("id") or prompt_data.get("name") or "prompt")
        return service.create(prompt_id, prompt_data)

    @staticmethod
    def get_prompt(prompt_id):
        service = FirestoreService("prompts")
        return service.get(prompt_id)

    @staticmethod
    def track_cost(cost_data):
        service = FirestoreService("cost_tracking")
        cost_id = str(cost_data.get("id") or cost_data.get("name") or "cost")
        return service.create(cost_id, cost_data)

    @staticmethod
    def add_consultation(consultation_data):
        service = FirestoreService("consultations")
        consultation_id = str(consultation_data.get("id") or "consultation")
        return service.create(consultation_id, consultation_data)

    @staticmethod
    def get_consultation(consultation_id):
        service = FirestoreService("consultations")
        return service.get(consultation_id)
