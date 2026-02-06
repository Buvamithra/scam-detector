SCAM_KEYWORDS = [
    "registration fee",
    "security deposit",
    "training fee",
    "processing fee",
    "offer letter fee"
]

FREE_EMAIL_DOMAINS = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com"
]

def calculate_scam_score(email, company, asked_money, message=""):
    score = 0
    reasons = []

    if asked_money:
        score += 60
        reasons.append("Company asking money is a major red flag.")

    domain = email.split("@")[-1].lower()

    if domain in FREE_EMAIL_DOMAINS:
        score += 25
        reasons.append("Free email domain used instead of company domain.")

    for word in SCAM_KEYWORDS:
        if word in message.lower():
            score += 30
            reasons.append(f"Suspicious keyword detected: '{word}'")
            break

    if company.lower() not in domain:
        score += 20
        reasons.append("Email domain does not match company name.")

    return score, reasons
