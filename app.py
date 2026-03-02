from flask import Flask, request, jsonify,render_template
from pymongo import MongoClient
from datetime import datetime

print("APP FILE LOADED")   # Debug check

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["github"]
collection = db["events"]

# HOME ROUTE
from flask import render_template

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

#  WEBHOOK ROUTE
@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json
    event = request.headers.get("X-GitHub-Event")

    author = data["sender"]["login"]
    timestamp = datetime.utcnow().isoformat()

    # PUSH EVENT
    if event == "push":
        branch = data["ref"].split("/")[-1]

        collection.insert_one({
            "type": "push",
            "author": author,
            "to_branch": branch,
            "timestamp": timestamp
        })

    # PULL REQUEST EVENT
    elif event == "pull_request":

        pr = data["pull_request"]

        collection.insert_one({
            "type": "pull_request",
            "author": author,
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": timestamp
        })

        # MERGE EVENT
        if pr["merged"]:

            collection.insert_one({
                "type": "merge",
                "author": author,
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": timestamp
            })

    return jsonify({"message": "Webhook received"})
@app.route("/events")
def get_events():
    events = list(collection.find({}, {"_id": 0}).sort("timestamp", -1))
    return jsonify(events)


if __name__ == "__main__":
    app.run(debug=True, port=5000)