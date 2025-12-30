
from requests import get

def get_games():
    url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
    return get(url).json()["scoreboard"]["games"]

print("=========== NBA Scoreboard ===========")

games = get_games()

for game in games:
    home_team = game["homeTeam"]
    away_team = game["awayTeam"]

    home = home_team["teamCity"] + " " + home_team["teamName"]
    away = away_team["teamCity"] + " " + away_team["teamName"]

    home_score = home_team["score"]
    away_score = away_team["score"]

    quarter = game["period"]
    clock = game["gameClock"]
    status = game["gameStatusText"]

    print(f"\n{away} vs {home}")
    print(f"Score: {away_score} - {home_score}")

    if quarter > 0:
        print(f"Quarter: Q{quarter}, Time left: {clock}")
    else:
        print(f"Start time: {status}")

    print("-" * 50)
