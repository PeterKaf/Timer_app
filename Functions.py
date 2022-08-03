# contains all functions and classes in different file for better visibility
import time
import csv
import numpy as np
from tkinter import *

w = 0


class Timer:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def load_instructions(self):
        with open(self.path, newline='') as f:
            reader = csv.reader(f)
            instructions = np.array(list(reader))
        return instructions

    def start_timer(self, instructions):
        instructions_time = instructions[:, 0]
        instructions_time = instructions_time.astype(np.int)
        instructions_comment = instructions[:, 1]
        while True:
            if input("Press y to start counting or any key to stop") == "y":
                for x in range(len(instructions)):
                    time.sleep(instructions_time[x])
                    print(instructions_comment[x])
            else:
                print("Counting aborted")
                break

    def gui(self, instructions):
        instructions_time = instructions[:, 0]
        instructions_time = instructions_time.astype(np.int)
        instructions_comment = instructions[:, 1]
        root = Tk()  # window init
        # GUI
        l = Label(root)  # creating empty label without text
        l.pack()

        def call():
            global w
            if w <= len(instructions)-1:  # if it is in the range of the list
                l.config(text=instructions_comment[w], font=("Arial", 50),
                         fg="white", bg="black", width=200, height=100)
                w += 1  # increase index number
                root.after(instructions_time[w]*1000, call)  # repeat the function after 2 seconds
            else:
                print('Done')  # if out of index range, then dont repeat

        call()  # call the function initially
        root.attributes("-fullscreen", True)
        root.attributes("-topmost", True)
        root.mainloop()
