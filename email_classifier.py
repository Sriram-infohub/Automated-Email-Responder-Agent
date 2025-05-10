def classify_email(email_text):
    email_text = email_text.lower()
    if "refund" in email_text or "return" in email_text:
        return "Customer Service"
    elif "job" in email_text or "resume" in email_text:
        return "Job Inquiry"
    elif "offer" in email_text or "discount" in email_text:
        return "Promotion"
    else:
        return "General"
