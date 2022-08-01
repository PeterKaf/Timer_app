# contains all functions and classes in different file for better visibility
import time
import csv
import numpy as np


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


