from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def serve_database():
    return send_file('database.db', mimetype='application/x-sqlite3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
