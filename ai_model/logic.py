import re

def detect_patterns(text):
    reasons = []
    
    if re.search(r"http[s]?://", text):
        reasons.append("Suspicious link detected")
        
    if "otp" in text.lower():
        reasons.append("Requests OTP")
        
    if "urgent" in text.lower() or "blocked" in text.lower():
        reasons.append("Urgency or threat language used")
    
    return reasons