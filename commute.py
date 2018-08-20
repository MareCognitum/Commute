import googlemaps
import requests
import sys
#declarations
Token = '' #Enter your Google API Token here
start = sys.argv[1]
end = sys.argv[2]
bot_token = '' # Enter your Telegram bot token here
id = '' # Enter your Telegram chat id here
# get Client object
client = googlemaps.Client(key=Token)
# get directions
try:
    directions = client.directions(start,end,alternatives=True)

# prepare data
    table = dict()
    for i in range(len(directions)):
        table.setdefault(directions[i]["summary"])
        table[directions[i]["summary"]] = directions[i]["legs"][0]["duration"]["text"]

    result_list = []
    for key,value in table.items():
        result_list.append(' '.join([key,':',value, "\n"]))

# get request and send message via bot
    message = ''.join(result_list)

    requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(bot_token,id,message))

except:
    error = 'Error during processing'
    requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(bot_token, id, error))

