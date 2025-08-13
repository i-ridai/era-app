from flask import Flask, render_template, redirect

app = Flask(__name__)

# /admin は暫定的に一覧へリダイレクト（ダッシュボードは別途実装予定）
@app.route("/admin")
def admin_redirect():
    return redirect("/admin/task-view", code=302)

@app.route("/admin/task-create")
def admin_task_create():
    return render_template("admin_task_create.html")

@app.route("/admin/task-view")
def admin_task_view():
    return render_template("admin_task_view.html")

if __name__ == "__main__":
    app.run(debug=True)
