# webhook-repo
# 📡 Webhook Receiver App for GitHub Events

This project captures GitHub repository events (push, pull request, and optionally merge) via webhooks, stores them in MongoDB, and displays them in a real-time frontend UI.

## 🔗 Related Repositories

- **Webhook Sender Repo (`action-repo`)**: [GitHub Link Here](https://github.com/Vedantjaiswal4352/action-repo)
- **Webhook Receiver Repo (`webhook-repo`)**: This repo

---

## 📌 Features

- 📥 Receives GitHub Webhook events (Push & Pull Request)
- 💾 Stores event data in **MongoDB** using a clean schema
- 🔁 UI **polls every 15 seconds** to fetch and display live updates
- 🧾 Clean and minimal frontend displaying event activity in human-readable format
- ☁️ Works with both **MongoDB Atlas** (cloud) and local MongoDB

---

## 🔧 Tech Stack

- **Backend**: Flask (Python)
- **Database**: MongoDB (Atlas or Local)
- **Frontend**: HTML + JavaScript (vanilla)
- **Integration**: GitHub Webhooks, ngrok

---

## 🚀 How It Works

### 1. GitHub → Webhook
GitHub repository (`action-repo`) is configured with a webhook pointing to this Flask app.

### 2. Flask → MongoDB
The Flask server receives events and stores them in a MongoDB collection (`webhooks.events`).

### 3. MongoDB → UI
Frontend fetches events every 15 seconds via `/events` API and displays them dynamically.

---

## 🔁 Webhook Events Handled

### ✅ Push

{author} pushed to {to_branch} on {timestamp}

shell
Copy
Edit

### ✅ Pull Request
{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}

shell
Copy
Edit

### ✅ Merge
{author} merged branch {from_branch} to {to_branch} on {timestamp}

yaml
Copy
Edit

---

## 📂 Project Structure
webhook-repo/
├── app.py # Flask server and routes
├── templates/
│ └── index.html # Frontend UI
├── requirements.txt # Python dependencies
└── README.md # This file

yaml

---

## 💻 Setup Instructions
### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/webhook-repo.git
cd webhook-repo
```

### 2. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
### 3. Add the MongoDB URI in app.py
```bash
client = MongoClient("your-mongodb-connection-uri")
```
### 4. Run Flask Server
```bash
python app.py
```
### 5. Expose Flask via ngrok
```bash
ngrok http 5000
```
### 6. Add Webhook to GitHub
In action-repo > Settings > Webhooks:

Payload URL: https://<your-ngrok-url>/webhook

Content Type: application/json

Events: Push and Pull Requests


## 🧪 Testing
Push a commit or open a pull request in action-repo

The event appears in MongoDB and on the UI within 15 seconds

## 🙌 Author
Vedant Jaiswal

GitHub: @Vedantjaiswal4352



