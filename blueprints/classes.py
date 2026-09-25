from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import ClassRoom, Student
from extensions import db

classes_bp = Blueprint('classes', __name__)

@classes_bp.route('/')
@classes_bp.route('/dashboard')
@login_required
def dashboard():
    classrooms = ClassRoom.query.all()
    return render_template('dashboard.html', classrooms=classrooms)

@classes_bp.route('/class/new', methods=['GET', 'POST'])
@login_required
def new_class():
    if request.method == 'POST':
        name = request.form.get('name')
        subject = request.form.get('subject')
        new_room = ClassRoom(name=name, subject=subject)
        db.session.add(new_room)
        db.session.commit()
        return redirect(url_for('classes.dashboard'))
    return render_template('new_class.html')

@classes_bp.route('/class/<int:class_id>')
@login_required
def class_detail(class_id):
    classroom = ClassRoom.query.get_or_404(class_id)
    return render_template('class_detail.html', classroom=classroom)

@classes_bp.route('/class/<int:class_id>/student/new', methods=['GET', 'POST'])
@login_required
def new_student(class_id):
    if request.method == 'POST':
        name = request.form.get('name')
        roll_number = request.form.get('roll_number')
        student = Student(name=name, roll_number=roll_number, class_id=class_id)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('classes.class_detail', class_id=class_id))
    return render_template('new_student.html', class_id=class_id)