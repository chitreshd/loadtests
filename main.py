# This is a sample Python script.

# Press ⇧⌘F11 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
from utils import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⇧⌘B to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = datetime.now().timestamp()
    print("timestamp =", int(start_time))
    print_hi('PyCharm')
    now = int(datetime.now().timestamp())
    payload = email_payload(now, emails=["abc@gmail.com", "def@gmail.com"])
    print_hi('initialized')
    print(payload)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
