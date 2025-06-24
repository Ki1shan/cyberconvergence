import time
import requests
import urllib3
from scanner import crawler
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

xss_payloads = [
    "<script>alert(1)</script>",
    "\"><svg/onload=alert(1)>",
    "';alert(String.fromCharCode(88,83,83))//"
]

sqli_payloads = [
    "' OR '1'='1",
    "' OR 1=1--",
    "' UNION SELECT NULL,NULL--"
]

def get_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(15)
    return driver

def test_xss(url):
    results = []
    forms = crawler.extract_forms(url)
    for form in forms:
        details = crawler.get_form_details(form)
        for payload in xss_payloads:
            response = crawler.submit_form(details, url, payload)
            if response and payload in response.text:
                print(f"[+] XSS Detected: {url} | Payload: {payload}")
                results.append((url, payload))
    return results

def test_sqli(url):
    results = []
    for payload in sqli_payloads:
        test_url = f"{url}?id={payload}"
        try:
            res = requests.get(test_url, timeout=10, verify=False)
            if any(error in res.text.lower() for error in ["sql", "mysql", "syntax", "query failed"]):
                print(f"[+] SQLi Detected: {test_url}")
                results.append((test_url, payload))
        except Exception as e:
            print(f"[!] SQLi Error: {test_url} | {e}")
    return results

def test_csrf(url):
    results = []
    forms = crawler.extract_forms(url)
    for form in forms:
        method = form.get("method", "").lower()
        inputs = form.find_all("input")
        token_fields = [i for i in inputs if "csrf" in i.get("name", "").lower()]
        if method == "post" and not token_fields:
            print(f"[+] CSRF Risk: {url} (no CSRF token)")
            results.append((url, "Missing Anti-CSRF Token"))
    return results

