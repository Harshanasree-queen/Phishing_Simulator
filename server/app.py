from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

user_responses = []

@app.route('/')
def index():
    # Pass the current time to the template
    return render_template('index.html', now=datetime.now())

@app.route('/response', methods=['POST'])
def response():
    action = request.form.get('action')
    timestamp = request.form.get('timestamp')
    user_responses.append({
        'action': action,
        'timestamp': timestamp
    })
    return redirect(url_for('index'))

@app.route('/results')
def results():
    return render_template('results.html', responses=user_responses)

if __name__ == '__main__':
    app.run(debug=True)
