import os
import csv
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from dataset import database_set
from titanic import decision_tree


# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def _upload_file(upload_folder):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder, filename))
            database_set()
            return redirect(request.url)
    return render_template('upload.html')
