import load_games as lg
import pandas as pd

filepath = "data/lichess_jeanleonino_2023-09-12.pgn"
games = lg.open_and_scrape_headers(filepath)
