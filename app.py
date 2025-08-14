from flask import Flask, request, redirect, render_template
import string, random, os

app = Flask(_name_)
url_mapping = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    if request.method == "POST":
        original_url = request.form.get("url", "").strip()
        if original_url:
            if not original_url.startswith(("http://", "https://")):
                original_url = "http://" + original_url
            short_code = generate_short_code()
            url_mapping[short_code] = original_url
            short_url = request.host_url + short_code
    return render_template("index.html", short_url=short…
