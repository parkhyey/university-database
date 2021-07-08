# Dependencies
from flask import Flask, render_template, json
import os
import database.db_connector as db

# Configuration
app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes
@app.route("/")
def root():
    return render_template("main.j2")

@app.route("/courses")
def courses():
    query = "SELECT * FROM courses;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("courses.j2", courses=results)

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)
# Use 'python app.py' or 'flask run' to run in terminal