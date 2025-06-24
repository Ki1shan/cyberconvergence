# Web Application Vulnerability Scanner

## Overview

This tool is a custom-built vulnerability scanner that automates the detection of OWASP Top 10 threats using:

- **Flask** (Web interface)
- **Selenium + Firefox** (Headless browser automation)
- **BeautifulSoup** (Form crawling and parsing)

It targets three critical vulnerabilities:

1. Cross-Site Scripting (XSS)
2. SQL Injection (SQLi)
3. Cross-Site Request Forgery (CSRF)

---

Usuage:

Open http://127.0.0.1:5000
    Enter a target URL (e.g. http://testphp.vulnweb.com)
    Click "Scan"
    View categorized results for:
       XSS (injected scripts)
       SQLi (URL injections, error messages)
       CSRF (missing tokens)

Export results to HTML report using the "Download Report" button.


Setup Instructions:

### Install Requirements

```bash
sudo apt install firefox-esr geckodriver -y
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt


To run:
source env/bin/activate
python run.py
