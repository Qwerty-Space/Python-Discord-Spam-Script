import os
import time
import logging
import threading
import keyboard as k

logging.basicConfig(level=logging.INFO)
should_spam = False

def spam():
    logging.debug("Spam thread started")
    while True:
        while should_spam:
            for _ in range(9):
                k.write(":smiley:", 0.02)
                k.send("enter")
                time.sleep(0.8)
                if not should_spam:
                    break
            time.sleep(5)
        time.sleep(1)

def main():
    global should_spam
    should_spam = not should_spam
    print(f"Spamming:  {should_spam}")

def cancel():
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
