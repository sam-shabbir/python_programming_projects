# Alarm Clock

# LINK: ALARM CLOCK SOUNDS
# https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
# Download a sound from the link above and save it next to this file as "alarm.mp3"
# pip install playsound==1.2.2

import os
import time # module

#ansi characters and colors
CLEAR = "\033[2J" # Clears the terminal screen
CLEAR_AND_RETURN = "\033[H" # Moves the cursor to the top-left corner (so the countdown overwrites itself)

def alarm(seconds):
    time_elapsed = 0 # FIX: was `time.elapsed = 0`, which tried to attach a value to the time MODULE instead of creating a variable

    print (CLEAR)

    while time_elapsed < seconds: # FIX: same variable name as above (was time.elapsed)
        time.sleep(1) # wait for 1 second
        time_elapsed +=1 # FIX: was misspelled `time_elpased`

        time_left = seconds - time_elapsed
        minutes_left = time_left //60
        seconds_left = time_left % 60 # mod operator gives the remainder of the division

        # FIX: was {minutes_left: 02d} - the space inside the format spec adds a stray space before the number
        print (f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") # :02d formats the number to be at least 2 digits, padding with zeros if necessary

    play_sound()

def play_sound():
    # FIX: if alarm.mp3 or the playsound package is missing, beep instead of crashing
    if os.path.exists("alarm.mp3"):
        try:
            from playsound import playsound
            playsound("alarm.mp3")
            return
        except ImportError:
            pass
    print("\a⏰ Time's up! ⏰") # "\a" makes the terminal beep

# FIX: these lines were indented inside alarm(), so they never ran - nothing ever called alarm() in the first place.
# They belong at the top level of the file.
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait?:  "))
total_seconds = minutes * 60 + seconds # FIX: was minutes * 60 * seconds - we ADD the extra seconds, not multiply
alarm(total_seconds) # FIX: was alarm(10), which ignored what the user typed
