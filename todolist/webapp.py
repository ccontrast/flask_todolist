from flask import redirect, url_for, render_template, request
from model import app, Task
import model


@app.route("/")
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("list_tasks.html", tasks=tasks)


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

