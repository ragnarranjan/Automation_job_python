# app.py

from flask import Flask
from scheduler_config import start_scheduler

app = Flask(__name__)

# Start the scheduler when the app starts
scheduler = start_scheduler()

@app.route('/')
def home():
    return "Flask app with APScheduler is running."

if __name__ == '__main__':
    app.run(debug=True)
