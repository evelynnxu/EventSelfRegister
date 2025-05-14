import requests
import csv

url = "https://api.tech-week.com/list_events/?city=NYC"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.tech-week.com/calendar",
    "Origin": "https://www.tech-week.com"
}

response = requests.get(url, headers=headers)
data = response.json()

#print(type(data))  
#print(data[0])     

with open("tech_week_events.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Time", "Neighborhood", "City", "Themes", "Link"])
    for event in data:
        writer.writerow([
            event.get("event_name"),
            event.get("start_time"),
            event.get("neighborhood"),
            event.get("city"),
            ", ".join(event.get("themes", [])),
            event.get("invite_url")
        ])
