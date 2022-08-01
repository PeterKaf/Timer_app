import time
import Functions

Instance_1 = Functions.Timer("Test", "Sample.csv")
loaded = Instance_1.load_instructions()
Instance_1.start_timer(loaded)
