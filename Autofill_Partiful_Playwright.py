import asyncio
import os
import pandas as pd
from playwright.async_api import async_playwright
from openai_helper import generate_answers_with_gpt

CSV_PATH = "tech_week_events.csv"
PROFILE_PATH = "partiful_profile"

# Step 1: Open the browser and let users to self-login
async def login_and_process():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_PATH,
            headless=False
        )
        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto("https://partiful.com")

        print("🔐 Please log in to Partiful. Press Enter once you're logged in.")
        input("✅ Logged in. Press Enter to start RSVP automation...")

        df = pd.read_csv(CSV_PATH)
        links = df["Link"].dropna().tolist()

        for url in links:
            print(f"\n🔗 Processing: {url}")
            try:
                await page.goto(url)
                await page.wait_for_timeout(2000)

                # Try clicking the RSVP button
                rsvp_keywords = ["Get on the list", "Going"]
                clicked = False
                for kw in rsvp_keywords:
                    btn = page.locator(f"button:has-text('{kw}')").first
                    if await btn.count() > 0:
                        await btn.scroll_into_view_if_needed()
                        await btn.click()
                        print(f"🟢 Clicked RSVP button: {kw}")
                        clicked = True
                        break
                if not clicked:
                    print("⚠️ RSVP button not found, skipping.")
                    continue

                # Click "Continue" in modal (if any)
                try:
                    await page.locator("text=Continue").first.click()
                    #print("🟢 Clicked modal Continue")
                    await page.wait_for_timeout(1000)
                except:
                    print("ℹ️ No modal Continue, may be direct form entry)")

                # Extract questions from the questionnair form of Partiful
                form = page.locator('form[name="questionnaire"]')
                await form.wait_for(timeout=5000)

                spans = form.locator("span, p")
                count = await spans.count()
                lines = []

                for i in range(count):
                    text = await spans.nth(i).inner_text()
                    if text.strip():
                        lines.append(text.strip())

                remove_prefixes = [
                    "Only the hosts can see your answers",
                    "Cancel", "Continue"
                ]
                questions = [q for q in lines if q not in remove_prefixes and len(q) > 3]

                #print("📋 Extracted：", questions)

                # generate answers using Openai API
                answers = generate_answers_with_gpt(questions)

                # Fill answers into form
                fields = form.locator("input, textarea")
                field_count = await fields.count()

                #if field_count < len(answers):
                    #print(f"⚠️ {len(answers)} answers generated but only {field_count} input fields found. Truncating.")
                answers = answers[:field_count]

                for i in range(len(answers)):
                    el = fields.nth(i)
                    answer_text = str(answers[i]) if answers[i] is not None else ""
                    await el.fill(answer_text)
                    print(f"✍️  {questions[i]} → {answer_text}")


                # Submit the RSVP form
                try:
                    await page.get_by_role("button", name="Continue").click(timeout=3000)
                    print("✅ RSVP submitted successfully")
                except:
                        print("⚠️ Final Continue button not found. Possibly auto-submitted.")

            except Exception as e:
                print(f"❌ Error while processing: {e}")
        
        print("\n🎉 All events processed! RSVP automation is complete.")

        await context.close()

if __name__ == "__main__":
    asyncio.run(login_and_process())
