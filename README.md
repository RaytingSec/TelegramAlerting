tg-alerts
==============================

## Setup

1. First create a bot and copy it's token.

2. First use `blankdata.json` to create your `data.json`. Enter your Telegram username to other people aren't snooping on your alerts, and your bot's token.

3. Clone the repo and run the following inside:

```bash
virtualenv .venv
pip install -r requirements
python alertbot.py --run
```

## Sending Alerts

```bash
# General format
python alertbot.py --notify $message
# Example
python alertbot.py --notify "Hello, this is $(whoami). $(hostname) has been $(uptime -p)."
```
