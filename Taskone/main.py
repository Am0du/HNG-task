from flask import Flask, jsonify, request
from datetime import datetime
import pytz
import os

time = datetime.now(pytz.UTC).strftime('%Y-%d-%HT%H:%M:%SZ')
month = datetime.now(pytz.UTC).strftime('%A')

app = Flask(__name__)
app.config['SECRET_key'] = os.environ.get('s_key')

@app.route('/')
def home():
    return jsonify(response='Hello')

@app.route('/api')
def api():
    return jsonify(slack_name=request.args.get('slack_name'),current_day=month, utc_time=time, track=request.args.get('track'),
                   github_file_url='https://github.com/Am0du/HNG-task/Taskone/main.py', github_repo_url='https://github.com/username/repo',
                   status_code=200), 200


if __name__ == '__main__':
    app.run(debug=True)
