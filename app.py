from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

tasks = [
    {"id": 1, "title": "サンプルタスク1", "status": "todo", "assignee": "佐藤", "content": "配管工事", "start": "2025-08-10", "end": "2025-08-20", "progress": 20, "tags": ["水道", "住宅"]},
    {"id": 2, "title": "サンプルタスク2", "status": "in_progress", "assignee": "鈴木", "content": "内装工事", "start": "2025-08-15", "end": "2025-08-25", "progress": 50, "tags": ["内装"]}
]

@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html', tasks=tasks)

@app.route('/admin/task-create', methods=['GET', 'POST'])
def task_create():
    if request.method == 'POST':
        new_task = {
            "id": len(tasks) + 1,
            "title": request.form['title'],
            "status": "todo",
            "assignee": request.form['assignee'],
            "content": request.form['content'],
            "start": request.form['start'],
            "end": request.form['end'],
            "progress": int(request.form['progress']),
            "tags": request.form.getlist('tags')
        }
        tasks.append(new_task)
        return redirect(url_for('task_view'))
    return render_template('admin_task_create.html')

@app.route('/admin/task-view')
def task_view():
    return render_template('admin_task_view.html', tasks=tasks)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
