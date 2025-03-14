import time
import tweepy
import os

print("🔵 התחלה!")

# הגדרת משתני סביבה מתוך ה-Environment ב-Render
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# בדיקה שהמידע נטען
if not all([BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    print("❌ שגיאה: אחד או יותר מהטוקנים חסרים. בדוק את הגדרות ה-Environment שלך!")
    exit(1)

try:
    # אימות עם Twitter API
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    print("✅ התחברנו לטוויטר בהצלחה!")

    # ניסיון לציוץ
    tweet_text = "ציוץ בדיקה מהבוט! 🚀"
    api.update_status(status=tweet_text)
    print(f"✅ ציוץ פורסם: {tweet_text}")

except Exception as e:
    print(f"❌ שגיאה בפרסום הציוץ: {e}")

print("🚀 הבוט עלה בהצלחה ומריץ לולאה...")

while True:
    print("✅ הבוט עדיין חי ומריץ לולאה...")
    time.sleep(60)
