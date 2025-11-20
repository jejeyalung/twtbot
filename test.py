import requests
from datetime import datetime, timezone, date

def get_last_ferrari_win():
    today = date.today()
    
    for year in range(today.year, 1949, -1):
        url = f"https://api.jolpi.ca/ergast/f1/{year}/constructors/ferrari/results/1.json?limit=300"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            races = data["MRData"]["RaceTable"]["Races"]
            
            if races:
                last_race = races[-1]
                win_date = datetime.strptime(last_race["date"], "%Y-%m-%d").date()
                return win_date
    return None
    
last_win = get_last_ferrari_win()
if last_win:
    days_since = (date.today() - last_win).days
    print(f"It has been {days_since} days since Ferrari won an F1 race. Their last win was on {last_win}.")
    
else:
    print("Ferrari has never won a race LMAO.")