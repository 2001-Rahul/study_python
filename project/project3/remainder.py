from win10toast import ToastNotifier
import time
import datetime
from playsound import playsound
import os

toaster = ToastNotifier()

title = input("Enter the title of the reminder: ")
message = input("Enter the message of the reminder: ")

# Find the sound file using an absolute path. This is a more compact way to do it.
script_dir = os.path.dirname(os.path.abspath(__file__))
possible_sound_files = ['notification.mpeg', 'Notification.mpeg', 'notification.MPEG']
SOUND_FILE = next((os.path.join(script_dir, f) for f in possible_sound_files if os.path.exists(os.path.join(script_dir, f))), None)

while True:
    try:
        time_str = input("Enter the time for the reminder (in HH:MM format, 24-hour clock): ")
        target_time = datetime.datetime.strptime(time_str, "%H:%M").time()

        # Get the current date and time
        now = datetime.datetime.now()

        # Combine today's date with the user's target time
        target_datetime = now.replace(hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0)

        # If the target time has already passed for today, set it for tomorrow
        if target_datetime < now:
            print("That time has passed for today. Setting reminder for tomorrow.")
            target_datetime += datetime.timedelta(days=1)

        seconds = (target_datetime - now).total_seconds()
        break
    except ValueError:
        print("Invalid time format. Please use HH:MM (e.g., 14:30).")

print(f"\nReminder set! You will be notified at {target_datetime.strftime('%Y-%m-%d %H:%M')}.\n")
time.sleep(seconds)

# Show the notification and then play the sound
toaster.show_toast(title, message, duration=10, threaded=True)

try:
    if SOUND_FILE:
        playsound(SOUND_FILE, block=False)
    else:
        print("Warning: Could not find a notification sound file in the script's directory.")
except Exception as e:
    print(f"Error playing sound: {e}")

while toaster.notification_active(): time.sleep(0.1)