from flask import Flask, render_template, request
from rule import calculate_scam_score

app = Flask(__name__, static_folder="static", template_folder="templates")
print("FLASK ROOT PATH:", app.root_path)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        email = request.form["email"]
        company = request.form["company"]
        asked_money = request.form.get("money") == "yes"
        message = request.form["message"]

        score, reasons = calculate_scam_score(
            email, company, asked_money, message
        )

        if score >= 61:
            status = "🚨 SCAM"
        elif score >= 31:
            status = "⚠️ SUSPICIOUS"
        else:
            status = "✅ LIKELY SAFE"

        result = {
            "score": score,
            "status": status,
            "reasons": reasons
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
