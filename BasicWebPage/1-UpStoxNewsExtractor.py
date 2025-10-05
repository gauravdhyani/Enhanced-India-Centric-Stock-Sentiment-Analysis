import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- Setup Chrome ---
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)
driver = webdriver.Chrome(service=service, options=options)
# --- Open website ---
url = "https://upstox.com/news/"  # replace with actual URL
driver.get(url)

try:
    # Wait until at least one h2 is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h2"))
    )
    
    # Find all h2 elements
    h2_elements = driver.find_elements(By.TAG_NAME, "h2")
    
    # Extract text
    headlines = [h2.text for h2 in h2_elements if h2.text.strip() != ""]  
    
    # Save to CSV
    df = pd.DataFrame(headlines, columns=["Headline"])
    df.to_csv("headlines.csv", index=False)
    print(f"Saved {len(headlines)} headlines to headlines.csv")

finally:
    driver.quit()
