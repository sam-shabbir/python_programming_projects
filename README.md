# Python Programming Projects

This repo collects the Python work I've done while learning the language: small games and tools, a set of practice problems, and notebooks from a data analytics course.

## Contents

### `mini_projects/`
Small command-line and GUI programs.

| Project | What it does | Extra requirements |
|---|---|---|
| Quiz Game | Multiple-choice quiz with a score at the end | none |
| Random Number Guessing Game | Guess a random number, with higher/lower hints | none |
| Rock Paper Scissors | Play against the computer and keep a running score | none |
| Choose Your Own Adventure | Text adventure with branching choices | none |
| Black Jack Project | Blackjack against a dealer, built with classes | none |
| 08 Timed Math Challenge | 10 timed arithmetic problems | none |
| 11 WPM Typing | Terminal typing-speed test (reads `text.txt`) | `windows-curses` on Windows |
| 12 Alarm Clock | Countdown timer, accepts input like `2m` or `30s` | none |
| 13 Password Generator | Secure passwords with an entropy score | none |
| 17 YouTube Downloader | Downloads a video to a folder you pick | `pytube` |
| 18 Auto Folder Backup | Copies a folder into a dated backup every day | `schedule` (edit the paths first) |
| 20 Advanced Aim Trainer | Pygame target-clicking game | `pygame` |
| 21 Advanced Get Game Data | Finds, copies, and compiles game folders, then writes metadata | Go toolchain |
| Quiz Game 2 | Computer-acronyms quiz with a percentage score | none |
| 06 PIG Dice Game | 2–4 player dice game where rolling a 1 loses your turn's points; first to 50 wins | none |
| 07 Madlibs Generator | Fills the `<blanks>` in `story.txt` with your words | none |
| 09 Turtle Racing | Races 2–10 randomly moving turtles | none (uses built-in `turtle`) |
| Slot Machine | Deposit, bet on 1–3 lines, and spin | none |
| 12A Alarm Clock With Sound | Countdown that plays `alarm.mp3`, or beeps if the file is missing | `playsound==1.2.2` (optional) |
| 14 Shortest Path Finder | Animated breadth-first search through a maze | `windows-curses` on Windows |
| 19 MasterMind | Guess the 4-colour code in 10 tries | none |
| Password Manager | Saves passwords encrypted with a key file | `cryptography` |
| 16 Currency Converter | Live exchange rates and conversions from the free Frankfurter API (ECB data, no key needed) | `requests` |
| HW Quiz Game (loop version) | Quiz Game rewritten to store questions in a list and ask them in one loop | none |
| Image Filter | Command-line tool: `python Image_Filter.py photo.jpg blur` (also sharpen, contour, edges, emboss, grayscale, invert, mirror) | `pillow` |
| CS2 Aim Trainer Game | Saves a 3D (Three.js) Counter-Strike-style reaction trainer as HTML and opens it in your browser | none |
| CS50 OpenAI First Call | Sends one prompt to the OpenAI API | `openai`, plus an `OPENAI_API_KEY` environment variable |

Lines marked `# FIX:` show where I later corrected a bug, with a short note on what was wrong.

### `practice_problems/`
Short exercises on lists, strings, loops, dictionaries, sets, file I/O, and an introduction to classes. Each file states the problem at the top.

### `data_analytics_course_notebooks/`
Notebooks from a Python for Data Analytics course:

- **01_python_basics**: variables, data types, control flow, functions, classes, NumPy, and intro pandas/matplotlib
- **02_advanced_pandas_and_visualisation**: cleaning, pivot tables, merging, `apply`, `explode`, matplotlib charts, and seaborn
- **03_capstone_job_market_eda**: the capstone project, now with its own repo and a write-up: **[Data_Analytics_Job_Market_EDA](https://github.com/sam-shabbir/Data_Analytics_Job_Market_EDA)**

> Cells marked **🪲 Debugging** fail on purpose. The course uses them to show common errors.
>
> Course material: Luke Barousse's Python for Data Analytics.

## Running

```bash
pip install pandas matplotlib seaborn datasets pygame pytube schedule windows-curses cryptography openai requests pillow
python mini_projects/13_Password_Generator.py
```

Open the notebooks with Jupyter or VS Code.
