from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    # ルートに来たら管理画面へ
    return redirect(url_for("admin"))

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/worker")
def worker():
    return render_template("worker.html")

if __name__ == "__main__":
    app.run(debug=True)  # ローカル実行用
