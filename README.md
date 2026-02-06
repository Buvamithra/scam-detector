# scam-detector

# Scam Detection System (Rule-Based) 🛡️

## Overview
The **Scam Detection System** is a Python-based tool designed to identify potential job scams or suspicious emails. It uses a **rule-based scoring mechanism** to detect red flags such as requests for money, free email domains, suspicious keywords, and mismatched company email domains.  

This is the **first version** of the project, laying the foundation for an **AI-powered version** with confidence visualization and explainability.

---

## Features
- Detects if a company is asking for money (major scam indicator).  
- Flags free email domains instead of official company domains.  
- Searches for suspicious keywords like “registration fee” or “training fee”.  
- Checks if the email domain matches the company name.  
- Returns a **scam score** (0–100) and detailed **reasons**.  

---

Scam Score: 90%
Reasons:
- Company asking money is a major red flag.
- Free email domain used instead of company domain.
- Suspicious keyword detected: 'registration fee'
- Email domain does not match company name.
Future Improvements (Stage 2+)

Replace the rule-based system with an AI-powered model for better accuracy.

Add a confidence meter animation for visual feedback.

Include explainability to show why a score increased (e.g., feature importance).

Deploy the system to Render / Railway.

Add screenshots and demo video for LinkedIn / portfolio showcase.

Contributing

Contributions are welcome! Feel free to:

Suggest new scam indicators

Improve scoring logic

Add AI-based enhancements

License

MIT License © 2026 Buvamithra Ulagarajan


---


# Install dependencies
pip install -r requirements.txt
