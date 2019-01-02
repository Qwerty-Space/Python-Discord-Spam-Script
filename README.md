# Python-Discord-Spam-Script
This script is intended to be used with Pokécord to increase your Pokémon's levels, whilst bypassing Discord's rate limiting.
Rewritten version of [Discord-Spam-Script](https://github.com/Qwerty-Space/Discord-Spam-Script).

---

## Using this script to attack a server won't work because it sends too slowly, so don't bother

---

### What does it do?
This script will send a message every 800 milliseconds for a total of 9 messages.  Then it will wait 5 seconds and start again.  

### How do I make it say something else?
Change `:smiley:` on [line 9](discord_spam_script.py#L11) to something else.  Open an issue, or PM me on Discord/Telegram if you know me on there and would like some help.

### How do I use it?
* Install python
* Clone the repo
* `pip install -U -r requirements.txt`

Use <kbd>F3</kbd> to toggle spamming, and <kbd>F4</kbd> to exit.

### Dependencies
* \> Python 3.5 
* [keyboard](https://github.com/boppreh/keyboard)
