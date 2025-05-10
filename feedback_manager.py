import json

def save_feedback(email_subject, original_reply, user_feedback, improved_reply):
    feedback_data = {
        "subject": email_subject,
        "original_reply": original_reply,
        "user_feedback": user_feedback,
        "improved_reply": improved_reply
    }
    with open("feedback_log.json", "a") as f:
        f.write(json.dumps(feedback_data) + "\n")
