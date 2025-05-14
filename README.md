
# 🧠 Auto-RSVP Agent for NYC Tech Week Events

This project builds an automated RSVP agent that scrapes upcoming NYC Tech Week events from [tech-week.com](https://www.tech-week.com/calendar) and uses AI (OpenAI GPT) to auto-fill RSVP forms hosted on [Partiful](https://partiful.com).

---

## 🚀 Features

- ✅ Automatically scrapes NYC Tech Week event data via API
- ✅ Detects and processes RSVP links hosted on Partiful
- ✅ Uses GPT-3.5 to generate context-aware answers to host questions
- ✅ Auto-fills the RSVP form and submits responses

---

## 📁 Project Structure

```
.
├── WebScraper.py                  # Scrapes Tech Week event data
├── tech_week_events.csv           # Output of the scraper (can be filtered manually)
├── Autofill_Partiful_Playwright.py # Automates RSVP process using Playwright
├── openai_helper.py               # GPT-based answer generation
├── partiful_profile/              # Local Chrome profile (excluded via .gitignore)
└── test_tech_week_events.csv      # Optional sample file for testing automation
```

---

## 🧠 How it Works

1. **Data Collection**
   - Run `WebScraper.py` to collect all upcoming NYC Tech Week events and export them to `tech_week_events.csv`.

2. **RSVP Automation**
   - Run `Autofill_Partiful_Playwright.py`. It:
     - Opens Chrome via Playwright.
     - Prompts you to log in to Partiful once.
     - Visits each event link and clicks "Get on the list" / "Going".
     - Extracts host questions from the RSVP form.
     - Calls OpenAI to generate appropriate responses.
     - Fills and submits the form automatically.

---

## 🔐 OpenAI API Key

The GPT-powered module requires an OpenAI API key. You must manually add your key in `openai_helper.py`:

```python
client = openai.OpenAI(api_key="YOUR_API_KEY_HERE")
```

---

## 📦 Dependencies

Install required packages with:

```bash
pip install -r requirements.txt
```

Sample `requirements.txt`:

```txt
playwright
openai
pandas
requests
```

After installing Playwright, run:

```bash
playwright install
```

---

## ✅ Example Usage

```bash
# Step 1: Scrape events
python WebScraper.py

# Step 2: Run autofill
python Autofill_Partiful_Playwright.py
```

---

## 📄 License

MIT License — use at your own risk and comply with third-party platform terms.

---

## 🤝 Acknowledgments

- [Partiful](https://partiful.com) for event RSVP infrastructure
- [Tech Week](https://www.tech-week.com) for open event data
- [OpenAI](https://platform.openai.com) for language model API
