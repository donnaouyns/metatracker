import os
import time
import ctypes
from datetime import datetime, timedelta

class MetaTracker:
    def __init__(self, sleep_hour=23, sleep_minute=0, wake_hour=7, wake_minute=0):
        self.sleep_time = timedelta(hours=sleep_hour, minutes=sleep_minute)
        self.wake_time = timedelta(hours=wake_hour, minutes=wake_minute)
        self.system_idle_time = 0
        self.idle_threshold = 300  # seconds

    def get_idle_duration(self):
        class LASTINPUTINFO(ctypes.Structure):
            _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

        lii = LASTINPUTINFO()
        lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
        ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
        millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
        return millis / 1000.0

    def should_sleep(self):
        now = datetime.now()
        current_time = timedelta(hours=now.hour, minutes=now.minute)
        return self.sleep_time <= current_time <= self.wake_time

    def schedule_sleep(self):
        if self.should_sleep():
            idle_duration = self.get_idle_duration()
            if idle_duration >= self.idle_threshold:
                os.system("shutdown /h")
                return True
        return False

    def start(self):
        print("MetaTracker is running...")
        while True:
            if self.schedule_sleep():
                print("System is going to sleep.")
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    tracker = MetaTracker()
    tracker.start()