
# 🧠 Auto-RSVP Agent for NYC Tech Week Events

This project builds an automated RSVP agent that scrapes upcoming NYC Tech Week events from [tech-week.com](https://www.tech-week.com/calendar) and uses AI (OpenAI GPT) to auto-fill RSVP forms hosted on [Partiful](https://partiful.com).

---

## 🚀 Features

- ✅ Automatically scrapes NYC Tech Week event data via API
- ✅ Detects and processes RSVP links hosted on Partiful
- ✅ Uses GPT-3.5 to generate context-aware answers to host questions
- ✅ Auto-fills the RSVP form and submits responses

---


## ✅ How to use

# Step 1: Clone the GitHub repo
You can either use Git, or just download the ZIP and unzip it anywhere on your computer.

# Step 2: Make sure all the dependencies installed
This script uses Python, so make sure you have Python 3.10 or higher installed.

Once you're in the project folder, open a terminal and run:

```bash
pip install -r requirements.txt
```

Sample `requirements.txt`:

```txt
playwright
openai
pandas
```

After installing Playwright, run:

```bash
playwright install
```
# Step 3: Change/add information in openai_helper.py

The GPT-powered module requires an OpenAI API key. You must manually add your key in `openai_helper.py`:

```python
client = openai.OpenAI(api_key="YOUR_API_KEY_HERE")
```
DM me if you don't have a openai api key and I can share mine.

Then enter your own information which will be used to fill in the RSVP form in `openai_helper.py`:

```python
def generate_answers_with_gpt(question_labels):
    identity = """
You are helping fill out RSVP forms for events. Use the following information to answer:

- Name: YOUR_NAME_HERE
- Email: YOUR_EMAIL_HERE
- Company: Anote
- Job Title: YOUR_TITLE_HERE
- LinkedIn: YOUR_LINKEDIN_HERE

If a question asks about email, company, title, or LinkedIn, always use exactly the values above.
```

# Step 4: Run autofill


```bash
python Autofill_Partiful_Playwright.py
```
---

Then follow the instruction in the terminal. Once you run "Autofill_Partiful_Playwright.py", it will automatically pop up a chrome window of partiful website. 

The script needs you to log in to your own Partiful account once, so it can use your session for registration. Once you have logged in, back to the terminal to press enter. 

After that, the program will start to RSVP for you automatically, and you should wait until the terminal shows "All events processed! RSVP automation is complete". 

Reminder: You will not receive email after registering for the events. You will only receive SMS notifications or emails after the event host approve your attendence. 

Feel free to DM me(Yining) if you have any trouble using this tool on Slack!
