import berserk
from decouple import config

session = berserk.TokenSession(config("LICHESS_KEY"))
client = berserk.Client(session=session)

games = client.games.export_by_player("sadrda")

past_game_search_threshold = 1000
game_count = 0

status_hist = {}
color_hist = {}
for game in games:
    print(game_count)
    if game_count >= past_game_search_threshold:
        break

    status = game["status"]
    players = game["players"]

    if("user" in players["white"].keys()):
        color = "white" if players["white"]["user"]["name"] == "sadrda" else "black"
    if("user" in players["black"].keys()):
        color = "black" if players["black"]["user"]["name"] == "sadrda" else "white"

    if status in status_hist.keys():
        status_hist[status] += 1
    else:
        status_hist[status] = 1

    if color in color_hist.keys():
        color_hist[color] += 1
    else:
        color_hist[color] = 1
    
    game_count += 1

    
print(color_hist)
print(status_hist)