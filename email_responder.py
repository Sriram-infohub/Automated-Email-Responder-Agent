import google.generativeai as genai

genai.configure(api_key="your-gemini-api-key")

def generate_reply(email_body):
    model = genai.GenerativeModel('gemini-1.5-flash') # Using the recommended model
    prompt = f"Please reply to the following email:\n\n{email_body}\n\nKeep the reply concise and professional."
    response = model.generate_content(prompt)
    return response.text

