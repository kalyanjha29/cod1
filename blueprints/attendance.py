from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import ClassRoom, Student, Attendance
from extensions import db
import os

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/class/<int:class_id>/upload', methods=['GET', 'POST'])
@login_required
def upload_photo(class_id):
    classroom = ClassRoom.query.get_or_404(class_id)
    if request.method == 'POST':
        if 'photo' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['photo']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        
        # Save file and process recognition
        return redirect(url_for('attendance.recognition_result', class_id=class_id))
    return render_template('upload_photo.html', classroom=classroom)

@attendance_bp.route('/class/<int:class_id>/results')
@login_required
def recognition_result(class_id):
    classroom = ClassRoom.query.get_or_404(class_id)
    return render_template('recognition_result.html', classroom=classroom)

@attendance_bp.route('/class/<int:class_id>/report')
@login_required
def attendance_report(class_id):
    classroom = ClassRoom.query.get_or_404(class_id)
    attendances = Attendance.query.join(Student).filter(Student.class_id == class_id).all()
    return render_template('attendance_report.html', classroom=classroom, attendances=attendances)