import requests
from bs4 import BeautifulSoup
import json

with open('champs.json', 'r') as file:
    config = json.load(file)
    
myChampPool = config['champions']
# def getLatestPatch():
lolurl = "https://www.leagueoflegends.com/en-us/news/game-updates/"
response = requests.get(lolurl)
patchNotesUrl = ""
webhook = "https://discord.com/api/webhooks/1525815553443237983/ovuR_rcgKaAjZM2SXE0-aGrliVFTkT27n5A2rgLpjHffrqLFKShzWTxKsOp4Zh4KuBji"


if  response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('a')
    for title in titles:
        if "League of Legends Patch" in title['aria-label']:
            patchNotesUrl = lolurl + (title['aria-label']).replace(" ","-").replace(".","-").lower()
            payload = {
                "content": f"## **{title['aria-label']}**\n"
            }
            discord_response = requests.post(webhook, json=payload)
            break
    

response = requests.get(patchNotesUrl)
if  response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for champName in myChampPool:
        champSummary = ""
        champ = soup.find(id = f"patch-{champName}")
        # print (champName.capitalize())
        if champ is None:
            # print("No changes")
            champSummary = "No changes"
            payload = {
                "content": f"## **{champName.capitalize()}**\n{champSummary}"
            }
        else:
            for sibling in champ.next_siblings:
                # print(sibling.name)
                if sibling.name == "ul":
                    for li in sibling.find_all("li"):
                        # print(li.text)
                        champSummary += f"{li.text}\n"
                else:
                    # print(sibling.text)
                    champSummary += f"{sibling.text}\n"
            # print(champSummary)
            
            payload = {
                "content": f"## **{champName.capitalize()}**\n{champSummary}"
            }
        discord_response = requests.post(webhook, json=payload)
        if discord_response.status_code == 204:
            print(f"Successfully sent Discord alert for {champName.capitalize()}!")
        else:
            print(f"Failed to send alert for {champName.capitalize()}. Error code: {discord_response.status_code}")