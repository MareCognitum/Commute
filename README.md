# Commute
Get traffic data from Google as a telegram message

## Description
This is a rudimentary Python script for personal use. It runs twice a day (morning and evening) to send a message via Telegram in order to tell the different time needed to travel different routes. The script uses Google API and Telegram API.

## Prerequisite
In order to use this, you need the following:
  1. Google API Token for directions (https://developers.google.com/maps/documentation/directions/get-api-key)
  2. A Telegram bot (https://core.telegram.org/bots)
  3. if you want to run it periodically, you need a running server,pc, etc.
  
  
## Usage
I run a scheduled task on Linux via crontab. In order to run the script you need to enter your Telegram chat ID (after you messaged your bot you can get your chat ID via the Telegram API), Google API token and Telegram bot token. Run in command line:

```
python commute.py "<starting location>" "<target location>"
```

For Example:
```
python commute.py "New York Manhatten" "New York Bronx"
```
![exampleroute](https://user-images.githubusercontent.com/23060346/44353811-79386480-a4a8-11e8-98a7-51652522fa1e.PNG)
