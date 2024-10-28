from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import db, User, Todo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/tasks')
@login_required
def task():
    todos = Todo.query.filter_by(created_by=current_user.id).all()
    return render_template('task.html', todos=todos)

@main.route('/add-task')
@login_required
def addTask():
    return render_template('add-task.html')

@main.route('/add-task', methods=['POST'])
@login_required
def addTask_post():
    title = request.form.get('title')
    description = request.form.get('desc')
    new_task = Todo(title=title, description=description, created_by=current_user.id)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('main.task'))

@main.route('/update/<int:id>/', methods=['GET', 'POST'])
@login_required
def update(id):
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('desc')
        todo = Todo.query.filter_by(id=id).first()
        todo.title = title
        todo.description = description
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('main.task'))
    todo = Todo.query.filter_by(id=id).first()
    return render_template('update.html', todo=todo)

@main.route('/delete/<int:id>/')
@login_required
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.task'))