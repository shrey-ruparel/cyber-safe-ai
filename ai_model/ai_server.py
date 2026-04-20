from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from logic import detect_patterns

app = FastAPI()

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

class InputText(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: InputText):
    text = input.text
    
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    conf = model.predict_proba(X).max()
    
    reasons = detect_patterns(text)
    
    if pred == "scam" or reasons:
        verdict = "Scam"
    else:
        verdict = "Safe"
    
    return {
        "verdict": verdict,
        "confidence": float(conf),
        "explanation": reasons,
        "action": "Do not click. Report to 1930." if verdict == "Scam" else "Safe"
    }