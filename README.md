# Ferrari F1 Win Tracker Bot

## 📌 Overview
Automated Twitter bot that tracks the number of days since Ferrari’s last Formula 1 race win and posts daily updates.

The bot runs on a scheduled basis and publishes updates automatically without manual intervention.

---

## 🚀 Features
- Automatically posts daily updates to Twitter (X)
- Tracks the number of days since Ferrari’s last F1 win
- Runs continuously using scheduled automation
- No manual interaction required after setup

---

## 🛠 Tech Stack
- Python 
- Twitter (X) API
- Scheduler via GitHub Actions

---

## ⚙️ How It Works

1. Retrieves or calculates the number of days since Ferrari’s last win
2. Formats a tweet message
3. Sends the tweet via Twitter API
4. Runs automatically once per day via scheduler

---

## 🧠 Key Concepts Demonstrated
- API integration (Twitter/X API)
- Task scheduling / automation
- Background jobs
- Handling real-world API constraints (rate limits, auth, etc.)
