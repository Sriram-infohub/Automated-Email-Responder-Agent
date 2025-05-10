from email_reader import read_latest_emails
from email_classifier import classify_email
from email_responder import generate_reply
from feedback_manager import save_feedback
from gmail_draft_saver import authenticate_gmail, create_draft

def main():
    # Authenticate Gmail only once
    service = authenticate_gmail()

    emails = read_latest_emails()
    for email_data in emails:
        sender = email_data["from"]
        subject = email_data["subject"]
        body = email_data["body"]

        print("\nFrom:", sender)
        print("Subject:", subject)
        print("Body:", body[:200], "...\n")

        label = classify_email(body)
        print("Category:", label)

        draft_reply = generate_reply(body)
        print("\nDraft Reply:\n", draft_reply)

        # Save to Gmail Drafts
        try:
            draft = create_draft(
                service,
                user_id="me",
                message_body=draft_reply,
                subject=f"RE: {subject}",
                to_email=sender
            )
            print("✅ Draft saved to Gmail (ID:", draft['id'], ")")
        except Exception as e:
            print("❌ Failed to save draft:", e)

        # Collect feedback from user
        feedback = input("Was this reply helpful? (yes/no): ")
        if feedback.lower() == "no":
            improved = input("Enter your improved version: ")
            save_feedback(subject, draft_reply, feedback, improved)
        else:
            save_feedback(subject, draft_reply, feedback, draft_reply)

if __name__ == "__main__":
    main()
