# Student Form Web Application

Welcome to the Student Form web application! This application allows users to submit student information using a form and displays the submitted data in a concise and user-friendly manner.

## Features

- Fill out the student form with details such as name, college, phone number, stream, and graduation year.
- Submit the form to save the student's information to the database.
- View the submitted student records in a well-organized table.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python (version 3.6 or later)
- Flask
- Flask SQLAlchem
- Flask Migrate

## Installation

1. Clone this repository to your local machine or download the source code as a ZIP file.
2. Navigate to the project directory using the command line.
3. Create a virtual environment (optional but recommended): `python3 -m venv venv` (replace `venv` with your preferred environment name).
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For macOS/Linux: `source venv/bin/activate`
5. Generate the requirements.txt file using the command `pip freeze > requirements.txt`
6. Install the required dependencies: `pip install -r requirements.txt`

## Configuration

1. Open the `app.py` file in a text editor.
2. Locate the following line of code: `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'`
3. Update the `data.db` part to the desired name of your SQLite database file.

## Running the Application

1. In the command line, navigate to the project directory.
2. Activate the virtual environment (if applicable).
3. Run `flask db init` after changing the name.
4. Run the command `flask db migrate -m "Initial Commit"
5. Then, run the command `flask db upgrade` to save changes in the Database.
6. Run the application: `python app.py`
7. Open a web browser and enter `http://localhost:5000` as the URL.
8. The Student Form web application should now be running, and you can start submitting and viewing student records.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
