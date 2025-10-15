import os
from zipfile import ZipFile

base_dir = "flask_app"
templates_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(base_dir, "static")

files = {
    os.path.join(base_dir, "app.py"): '''from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/records')
def records():
    dummy_data = [{'id': 1, 'name': 'Item A'}, {'id': 2, 'name': 'Item B'}]
    return render_template('records.html', records=dummy_data)

@app.route('/add')
def add():
    return render_template('form.html', action='Add', name='')

@app.route('/edit/<int:id>')
def edit(id):
    return render_template('form.html', action='Edit', name='Item {}'.format(id))

if __name__ == '__main__':
    app.run(debug=True)
''',

    os.path.join(base_dir, "requirements.txt"): "flask\n",

    os.path.join(templates_dir, "login.html"): '''<!DOCTYPE html>
<html>
<head><title>Login</title><link rel="stylesheet" href="/static/styles.css"></head>
<body>
<h2>Login</h2>
<form method="POST">
  <input name="username" placeholder="Username"><br>
  <input name="password" type="password" placeholder="Password"><br>
  <button type="submit">Login</button>
</form>
</body></html>
''',

    os.path.join(templates_dir, "contact.html"): '''<!DOCTYPE html>
<html>
<head><title>Contact Us</title><link rel="stylesheet" href="/static/styles.css"></head>
<body>
<h2>Contact Us</h2>
<form method="POST">
  <input name="name" placeholder="Name"><br>
  <input name="email" placeholder="Email"><br>
  <textarea name="message" placeholder="Message"></textarea><br>
  <button type="submit">Send</button>
</form>
</body></html>
''',

    os.path.join(templates_dir, "records.html"): '''<!DOCTYPE html>
<html>
<head><title>Records</title><link rel="stylesheet" href="/static/styles.css"></head>
<body>
<h2>Records</h2>
<a href="/add">Add New</a>
<table border="1">
  <tr><th>ID</th><th>Name</th><th>Actions</th></tr>
  {% for r in records %}
  <tr>
    <td>{{ r.id }}</td>
    <td>{{ r.name }}</td>
    <td>
      <a href="/edit/{{ r.id }}">Edit</a> |
      <a href="#">Delete</a>
    </td>
  </tr>
  {% endfor %}
</table>
</body></html>
''',

    os.path.join(templates_dir, "form.html"): '''<!DOCTYPE html>
<html>
<head><title>{{ action }} Item</title><link rel="stylesheet" href="/static/styles.css"></head>
<body>
<h2>{{ action }} Item</h2>
<form method="POST">
  <input name="name" placeholder="Item name" value="{{ name }}"><br>
  <button type="submit">{{ action }}</button>
</form>
</body></html>
''',

    os.path.join(static_dir, "styles.css"): '''body {
  font-family: 'Poppins', 'Open Sans', sans-serif;
  margin: 20px;
}
input, textarea {
  margin-bottom: 10px;
  padding: 5px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
td, th {
  padding: 10px;
  border: 1px solid #ccc;
}
'''
}

# Create the folder structure and write files
for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Zip the project folder
with ZipFile("flask_app_frontend.zip", "w") as zipf:
    for folder, _, filenames in os.walk(base_dir):
        for filename in filenames:
            filepath = os.path.join(folder, filename)
            zipf.write(filepath, os.path.relpath(filepath, base_dir))

print("ZIP file 'flask_app_frontend.zip' created successfully!")
