import telebot
import time
import json
from datetime import datetime, timedelta
import os

API_TOKEN = os.getenv("API_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = telebot.TeleBot(API_TOKEN)

def get_local_time():
    return (datetime.utcnow() + timedelta(hours=3)).strftime("%H:%M")

def load_messages():
    with open("messages.json", "r", encoding="utf-8") as f:
        return json.load(f)

def send_reminders():
    already_sent = set()
    while True:
        now = get_local_time()
        messages = load_messages()
        if now in messages and now not in already_sent:
            bot.send_message(CHAT_ID, messages[now])
            print(f"[{now}] Mesaj gönderildi: {messages[now]}")
            already_sent.add(now)
        time.sleep(30)

if __name__ == "__main__":
    send_reminders()
