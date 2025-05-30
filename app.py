from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb+srv://YOUR_MONGO_USER:<YOUR_PASSWORD>@cluster0.uf4olsf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.webhooks # DB name
events = db.events # Collection name

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook',methods=["POST"])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')

    print(f"Received {event_type} events.")

    if event_type == "push":
        author = data['pusher']['name']
        branch = data['ref'].split('/')[-1]
        timestamp = datetime.utcnow().strftime("%d %B %Y - %I:%M %p UTC")

        events.insert_one({
            "type":"push",
            "author":author,
            "to_branch":branch,
            "timestamp":timestamp
        })
    elif event_type == "pull_request":
        pr = data["pull_request"]
        author = pr['user']['login']
        from_branch = pr['head']['ref']
        to_branch = pr['base']['ref']
        timestamp = datetime.utcnow().strftime("%d %B %Y - %I:%M %p UTC")

        events.insert_one({
            "type":"pull_request",
            "author":author,
            "from_branch":from_branch,
            "to_branch":to_branch,
            "timestamp":timestamp
        })

    return '',204

@app.route('/events',methods=["GET"])
def get_events():
    return jsonify(list(events.find({},{"_id":0})))

if __name__ == '__main__':
    app.run(port=5000,debug=True)
