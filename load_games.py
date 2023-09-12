import chess.pgn
import pandas as pd


def get_headers(filepath):
	with open(filepath) as f:
		game = chess.pgn.read_game(f)

	header_list = []

	for key in game.headers:
		header_list.append(key)

	return header_list

def open_and_scrape_headers(filepath):
	header_list = get_headers(filepath)
	game_id = 0
	g = pd.DataFrame(columns=['game_id'] + header_list)

	with open(filepath) as f:
		while True:
			game = chess.pgn.read_game(f)
			game_id += 1

			# If there are no more games, exit the loop
			if game is None:
				break

			value_list = [game_id]

			for header in header_list:
				try:
					value_list.append(game.headers[header])
				except:
					value_list.append('')

			g.loc[len(g)] = value_list

			if (game_id % 500 == 0):
				print('Now adding game_id: ' + str(game_id))

	return g
