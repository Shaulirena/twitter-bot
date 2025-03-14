import tweepy
import time
import os

# קריאת המפתחות מהסביבה
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# התחברות לטוויטר
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

print("🚀 הבוט עלה בהצלחה!")

# ציוץ ניסיון
try:
    api.update_status("זהו ציוץ ניסיון מהבוט האוטומטי שלי! 🐦 #בדיקה")
    print("✅ ציוץ פורסם בהצלחה!")
except Exception as e:
    print(f"❌ שגיאה בפרסום הציוץ: {e}")

# שמירה על ריצה
while True:
    print("✅ הבוט עדיין חי וממתין...")
    time.sleep(60)
