from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from database import get_credentials
from logging_handler import log_successful_application, log_failed_application
from datetime import datetime

def login_to_internshala(driver):
    """Logs into Internshala using stored credentials."""
    email, password = get_credentials()
    if not email or not password:
        print("Error: No credentials found!")
        return False

    driver.get("https://internshala.com/")
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[text()='Login']").click()
    time.sleep(2)

    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)

    return True

def apply_for_multiple_internships(max_applications, work_from_home, category, resume_path, cover_letter_path, progress_bar):
    """Applies for internships & updates progress dynamically."""
    CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"  # Change if needed
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://internshala.com/internships/")
    time.sleep(3)
    try:
        driver = webdriver.Chrome(service=service, options=options)
        print("✅ ChromeDriver initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing ChromeDriver: {str(e)}")

    if work_from_home:
        driver.find_element(By.XPATH, "//label[contains(text(),'Work From Home')]").click()
        time.sleep(2)

    driver.find_element(By.XPATH, f"//label[contains(text(),'{category}')]").click()
    time.sleep(2)

    internships = driver.find_elements(By.XPATH, "//div[contains(@class, 'internship_meta')]")
    applied_count = 0

    for internship in internships[:max_applications]:
        try:
            title = internship.find_element(By.XPATH, ".//h3").text
            link = internship.find_element(By.XPATH, ".//a").get_attribute("href")

            internship.click()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[-1])

            driver.find_element(By.XPATH, "//input[@type='file']").send_keys(resume_path)
            driver.find_element(By.XPATH, "//textarea[@id='cover_letter']").send_keys(open(cover_letter_path, "r").read())
            driver.find_element(By.XPATH, "//button[contains(text(),'Submit Application')]").click()

            applied_count += 1
            log_successful_application(title, link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            progress_bar["value"] = (applied_count / max_applications) * 100
            progress_bar.update_idletasks()

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            log_failed_application(title, link, str(e))

    driver.quit()
