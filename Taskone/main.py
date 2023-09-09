from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import pytz
import os



app = Flask(__name__)
app.config['SECRET_key'] = os.environ.get('s_key')

@app.route('/')
def home():
    return jsonify(response='Hello')

@app.route('/api')
def api():
    time = datetime.now(pytz.UTC)
    month = datetime.now(pytz.UTC).strftime('%A')

    plus_time = time - timedelta(minutes=2)
    minus_time = time + timedelta(minutes=2)

    plus_time = plus_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    minus_time = minus_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    time = datetime.now(pytz.UTC).strftime('%Y-%m-%dT%-H:%M:%SZ')

    # if time == minus_time:
        return jsonify(slack_name=request.args.get('slack_name'),
                       current_day=month,
                       utc_time=time,
                       track=request.args.get('track'),
                       github_file_url='https://github.com/Am0du/HNG-task/Taskone/main.py',
                       github_repo_url='https://github.com/username/repo',
                       status_code=200), 200
    # elif time == plus_time:
    #     return jsonify(slack_name=request.args.get('slack_name'),
    #                    current_day=month,
    #                    utc_time=plus_time,
    #                    track=request.args.get('track'),
    #                    github_file_url='https://github.com/Am0du/HNG-task/Taskone/main.py',
    #                    github_repo_url='https://github.com/username/repo',
    #                    status_code=200), 200
    # else:
    #     return jsonify(slack_name=request.args.get('slack_name'),
    #                    current_day=month,
    #                    utc_time=time,
    #                    track=request.args.get('track'),
    #                    github_file_url='https://github.com/Am0du/HNG-task/Taskone/main.py',
    #                    github_repo_url='https://github.com/username/repo',
    #                    status_code=200), 200


if __name__ == '__main__':
    app.run(debug=True)
