import os
import time

def take_screenshot(driver, vuln_type):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{vuln_type}_{timestamp}.png"
    driver.save_screenshot(filename)
