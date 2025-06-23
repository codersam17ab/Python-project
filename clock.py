import datetime
import time
import sys
import os
import tkinter as tk

# Check the operating system
if sys.platform == "win32":
    import winsound


def beep():
    if sys.platform == "win32":
        winsound.Beep(2000, 1000)  # Frequency = 1000 Hz, Duration = 500 ms
    else:
        os.system("echo -e '\a'")  # System beep for Linux/macOS


def set_alarm(alarm_time, alarm_sound):
    print(f"Alarm set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            beep()  # Make a beep sound
            break
        time.sleep(1)  # Check time every second


def update_clock():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)


if __name__ == "__main__":
    # Hardcoded alarm time to avoid input() issues in sandboxed environments
    alarm_time = "11:05:00"  # Change this to the desired alarm time

    # Create digital clock GUI
    root = tk.Tk()
    root.title("Digital Clock")
    clock_label = tk.Label(root, font=("Garamond", 58), fg="red")
    clock_label.pack()
    update_clock()

    # Run alarm in a separate thread
    import threading

    alarm_thread = threading.Thread(target=set_alarm, args=(alarm_time, None))
    alarm_thread.daemon = True
    alarm_thread.start()

    root.mainloop()
