import requests
from bs4 import BeautifulSoup
import os

if __name__ == "__main__":
    url = 'https://app.acuityscheduling.com/schedule/fb85a23f/?appointmentTypeIds%5B%5D=28912694'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    available_slots = []

    calendar_items = soup.select('.calendar-day:not(.calendar-day-unavailable)')

    for item in calendar_items:
        date_text = item.get_text().strip()
        if date_text:
            available_slots.append(date_text)

    # Get the GitHub Actions output file path
    env_file = os.environ.get("GITHUB_OUTPUT")

    if available_slots:
        with open(env_file, "a") as f:
            f.write(f"availability=true\n")
    else:
        with open(env_file, "a") as f:
            f.write(f"availability=false\n")