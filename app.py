from flask import Flask, render_template

app = Flask(__name__)

@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/admin/task-create")
def admin_task_create():
    return render_template("admin_task_create.html")

@app.route("/admin/task-view")
def admin_task_view():
    return render_template("admin_task_view.html")

if __name__ == "__main__":
    app.run(debug=True)
