# GitHub Webhook Event Tracker

## 📌 Project Overview

This project implements a GitHub webhook listener that captures repository events and displays them in a live dashboard.

The system listens for GitHub actions such as:

* Push Events
* Pull Request Events
* Merge Events (Bonus)

Whenever an event occurs in the repository, GitHub sends a webhook request to a Flask backend, which stores the event data in MongoDB.
The frontend UI automatically polls the backend every 15 seconds and displays the latest repository activity.

---

## 🏗️ Architecture

GitHub Repository (action-repo)
→ GitHub Webhook
→ Cloudflare Tunnel (Public URL)
→ Flask Webhook Server
→ MongoDB Database
→ Live Activity Dashboard (UI)

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** MongoDB
* **Frontend:** HTML + JavaScript
* **Integration:** GitHub Webhooks
* **Tunnel Service:** Cloudflare Tunnel
* **Version Control:** Git & GitHub

---

## 📂 Repository Structure

```
webhook-repo/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── templates/
    └── index.html
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone <your-webhook-repo-link>
cd webhook-repo
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Start MongoDB

Make sure MongoDB service is running locally.

```
mongod
```

---

### 5️⃣ Run Flask Server

```
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### 6️⃣ Expose Public URL (Cloudflare Tunnel)

```
cloudflared tunnel --url http://localhost:5000
```

Copy the generated public URL and configure it in GitHub Webhooks:

```
https://<public-url>/webhook
```

---

## 🔗 Webhook Configuration

Configure webhook in **action-repo**:

* Payload URL → `https://<public-url>/webhook`
* Content Type → `application/json`
* Events:

  * Push
  * Pull Requests

---

## 📊 Event Formats

### Push Event

```
{author} pushed to {branch} on {timestamp}
```

### Pull Request Event

```
{author} submitted a pull request from {source_branch} to {target_branch} on {timestamp}
```

### Merge Event

```
{author} merged branch {source_branch} to {target_branch} on {timestamp}
```

---

## 🔄 Auto Refresh Logic

The frontend polls the backend every **15 seconds** to fetch only new events from MongoDB and updates the dashboard dynamically.

---

## 🎥 Demo

Demo walkthrough video:
(Add Google Drive link here)

---

## 👨‍💻 Author

Keerthi
GitHub: https://github.com/keerthi25-ops

---

## ✅ Assignment Completion

This implementation satisfies all requirements of the TechStacx Developer Assessment:

* ✔ GitHub Webhook Integration
* ✔ Flask Webhook Endpoint
* ✔ MongoDB Storage
* ✔ Auto-updating UI
* ✔ Push Events
* ✔ Pull Request Events
* ✔ Merge Events (Bonus)
