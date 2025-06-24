from datetime import datetime

def write_html_report(results):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = f"""<html>
<head>
    <title>Scan Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #1e1e1e; color: #eee; padding: 20px; }}
        h1 {{ color: #ffa500; }}
        h2 {{ border-bottom: 1px solid #444; }}
        .section {{ margin-bottom: 30px; }}
        .vuln {{ margin: 10px 0; padding: 10px; background: #333; border-left: 4px solid #f00; }}
    </style>
</head>
<body>
    <h1>Web Vulnerability Scan Report</h1>
    <p><strong>Scan Time:</strong> {now}</p>
"""

    for vuln_type, items in results.items():
        html += f'<div class="section"><h2>{vuln_type.upper()}</h2>'
        if items:
            for item in items:
                html += f'<div class="vuln"><strong>URL:</strong> {item["url"]}<br><strong>Payload:</strong> {item["payload"]}</div>'
        else:
            html += "<p>No vulnerabilities found.</p>"
        html += "</div>"

    html += "</body></html>"

    with open("scan_report.html", "w") as f:
        f.write(html)

