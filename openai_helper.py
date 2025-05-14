# openai_helper.py
import openai

client = openai.OpenAI(
    api_key="YOUR_API_KEY_HERE"
)

def generate_answers_with_gpt(question_labels):
    identity = """
You are helping fill out RSVP forms for events. Use the following information to answer:

- Name: Natan Vidra
- Email: nvidra@anote.ai
- Company: Anote
- Job Title: CEO
- LinkedIn: https://www.linkedin.com/in/natanvidra/

If a question asks about email, company, title, or LinkedIn, always use exactly the values above.

If the question is generic (e.g. "Why are you interested in this event?", "Anything to share?"), answer simply and professionally, like:
- "Looking forward to meeting like-minded builders."
- "Excited to attend and learn more."
"""

    messages = [
        {
            "role": "system",
            "content": identity.strip()
        },
        {
            "role": "user",
            "content": f"Questions: {question_labels}\nReturn a JSON array of answers."
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.3,
    )

    import json
    
    try:
        raw = json.loads(response.choices[0].message.content.strip())

        if isinstance(raw, list) and all(isinstance(item, dict) for item in raw):
            answers = [list(item.values())[0] for item in raw]

        elif isinstance(raw, list) and all(isinstance(item, str) for item in raw):
            answers = raw
        else:
            raise ValueError("❌ Unsupported answer format.")

        return [str(a).strip() if a is not None else "" for a in answers]
    except Exception as e:
        print("❌ Error parsing GPT response:", e)
        print("🔁 Raw response:", response.choices[0].message.content)
        return ["(Failed to generate answer)"] * len(question_labels)

