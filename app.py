from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_marks():
    name = request.form['name']
    rollNum = request.form['rollNum']
    marks = int(request.form['marks'])
    
    if 90 <= marks <= 100:
        grade = 'S'
    elif 80 <= marks < 90:
        grade = 'A'
    elif 70 <= marks < 80:
        grade = 'B'
    elif 60 <= marks < 70:
        grade = 'C'
    else:
        grade = 'F'

    return render_template('student.html', name=name, rollNum=rollNum, marks=marks, grade=grade)

if __name__ == '_main_':
    app.run(debug=True)