import requests
from bs4 import BeautifulSoup
import os

if __name__ == "__main__":
    url = os.environ.get("URL")
    headers = {
        'User-Agent': os.environ.get("USER_AGENT"),
    }

    # Run as part of a GitHub Action, and where the output is written to
    env_file = os.environ.get("GITHUB_OUTPUT")

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        with open(env_file, "a") as f:
            f.write(f"availability=false\n")
        exit(1)
    soup = BeautifulSoup(response.text, 'html.parser')

    available_slots = []

    calendar_items = soup.select('.calendar-day:not(.calendar-day-unavailable)')

    for item in calendar_items:
        date_text = item.get_text().strip()
        if date_text:
            available_slots.append(date_text)

    if available_slots:
        with open(env_file, "a") as f:
            f.write(f"availability=true\n")
    else:
        with open(env_file, "a") as f:
            f.write(f"availability=false\n")

