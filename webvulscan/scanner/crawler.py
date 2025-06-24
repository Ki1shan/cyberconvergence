import requests
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def extract_forms(url):
    try:
        res = requests.get(url, timeout=10, verify=False)
        res.raise_for_status()
        soup = BeautifulSoup(res.content, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[!] Error extracting forms from {url}: {e}")
        return []

def get_form_details(form):
    details = {
        "action": form.get("action"),
        "method": form.get("method", "get").lower(),
        "inputs": []
    }
    for tag in form.find_all(["input", "textarea", "select"]):
        name = tag.get("name")
        type_ = tag.get("type", "text")
        if name:
            details["inputs"].append({"type": type_, "name": name})
    return details

def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details["action"])
    data = {}
    for input in form_details["inputs"]:
        if input["type"] in ["text", "search", "email", "url"]:
            data[input["name"]] = payload
        else:
            data[input["name"]] = "test"

    try:
        if form_details["method"] == "post":
            return requests.post(target_url, data=data, timeout=10, verify=False)
        else:
            return requests.get(target_url, params=data, timeout=10, verify=False)
    except Exception as e:
        print(f"[!] Error submitting form to {target_url}: {e}")
        return None

