import time
from notifypy import Notify
import datetime
def remind():
    notification = Notify()
    notification.title = "Water Reminder"
    notification.message = "Time to code, and time to hydrate! 💧 Keep your brain and body fueled with water. "
    
    notification.send()
while True:
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(f"The Time is {current_time}")
    remind()
    time.sleep(60*60)

