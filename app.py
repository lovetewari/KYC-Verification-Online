from flask import Flask, request, redirect, render_template, session, url_for
import uuid
import json
import os
import base64
import cv2
import numpy as np
import pytesseract
from PIL import Image
from werkzeug.utils import secure_filename
import uuid

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id_type = request.form['id_type']
        session['id_type'] = id_type
        return redirect(url_for('id_file'))
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/id_file', methods=['GET', 'POST'])
def id_file():
    id_type = session.get('id_type')
    if id_type is None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        id_file = request.files['id_file']
        if id_file and allowed_file(id_file.filename):
            filename = secure_filename(id_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            id_file.save(filepath)

            if id_type == 'ic':
                return redirect(url_for('id_detail', filename=filename))
            else:
                return redirect(url_for('face_recognition_selfie', filename=filename))

    return render_template('id_file.html', id_type=id_type)

@app.route('/id_detail/<filename>',methods=['GET'])
def id_detail(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image = Image.open(filepath)
    ocr_text = pytesseract.image_to_string(image)

    return render_template('id_detail.html', ocr_text=ocr_text)

@app.route('/face_recognition_selfie/<filename>', methods=['GET', 'POST'])
def face_recognition_selfie(filename):
    if request.method == 'POST':
        fr_selfie = request.files['fr_selfie']
        if fr_selfie and allowed_file(fr_selfie.filename):
            filename = secure_filename(fr_selfie.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            fr_selfie.save(filepath)

            id_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            id_image = cv2.imread(id_file_path)
            fr_selfie_image = cv2.imread(filepath)

            id_encoding = face_recognition.face_encodings(id_image)[0]
            fr_selfie_encoding = face_recognition.face_encodings(fr_selfie_image)[0]

            result = face_recognition.compare_faces([id_encoding], fr_selfie_encoding)
            similarity = face_recognition.face_distance([id_encoding], fr_selfie_encoding)

            return render_template('face_recognition_result.html', result=result, similarity=similarity)

    return render_template('face_recognition_selfie.html', filename=filename)

def face_recognition(id_payload, fr_selfie):
    id_image = base64.b64decode(id_payload['image'])
    id_image = np.frombuffer(id_image, np.uint8)
    id_image = cv2.imdecode(id_image, cv2.IMREAD_COLOR)

    fr_selfie_image = base64.b64decode(fr_selfie['image'])
    fr_selfie_image = np.frombuffer(fr_selfie_image, np.uint8)
    fr_selfie_image = cv2.imdecode(fr_selfie_image, cv2.IMREAD_COLOR)

    id_encoding = face_recognition.face_encodings(id_image)[0]
    fr_selfie_encoding = face_recognition.face_encodings(fr_selfie_image)[0]

    result = face_recognition.compare_faces([id_encoding], fr_selfie_encoding)
    similarity = face_recognition.face_distance([id_encoding], fr_selfie_encoding)

    return result, similarity

if __name__ == '__main__':
    app.run(debug=True)
