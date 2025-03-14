import time
import tweepy
import os
import sys

print("🔵 התחלה!", flush=True)

# הגדרת משתני סביבה מתוך ה-Environment ב-Render
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# בדיקה שהמידע נטען
if not all([BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    print("❌ שגיאה: אחד או יותר מהטוקנים חסרים. בדוק את הגדרות ה-Environment שלך!", flush=True)
    exit(1)

try:
    # אימות עם Twitter API
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    print("✅ התחברנו לטוויטר בהצלחה!", flush=True)

    # ניסיון לציוץ
    tweet_text = "test"
    api.update_status(status=tweet_text)
    print(f"✅ ציוץ פורסם: {tweet_text}", flush=True)

except Exception as e:
    print(f"❌ שגיאה בפרסום הציוץ: {e}", flush=True)

print("🚀 הבוט עלה בהצלחה ומריץ לולאה...", flush=True)

while True:
    print("✅ הבוט עדיין חי ומריץ לולאה...", flush=True)
    time.sleep(60)
