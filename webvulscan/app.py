from flask import Flask, render_template, request
from scanner import detector, logger
from utils.report import write_html_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {"xss": [], "sqli": [], "csrf": []}
    if request.method == "POST":
        url = request.form["url"]
        results["xss"] = [{"url": r[0], "payload": r[1]} for r in detector.test_xss(url)]
        results["sqli"] = [{"url": r[0], "payload": r[1]} for r in detector.test_sqli(url)]
        results["csrf"] = [{"url": r[0], "payload": r[1]} for r in detector.test_csrf(url)]
        logger.save_results(results)
        write_html_report(results)
    return render_template("index.html", results=results)

@app.route("/report")
def download_report():
    return open("scan_report.html").read()

