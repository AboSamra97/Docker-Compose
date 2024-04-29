# app.py

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Route to render the main page with data table
@app.route('/')
def index():
    try:
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Retrieve all data from the students table
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        
        # Close the connection
        conn.close()

        return render_template('index.html', students=students)
    except Exception as e:
        return str(e)

# Route to render the insert form
@app.route('/insert_form')
def insert_form():
    return render_template('insert.html')

# Route to handle insertion of data into the database
@app.route('/insert', methods=['POST'])
def insert_data():
    try:
        # Extract data from the request
        name = request.form.get('name')
        student_id = request.form.get('student_id')
        gpa = request.form.get('gpa')

        if not (name and student_id and gpa):
            return jsonify({'error': 'Missing data'}), 400

        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Insert data into the students table
        cursor.execute("INSERT INTO students (name, student_id, gpa) VALUES (?, ?, ?)", (name, student_id, gpa))
        
        # Commit the transaction
        conn.commit()
        
        # Close the connection
        conn.close()

        return jsonify({'message': 'Data inserted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to handle deletion of data from the database
@app.route('/delete', methods=['POST'])
def delete_data():
    try:
        # Extract data from the request
        student_id = request.form.get('student_id')

        if not student_id:
            return jsonify({'error': 'Missing student_id'}), 400

        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Delete data from the students table
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        
        # Commit the transaction
        conn.commit()
        
        # Close the connection
        conn.close()

        return jsonify({'message': 'Data deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
