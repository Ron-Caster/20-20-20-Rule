import time
import ctypes
import winsound
def beep():
    # Play a beep sound
    winsound.Beep(440, 1000)  # Adjust the frequency and duration as desired
def follow_20_20_20_rule():
    while True:
        # Wait for 20 minutes
        for i in range(20, 0, -1):
            print(f"Next break in {i} minutes", end='\r')
            time.sleep(60)
         # Play the beep sound
        beep()
         # Display a message box
        ctypes.windll.user32.MessageBoxW(0, "Time for a 20-second break!", "Break Reminder", 0x40)
 # Call the function to start following the 20:20:20 rule
follow_20_20_20_rule()