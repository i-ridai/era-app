from flask import Flask, render_template

app = Flask(__name__)

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/worker")
def worker():
    return render_template("worker.html")

if __name__ == "__main__":
    app.run(debug=True)
