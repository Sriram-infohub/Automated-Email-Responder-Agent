# 📬 Automated Email Responder Agent 🤖

A smart AI-powered email assistant that can **read**, **classify**, **generate replies**, and even **refine responses** based on user feedback. Built using Gmail API, Python, and Gemini AI.

---


## 📌 **Core Features:**
- 🔍 Reads unread emails from Gmail
- 🧠 Classifies emails using ML/NLP
- ✍️ Drafts smart replies using Gemini AI
- 🔁 Accepts feedback and improves replies
- 📦 Stores processed emails and replies on Draft Mail

---

## 🧠 Technologies Used

- Python
- Gmail API
- Google Gemini AI
- scikit-learn / spaCy (for classification)
- JSON / CSV (data persistence)

---

## ✨ Usage Flow

1. **Agent logs into Gmail**
2. **Fetches unread emails**
3. **Classifies them (e.g., Work, Personal, Spam)**
4. **Generates a draft reply using Gemini AI**
5. **Displays it to you**
6. **You approve or give feedback**
7. **Agent refines the reply**
8. **Stores response + feedback for future learning**

---

## 🛠️ Project Structure

```
📁 email_agent_project/
├── .env                          # load environment variables securely.
├── credentials.json              # Gmail API access on Google Cloud.
├── email_classifier.py           # Classifies emails
├── email_reader.py               # Fetches emails using Gmail API
├── email_responder.py            # Generates smart replies using Gemini API
├── feedback_log.json             # Stores responses & feedback
├── feedback_manager.py           # Helper functions
├── gamil_draft_saver.py          # saves draft emails in a Gmail account
├── main.py                       # Orchestrates all components
└── requirements.txt              # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. 🔐 Gmail API Setup

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable **Gmail API**
- Create **OAuth 2.0 credentials** and download `credentials.json`
- Place `credentials.json` in your project root

### 2. 🔑 Gemini API Setup

- Create a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Add the key to `.env` like this:

```json
{
  "EMAIL=your-email(create-dummy)",
  "PASSWORD=your-password-or-app password",
  "GENAI_API_KEY=your-api-key"
}
```

---

## ▶️ How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the agent
python main.py
```

---



## 📁 Sample Output (stored locally)

All email-response pairs and feedback are saved in JSON/CSV for reference and retraining:

```json
{
  "email_subject": "Meeting Reminder",
  "category": "Work",
  "generated_reply": "Thank you for the reminder. Looking forward to it.",
  "user_feedback": "Make it more formal.",
  "refined_reply": "Thank you for the reminder. I will be there on time. Looking forward to our discussion."
}
```

---

## 📌 Roadmap

- [x] Email fetching & classification
- [x] Smart reply generation
- [x] Feedback-based refinement
- [ ] Active learning from feedback
- [ ] Web interface or mobile version

---

## 🤝 Contributing

We welcome contributions! Feel free to fork the repo, suggest improvements, or open issues.

---


## 📞 Contact

**Author**: [Sriram K](https://www.linkedin.com/in/sriram-k-94b539283)  
📧 sriramkannanofficial@gmail.com  
📍 Coimbatore, India

---

## 📄 License

This project is licensed under the MIT License.
