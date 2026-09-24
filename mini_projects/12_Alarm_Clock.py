# LINK: ALARM CLOCK SOUNDS
# https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203

import time  # For creating delays in the countdown
import sys   # For handling system operations

def countdown_timer(seconds): # why f? The 'f' in the function name 'countdown_timer' is not related to f-strings. It is simply part of the function name and does not have any special meaning in this context.
    # The function is designed to run a countdown timer for a specified number of seconds, and the 'f' is just a character in the name chosen by the programmer.
    """Runs a countdown timer for the given number of seconds."""
    try: # why try-except block? The try-except block is used to handle potential exceptions that may occur during the execution of the countdown timer, such as a KeyboardInterrupt
        # when the user wants to stop the timer prematurely.
        while seconds >= 0: # A while loop is used here to continuously update the countdown timer until it reaches zero.
            mins, secs = divmod(seconds, 60) # whats divmod? it divides the first number by the second and returns the quotient and remainder as a tuple **
            timer_display = f"{mins:02d}:{secs:02d}" # why f? f-strings are a way to format strings in Python. The expression inside the curly braces {} is evaluated and inserted into the string. 
            # In this case, {mins:02d} formats the minutes as a two-digit integer, padding with zeros if necessary, and {secs:02d} does the same for seconds.
            print(timer_display, end='\r')  # Overwrites the previous line
            time.sleep(1) # Why wait for 1 second? To create a real-time countdown effect, we need to pause the program for 1 second between each update of the timer display.
            # This allows the user to see the countdown in action as it decreases every second.
            seconds -= 1 # Why decrease seconds by 1? To create a countdown effect, we need to decrease the number of seconds remaining by 1 after each second has passed.
            # This way, the timer will count down from the initial value to zero, giving the user a visual representation of the time left until the alarm goes off.
        print("\n⏰ Time's up! ⏰")

    except KeyboardInterrupt: # Why handle KeyboardInterrupt? Handling KeyboardInterrupt allows the user to gracefully exit the countdown timer by pressing Ctrl+C.
        print("\n⏸ Countdown interrupted!")

def get_user_time(): # Why get user time? This function prompts the user to enter a time duration for the countdown timer, allowing them to specify how long they want the timer to run before the alarm goes off.
    """Prompts the user to enter time in minutes or seconds."""
    while True:
        try: # Why try-except block? The try-except block is used to handle potential errors that may occur when the user inputs their time. 
            # If the user enters an invalid format (e.g., not ending with 'm' or 's'), a ValueError will be raised when trying to convert the input to an integer.
            # By catching this exception, we can provide a user-friendly error message and prompt them to enter the time again without crashing the program.
            user_input = input("Enter time (e.g., '2m' for 2 minutes or '30s' for 30 seconds): ").strip().lower()
            # why strip and lower? The strip() method is used to remove any leading or trailing whitespace from the user's input, ensuring that the input is clean and doesn't contain unintended spaces.
            if user_input.endswith('m'): # Why check for 'm'? Checking if the input ends with 'm' allows us to determine if the user wants to set the timer in minutes.
                # If the input ends with 'm', we can then convert the numeric part of the input to seconds by multiplying it by 60, since there are 60 seconds in a minute.
                return int(user_input[:-1]) * 60  # Convert minutes to seconds
            elif user_input.endswith('s'): # Why check for 's'? Checking if the input ends with 's' allows us to determine if the user wants to set the timer in seconds.
                return int(user_input[:-1]) # If the input ends with 's', we can directly convert the numeric part of the input to an integer, as it already represents seconds.
            else:
                print("⚠️ Invalid format! Use 'Xm' for minutes or 'Ys' for seconds.")
        except ValueError: # Why catch ValueError? Catching ValueError allows us to handle cases where the user input cannot be converted to an integer (e.g., if they enter non-numeric characters before 'm' or 's').
            print("⚠️ Please enter a valid number followed by 'm' or 's'.")

def alert_user():
    """Alerts the user when the timer ends."""
    print("\n⏰ Time's up! ⏰")
    try:
        # Works on most systems
        for _ in range(3): # why _? The underscore (_) is a common convention in Python for a variable that is used as a placeholder when the actual value is not important.
            # amd why 3? The loop runs 3 times to create a series of beeps or alerts to ensure that the user notices when the timer ends. This can help to make the alert more effective and harder to miss.
            print("\a", end='')  # Terminal beep sound and end='' prevents adding a new line after each beep
            time.sleep(0.5) # why sleep for 0.5 seconds? Sleeping for 0.5 seconds between beeps creates a short pause, making the alert more noticeable and less overwhelming than a continuous beep.
            # It allows the user to distinguish each beep clearly, enhancing the effectiveness of the alert.
    except:
        pass # Ignore errors if sound doesn't play

if __name__ == "__main__": # Why use __name__ == "__main__"? This condition checks if the script is being run directly (as the main program) rather than imported as a module in another script.
    # If the script is run directly, the code inside this block will execute, allowing us to run the countdown timer and alert the user when the time is up. 
    # If the script is imported as a module, this block will not execute, preventing unintended behavior when the functions are used in other contexts.  
    print("===== ⏳ Countdown Timer ⏳ =====")
    user_seconds = get_user_time()
    countdown_timer(user_seconds)
    alert_user()