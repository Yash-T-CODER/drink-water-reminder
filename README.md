# 💧 Water Reminder Notification App

A simple Python script that sends **hourly desktop notifications** reminding you to stay hydrated — because good code needs a well-fueled brain!

---

## 🔔 Features

- Sends desktop notifications every hour
- Lightweight and runs silently in the background
- Motivational message with hydration reminder
- Cross-platform notification support via `notifypy`

---

## 🖼️ Sample Notification

> **Title:** Water Reminder  
> **Message:** Time to code, and time to hydrate! 💧 Keep your brain and body fueled with water.

---

## 🧠 How It Works

- Uses Python's `datetime` to track time
- Sends a notification using the `notifypy` library every 60 minutes
- Includes a motivational hydration message

---

## 📦 Requirements

- Python 3.6+
- [`notifypy`](https://pypi.org/project/notifypy/)

Install via pip:

```bash
pip install notifypy
