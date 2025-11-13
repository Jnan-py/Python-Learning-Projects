from flask import Flask, request, render_template, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"

class Animal:
    def __init__(self, name):
        self._name = name  # encapsulated attribute

    def speak(self):
        return f"{self._name} makes a sound."

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        self._name = value


class Dog(Animal):
    def speak(self):  # polymorphism by overriding parent method
        return f"{self._name} says woof!"

    def fetch(self):
        return f"{self._name} is fetching the ball."


class Cat(Animal):
    def speak(self):  # polymorphism by overriding parent method
        return f"{self._name} says meow!"

    def scratch(self):
        return f"{self._name} is scratching the post."

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['txt', 'csv']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_animal', methods=['POST'])
def create_animal():
    name = request.form.get("name")
    a_type = request.form.get("animal_type")
    if a_type == "dog":
        animal = Dog(name)
    elif a_type == "cat":
        animal = Cat(name)
    else:
        return "Invalid animal type", 400

    return render_template('animal_created.html', animal=animal, a_type=a_type)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash("No file part in the request")
        return redirect(url_for('home'))
    file = request.files['file']
    if file.filename == '':
        flash("No selected file")
        return redirect(url_for('home'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            file.save(save_path)
            flash(f"File {filename} uploaded successfully.")
        except Exception as e:
            flash(f"Error saving file: {e}")
        return redirect(url_for('list_files'))
    else:
        flash("Invalid file type; only .txt and .csv allowed.")
        return redirect(url_for('home'))

@app.route('/files')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('file_list.html', files=files)

@app.route('/files/<filename>')
def display_file(filename):
    try:
        filename_safe = secure_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_safe)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return render_template('file_display.html', filename=filename_safe, content=content)
    except FileNotFoundError:
        flash(f"File {filename} not found.")
        return redirect(url_for('list_files'))
    except Exception as e:
        flash(f"Error reading file: {e}")
        return redirect(url_for('list_files'))

if __name__ == '__main__':
    app.run(debug=True)
