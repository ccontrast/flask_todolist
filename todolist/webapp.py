from flask import redirect, url_for, render_template, request
from model import app, Task
import model


@app.route("/")
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("list_tasks.html", tasks=tasks)
    # add ability to check off tasks

@app.route("/add", methods=["GET"])
def make_task():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def save_task():
	print request.form['task_description']
	newtask = Task(request.form['task_description'])
	model.add(newtask)
	model.save_all()
	print newtask
	return "Thank you! Your task has been saved on the to-do list."

@app.route("/edit/<task_id>", methods=["GET"])
def view_task(task_id):
	task = Task.query.get(task_id)
	return render_template("edit.html", task=task)

@app.route("/edit/<task_id>", methods=["POST"])
def edit_task(task_id):
	print request.form['edited_task']
	done = request.form.get('complete')
	task = Task.query.get(task_id)
	if done:
		task.complete()
	new_title = request.form['edited_task']
	task.title = new_title
	model.save_all()
	return redirect(url_for("home"))
