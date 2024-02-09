import requests
import bs4


# Basis URL für die Liga
url_league = "https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"

# Benötigte Infos für requests-Anfrage 
payload = ""
headers = {
    "cookie": "_sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbKKxs_IAzEMamN1YpRSQcy80pwcILsErKC6lpoSSrEA-EAOLpYAAAA^%^3D; _sp_v1_p=893; _sp_v1_data=745500; _sp_su=false; TMSESSID=7f81390691515adc2ce043701b785bc1; euconsent-v2=CP5m9AAP5m9AAAGABCENAmEsAP_gAEPAAAYgJDgBdDJECCFAIXBaAOsQKIEVUVABAEAAAAABACABQAAAIAQCkAAIAACAAigAARAAIEQAAAAAAAAABAAAAIAAIAAEAAAQgAAIIAAAAAAAAABAAAAIAAAAQAAAgAABAAQAkACIAAIAUEAAAAACAAAQAIgAAIAAAgAAAAAAAAAAAAIIICgAAAAAAAAAAAACABAAAAAIH7wEQAFAAOAEUAI4AcgBCACIgE7ALEAXUA14B2wF0AMEAZCAyYB-4BwSAsABUADgAIAAZAA0ACIAEwAJ4AZgA3gB6AD8AIQAQwAmgBlAD9AKeAo8BeYDJAG5hQAQAigF0BoAIBTx0BwACoAHAAQAAyABoAEQAJgAT4AuAC6AGIAMwAbwA9AB-AEMAJoAZQA_QCLAFPALEAi8BR4CrAF5gMkAZYA4seABAEUOAAgNzEQAQCnkIBAATAAuABiADeAHoARwBTwFWEAAIA5CUAsADgARAAmABcADEAIYAp4CLwFHgLzAZISAAgMsLQAgBHAKsKQFAAKgAcABAADQAIgATAAngBiADMAH4AQwAygB-gEWAPaAi8BVgC8wGSAMsKABQAZABbAHIAScBuYA.YAAAAAAAAAAA; consentUUID=259e2e62-4ca7-4c17-b0d4-38dbff789f80_28; _ga=GA1.2.200025538.1707311381; _gid=GA1.2.230276665.1707311381; _gat_gtag_UA_3816204_13=1; kndctr_B21B678254F601E20A4C98A5_AdobeOrg_identity=CiYwMDI3NDI3MDE4MzQzMDYzMzg0MTc5MDMzMDkzNjMyOTEwMzIzNFIRCOH0wJ3YMRgBKgRJUkwxMAHwAeH0wJ3YMQ==; kndctr_B21B678254F601E20A4C98A5_AdobeOrg_cluster=irl1; AMCV_B21B678254F601E20A4C98A5^%^40AdobeOrg=MCMID^|00274270183430633841790330936329103234; _tmlpu=2",
    "authority": "www.transfermarkt.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "de-DE,de;q=0.9,en-DE;q=0.8,en;q=0.7,en-US;q=0.6,tr;q=0.5,da;q=0.4",
    "cache-control": "max-age=0",
    "referer": "https://www.transfermarkt.com/",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua": "Not",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

# leeres Dictionary anlegen, um Daten speichern zu können
teams = {}

# Unendliche Schleife mit Menüauswahl, bis der Nutzer das Programm beendet
while True: 
    print('1. Show available teams') 
    print('2. Select team and show high level information on the team')
    print('3. Select team and and show all players of the team')
    print('4. Quit') 

    # Input für Menüauswahl
    userInput = int(input())
    

    # Code, wenn Nutzer 1 eingibt:
    if userInput == 1: # Nutzerauswahl auf 1 prüfen
        r = requests.request("GET", url_league, data=payload, headers=headers) # requests-Befehl definieren
        if r.status_code == 200: # Nur ausführen, wenn Status-Code gültig ist und Daten geladen werden können
            htmlText = r.text # Text extrahieren aus html
            htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') # Text parsen mit Beautiful Soup
            items = htmlDocument.find('table', {'class': 'items'}).find('tbody').find_all('tr') # Definition, in welchem Bereich die benötigten Informationen liegen
            print('\n')
            pos = 1 # Variable Position anlegen und auf 1 setzen

            # Schleife erstellen, die den Teamnamen und alle nötigen Details sucht
            for item in items:
                team = item.find('td', {'class': 'hauptlink no-border-links'})
                team_name = team.find('a').get_text()
                team_link = team.find('a').get('href')
                details_a = item.find_all('td', {'class': 'zentriert'})
                detaillist_a = [] # Liste für Details anlegen, da class: zentriert mehrfach vorkommt
                for detail_a in details_a: # Schleife für die ersten drei Details
                    detaillist_a.append(detail_a)
                squad = detaillist_a[1].get_text()
                avg_age = detaillist_a[2].get_text()
                foreigners = detaillist_a[3].get_text()
                details_b = item.find_all('td', {'class': 'rechts'})
                detaillist_b = [] # Liste für Details anlegen, da class: rechts mehrfach vorkommt
                for detail_b in details_b: # Schleife für die weiteren Details, die in Liste gespeichert werden müssen
                    detaillist_b.append(detail_b)
                avg_market_value = detaillist_b[0].get_text()
                total_market_value = detaillist_b[1].find('a').get_text()


                # Liste ausgeben, Dictionary befüllen und Position um 1 erhöhen:
                print(f'{pos}. {team_name}') # Tabelle ausgeben
                
                # Dictionary befüllen
                teams[pos] = {
                    'teamname': team_name, 
                    'teamlink': team_link, 
                    'squad': squad, 
                    'average age': avg_age, 
                    'foreigners': foreigners, 
                    'average market value': avg_market_value, 
                    'total market value': total_market_value
                            }
                pos += 1 # Position um 1 erhöhen
            print('\n')
        else:
            print(f'Der Vorgang war nicht erfolgreich, Status-Code: {r.status_code}') # Fehlermeldung falls, Statuscode nicht 200 ist
    
    # Code, wenn Nutzer 2 eingibt:
    elif userInput == 2: # Nutzerauswahl auf 2 prüfen
        print("Select your team by position")
        newInput = int(input()) # fragt Nutzer nach Input für das Team
        selected_team = teams[newInput] # Weist das gewählte Team im Dictionary zu
        print('\n')
        for key, value in selected_team.items(): # Schleife, die alle Details ausgibt, außer den Teamlink, da dieser nur für Menü 3 gespeichert werden soll
            if key != 'teamlink':
                print(f"{key}: {value}")
        print('\n')

    # Code, wenn Nutzer 3 eingibt:
    elif userInput == 3: # Nutzerauswahl auf 3 prüfen
        print("Select your team by position")
        newInput = int(input()) # fragt Nutzer nach Input für das Team
        selected_team = teams[newInput] # Weist das gewählte Team im Dictionary zu
        url_team = f"https://www.transfermarkt.com{selected_team['teamlink']}/plus/1" # Definiert die neue URL, auf der gesucht werden soll anhand des Teamlinks
        # Erstelle neuen requests-Befehl
        r = requests.request("GET", url_team, data=payload, headers=headers)
        if r.status_code == 200:  # Nur ausführen, wenn Status-Code gültig ist und Daten geladen werden können
            htmlText = r.text # Text extrahieren aus html
            htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') # Text parsen mit Beautiful Soup
            soup = htmlDocument.find('div', {'class': 'box'}).find('table', {'class': 'items'}).find('tbody') # Definition, in welchem Bereich die benötigten Informationen liegen
            items = soup.find_all('td', {'class': 'posrela'}) # Suche nach allen Einträgen, in denen der Name in der weiteren Struktur ausgegeben wird
            print('\n')

            # Schleife erstellen, die die Spielernamen sucht und direkt ausgibt
            for item in items:
                player = item.find('td', {'class': 'hauptlink'})
                player_name = player.find('a').text.strip()
                print(player_name)
            print('\n')

    # Code, wenn Nutzer 3 eingibt: 
    elif userInput == 4: # Nutzerauswahl auf 4 prüfen
        break # Große while Schleife beenden
    
    # Fehlermeldung, wenn Input nicht gültig ist
    else:
        print('Invalid input')