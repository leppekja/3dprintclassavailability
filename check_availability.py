import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

if __name__ == "__main__":
    url = os.environ.get("URL")
    env_file = os.environ.get("GITHUB_OUTPUT")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    user_agent = os.environ.get("USER_AGENT")
    if user_agent:
        chrome_options.add_argument(f'user-agent={user_agent}')
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        driver.get(url)
        
        time.sleep(2)  
        
        page_content = driver.page_source
        
        spots_pattern = re.compile(r'(\d+)\s+spots?\s+left', re.IGNORECASE)
        spots_found = spots_pattern.findall(page_content)
        
        if spots_found:
            print(f"Found availability: {spots_found}")
            with open(env_file, "a") as f:
                f.write(f"availability=true\n")
        else:
            print("No availability found")
            with open(env_file, "a") as f:
                f.write(f"availability=false\n")
                
    except Exception as e:
        print(f"Error occurred: {e}")
        with open(env_file, "a") as f:
            f.write(f"availability=false\n")
    finally:
        if 'driver' in locals():
            driver.quit()

