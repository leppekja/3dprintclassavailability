import requests
import os
import re 

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

    available_slots = []

    spots_pattern = re.compile(r'(\d+)\s+spots?\s+left', re.IGNORECASE)
    spots_found = spots_pattern.findall(response.text)

    if spots_found:
        with open(env_file, "a") as f:
            f.write(f"availability=true\n")
    else:
        with open(env_file, "a") as f:
            f.write(f"availability=false\n")

