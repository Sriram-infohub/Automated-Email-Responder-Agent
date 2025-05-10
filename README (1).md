# 📬 Automated Email Responder Agent 🤖

A smart AI-powered email assistant that can **read**, **classify**, **generate replies**, and even **refine responses** based on user feedback. Built using Gmail API, Python, and Gemini AI.

---

## 🚀 Demo

![Email Bot Flow](https://github.com/yourusername/email-agent-demo.gif) <!-- Optional: Add a demo GIF or screenshot -->

**Core Features:**
- 🔍 Reads unread emails from Gmail
- 🧠 Classifies emails using ML/NLP
- ✍️ Drafts smart replies using Gemini AI
- 🔁 Accepts feedback and improves replies
- 📦 Stores processed emails and replies locally

---

## 🛠️ Project Structure

```
📁 email_agent_project/
├── main.py              # Orchestrates all components
├── classify.py          # Classifies emails
├── fetch.py             # Fetches emails using Gmail API
├── generate.py          # Generates smart replies using Gemini API
├── store.py             # Stores responses & feedback
├── utils.py             # Helper functions
├── config.json          # API keys and credentials
└── requirements.txt     # Python dependencies
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
- Add the key to `config.json` like this:

```json
{
  "gmail_user": "youremail@gmail.com",
  "gemini_api_key": "YOUR_GEMINI_API_KEY"
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

## 🧠 Technologies Used

- Python
- Gmail API
- Google Gemini AI
- scikit-learn / spaCy (for classification)
- JSON / CSV (data persistence)

---

## 📞 Contact

**Author**: [Sriram Kannan](https://www.linkedin.com/in/sriram-k-94b539283)  
📧 sriramkannanofficial@gmail.com  
📍 Coimbatore, India

---

## 📄 License

This project is licensed under the MIT License.