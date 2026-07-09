import requests
from bs4 import BeautifulSoup

# def getLatestPatch():
lolurl = "https://www.leagueoflegends.com/en-us/news/game-updates/"
response = requests.get(lolurl)
patchNotesUrl = ""

if  response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('a')
    for title in titles:
        if "League of Legends Patch" in title['aria-label']:
            # patchNotes.append((title['aria-label']).replace(" ","-").replace(".","-").lower())
            # print("https://www.leagueoflegends.com/en-us/news/game-updates/" + (title['aria-label']).replace(" ","-").replace(".","-").lower())
            patchNotesUrl = lolurl + (title['aria-label']).replace(" ","-").replace(".","-").lower()
            break
    

response = requests.get(patchNotesUrl)
if  response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    champ = soup.find(id="patch-senna")
    for sibling in champ.next_siblings:
        print(sibling.text)
    
    
    
    
#     # Step 2: Send a network request to the hub page
#     response = send_get_request(hub_url)
    
#     # Step 3: Check if the request was successful (Status Code 200)
#     IF response is not successful:
#         PRINT "Error fetching page"
#         RETURN
        
#     # Step 4: Pass the response text into your HTML parser
#     soup = parse_html(response.text)
    
#     # Step 5: Search the parsed HTML for the first link that points to a specific patch
#     # Hint: Look for <a> tags where the href attribute contains "patch-" and "notes"
#     target_link = search_for_patch_link(soup)
    
#     # Step 6: Make a second GET request to that specific patch notes URL
#     patch_response = send_get_request(target_link)
    
#     # Step 7: Return or print the raw HTML of the patch notes
#     RETURN patch_response.text