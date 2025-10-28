from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

title = input("Enter the title of the reminder: ")
message = input("Enter the message of the reminder: ")

while True:
    try:
        minutes_str = input("Enter the time in minutes for the reminder: ")
        minutes = float(minutes_str)
        if minutes <= 0:
            print("Please enter a positive number for minutes.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

seconds = minutes * 60

print(f"\nReminder set! You will be notified in {minutes} minute(s).\n")
time.sleep(seconds)

toaster.show_toast(title, message, duration=10, threaded=True)
while toaster.notification_active(): time.sleep(0.1)