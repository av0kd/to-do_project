from flask import Flask,render_template
app = Flask(__name__)

@app.route('/list')
def todo_list():
    return render_template('to-do_list.html')

@app.route('/new_task')
def new_task():
    return render_template('new_task.html')
