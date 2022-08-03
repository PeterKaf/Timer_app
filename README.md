# Timer_app
This tool displays messages after certain amount of time. It takes input data as a 2 column csv file. First column is
responsible for time of the alert, while second contains the message to be displayed.

CSV file works like instructions for a program, it is only neccesary to edit this file to display different messages

It is working via tkinter GUI. Currently each new message replaces the old one.
# TO DO:
- Change GUI to either:
  - give all messages at the start and then only highlight the one valid for specific time
  - or add new message as a newline, while also keeping the old one
- GUI with start button or canvas instead of "y" keyboard input