from flask import Flask, render_template, request, send_file
import random
import string
import csv
import os

app = Flask(__name__)

# Directory to save generated password files
PASSWORD_DIR = os.path.join(app.root_path, 'passwords')
os.makedirs(PASSWORD_DIR, exist_ok=True)

# Function to generate random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+~`|}{[]:;?><,./-="
    return ''.join(random.choice(characters) for _ in range(length))

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate password and save to CSV
@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    password = generate_password(length)
    file_path = os.path.join(PASSWORD_DIR, 'passwords.csv')

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([password])

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
