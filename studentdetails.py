import sqlite3

from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
app = Flask(__name__)
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS studentdetails(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, regNo TEXT )")
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    dept = request.form['dept']
    regNo = request.form['regNo']
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO studentdetails(name, dept, regNo) VALUES (?, ?, ?)', (name, dept, regNo))
    conn.commit()
    conn.close()
    return 'DATA BASE SUBMITTED SUCCESSFULLY!'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
