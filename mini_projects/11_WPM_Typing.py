# LINK: https://docs.python.org/3/howto/curses.html
# -----------------curses--------------------------

import curses # module for creating text-based user interfaces in the terminal. It provides functions to control the terminal screen, handle user input, and manage colors and text attributes.
from curses import wrapper # wrapper is a function that initializes the curses application, calls the provided main function, and then cleans up the terminal after the main function exits.
# It ensures that the terminal is properly restored to its original state even if an error occurs during the execution of the main function.
import time # module for working with time-related functions. In this code, it is used to measure the elapsed time during the typing test to calculate the words per minute (WPM) score.
import random # module for generating random numbers and making random selections. In this code, it is used to randomly select a line of text from a file to be used as the target text for the typing test.

def start_screen(stdscr): # stdscr/standard screen is the window object that curses uses to control the terminal
	stdscr.clear() # Clear the screen to start afresh
	stdscr.addstr("Welcome to the Speed Typing Test!") # Add a string to the screen at the current cursor position
	stdscr.addstr("\nPress any key to begin!") # Add another string on a new line (because of \n) to prompt the user to start the test
	stdscr.refresh() # Refresh the screen to update it with the new content. This is necessary after making changes to the screen to ensure they are displayed.
	stdscr.getkey() # Wait for the user to press a key before proceeding. This allows the user to read the welcome message before starting the test.

def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target) # Display the target text on the first line of the screen. The target text is the text that the user is supposed to type during the test.
	stdscr.addstr(1, 0, f"WPM: {wpm}") # Display the target text on the first line and the WPM score on the second line (line index 1).
	# The WPM score is formatted as a string using an f-string for easy readability.

	for i, char in enumerate(current): # Loop through each character in the current text (the text the user has typed so far) using enumerate to get both the index (i) and the character (char).
		correct_char = target[i] # Get the corresponding character from the target text at the same index (i) to compare it with the character typed by the user.
		color = curses.color_pair(1) # Initialize the color variable to the color pair for correct characters (green). This assumes that the character is correct by default.
		if char != correct_char: # If the character typed by the user does not match the corresponding character in the target text, change the color variable to the color pair for incorrect characters (red).
			color = curses.color_pair(2) # This will allow us to display incorrectly typed characters in red, providing visual feedback to the user about their mistakes.

		stdscr.addstr(0, i, char, color) # Add the character typed by the user to the screen at the position corresponding to its index (i) on the first line (line index 0). 
		#The color of the character is determined by whether it is correct or incorrect, as set in the previous steps.

def load_text(): # This function is responsible for loading the target text for the typing test. It reads lines from a file called "text.txt" and randomly selects one line to be used as the target text.
	with open("text.txt", "r") as f: # Open the file "text.txt" in read mode. The with statement ensures that the file is properly closed after we are done with it.
		lines = f.readlines() # Read all lines from the file and store them in a list called lines. Each element of the list is a line from the file, including the newline character at the end of each line.
		return random.choice(lines).strip() # Use random.choice() to select a random line from the lines list.
	# The strip() method is called on the selected line to remove any leading or trailing whitespace, including the newline character, ensuring that the target text is clean and ready for the typing test.

