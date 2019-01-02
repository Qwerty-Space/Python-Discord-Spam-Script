import os
import time
import logging
import threading
import keyboard as k


should_spam = False

# Config
message_text = ":smiley:" # Text to send.  Default: ":smiley:"
msg_time = 0.8 # Time between messages (seconds).  Default: 0.8
wait_time = 5 # Time to wait between each run (seconds).  Default: 5
logging.basicConfig(level=logging.INFO) # Logging level.  Default: INFO


def spam():
    """Checks whether it should spam, and spams."""
    logging.debug("Spam thread started")
    while True:
        while should_spam:
            for _ in range(9):
                k.write(message_text, 0.02)
                k.send("enter")
                time.sleep(msg_time)
                if not should_spam:
                    break
            time.sleep(wait_time)
        time.sleep(1)

def main():
    """Toggles the spam switch."""
    global should_spam
    should_spam = not should_spam
    print(f"Spamming:  {should_spam}")

def cancel():
    """Stops spamming, and kills the process."""
    global should_spam
    should_spam = False
    print("Exiting in 3 seconds...")
    time.sleep(3)
    os._exit(1)


spam_thread = threading.Thread(target=spam)

if __name__ == "__main__":
    print("Welcome to the Discord Spam Script.\nPress <F3> to toggle spamming, and <F4> to exit.\n\n")
    k.add_hotkey("F3", main)
    k.add_hotkey("F4", cancel)
    if not spam_thread.is_alive():
        logging.debug("Starting the spam thread")
        spam_thread.start()
    while True:
        time.sleep(1)
