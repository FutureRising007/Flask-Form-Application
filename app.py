from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_data.db'  # Change the database name here
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    college = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    stream = db.Column(db.String(50), nullable=False)
    graduation_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Student(name={self.name}, college={self.college}, phone_number={self.phone_number}, stream={self.stream}, graduation_year={self.graduation_year})"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        phone_number = request.form.get('phone_number', '')  # Use get() with default value
        stream = request.form['stream']
        graduation_year = int(request.form['graduation_year'])
        student = Student(name=name, college=college, phone_number=phone_number, stream=stream, graduation_year=graduation_year)
        db.session.add(student)
        db.session.commit()

    students = Student.query.all()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