def wpm_test(stdscr): # The main function that runs the typing test.
	# It loads the target text, initializes the current text and WPM score, and enters a loop to handle user input and update the display until the test is completed.	
	target_text = load_text() # Load the target text for the typing test by calling the load_text() function, which reads lines from a file and randomly selects one to be used as the target text.
	current_text = [] # every charater is stored in a list, so we can easily compare it to the target text and update the display accordingly.
	wpm = 0 # starting points for the WPM score, which will be calculated based on the number of characters typed and the elapsed time.
	start_time = time.time() # Record the start time of the test using time.time(), which returns the current time in seconds since the epoch.
	# This will be used to calculate the elapsed time during the test.
	stdscr.nodelay(True) # Set the getkey() function to non-blocking mode using stdscr.nodelay(True). This allows the program to continue running and updating the display
	# even if the user has not pressed a key, enabling real-time feedback on the WPM score and the current text being typed.

	while True:
		time_elapsed = max(time.time() - start_time, 1) # time.time is time since epoc 1970 in seconds. By subtracting the start time from the current time, we get the elapsed time in seconds.
		# The max function is used to ensure that the elapsed time is at least 1 second to avoid division by zero when calculating the WPM score.
		# This means that even if the user types very quickly and the elapsed time is less than 1 second, we will still use 1 second for the WPM calculation to prevent errors.
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5) # Calculate the WPM score based on the number of characters typed (len(current_text)), the elapsed time in minutes (time_elapsed / 60), and the standard definition of a word as 5 characters.
		 # The formula for WPM is: (number of characters / 5) / (elapsed time in minutes). The result is rounded to the nearest whole number using round() for a cleaner display.

		stdscr.clear() # Clear the screen at the beginning of each loop iteration to update the display with the latest target text, current text, and WPM score.
		display_text(stdscr, target_text, current_text, wpm) # Call the display_text() function to update the screen with the target text, the current text typed by the user, and the current WPM score.
		# This function handles the visual representation of the typing test.
		stdscr.refresh() # Refresh the screen to apply the changes made by display_text() and show the updated target text, current text, and WPM score to the user.

		if "".join(current_text) == target_text:# convert list to a string, char sep by nothing, and compare it to the target text. If they match, it means the user has completed typing the target text correctly.
			stdscr.nodelay(False) # Set nodelay back to False to make getkey() blocking again, allowing the user to see the final WPM score and the completed text before exiting the test.
			break

		try:
			key = stdscr.getkey() # Wait for the user to press a key and store it in the variable key. This function will raise an exception if no key is pressed, which is why it is wrapped in a try-except block.
		except: # If no key is pressed, the getkey() function will raise an exception. In this case, we catch the exception and simply continue the loop.
			continue

		if ord(key) == 27: # Check if the key pressed is the Escape key (ASCII code 27). If it is, exit the loop and end the test. ordinal vlaue of the key is obtained using ord() function.
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"): # Check if the key pressed is the Backspace key (ASCII code 127). If it is, remove the last character from the current text. 
			#The getkey() function can return different representations for the Backspace key depending on the terminal, so we check for multiple possible values.
			#why \b and \x7f? Because different terminals may represent the Backspace key differently. Some terminals may return "KEY_BACKSPACE", while others may return the ASCII backspace character ('\b') or the delete character ('\x7f').
			# # By checking for all three possibilities, we ensure that the Backspace functionality works correctly across different terminal environments.	
			if len(current_text) > 0: # why len(current_text) > 0? This check is necessary to prevent an error that would occur if we try to pop from an empty list.
				#If the current_text list is empty and we attempt to pop, it would raise an IndexError.
				# By checking that the length of current_text is greater than 0, we ensure that there is at least one character to remove before calling pop().
				current_text.pop() # will remove the last character from the current text list, allowing the user to correct their input 
		elif len(current_text) < len(target_text): # Check if the length of the current text is less than the length of the target text.
			# This ensures that the user cannot type more characters than the target text, which would not make sense in the context of a typing test.
			current_text.append(key) # If the key pressed is not the Backspace key and the current text is still shorter than the target text, append the key to the current text list.


def main(stdscr): # The main function that will be passed to the wrapper. It initializes the curses application and contains the main loop for the typing test.
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # Initialize a color pair for correct characters (1) with green text on a black background. 
	# This color pair will be used to display correctly typed characters in green.
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # Initialize a color pair for incorrect characters (2) with red text on a black background.
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) # Initialize a color pair for default text (3) with white text on a black background. 
	# This can be used for displaying the target text and WPM score in the default color.

	start_screen(stdscr)
	while True:
		wpm_test(stdscr)
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()
		
		if ord(key) == 27: # Check if the key pressed is the Escape key (ASCII code 27). If it is, exit the loop and end the program.
			break

wrapper(main) # Call the wrapper function with the main function as an argument. This will initialize the curses application, run the main function, and handle cleanup after the main function exits.