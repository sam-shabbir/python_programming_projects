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

### `practice_problems/`
Short exercises on lists, strings, loops, dictionaries, sets, file I/O, and an introduction to classes. Each file states the problem at the top.

### `data_analytics_luke_barousse/`
Notebooks from Luke Barousse's *Python for Data Analytics* course:

- **01_python_basics**: variables, data types, control flow, functions, classes, NumPy, and intro pandas/matplotlib
- **02_advanced_pandas_and_visualisation**: cleaning, pivot tables, merging, `apply`, `explode`, matplotlib charts, and seaborn
- **03_capstone_job_market_eda**: exploratory analysis of data-job postings covering skill demand, skill trends, salaries, and the best skills to learn

> Cells marked **🪲 Debugging** fail on purpose. The course uses them to show common errors.

## Running

```bash
pip install pandas matplotlib seaborn datasets pygame pytube schedule windows-curses
python mini_projects/13_Password_Generator.py
```

Open the notebooks with Jupyter or VS Code.
