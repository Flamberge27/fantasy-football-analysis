import os

# this is just for my own use, so it's going to be a console script

# to start, define the year.
# this could just prompt the user, but then I'd have to enter it
# every time I do a test run. sounds like a pain.
year = 2023

current_folder = ("\\").join(__file__.split("\\")[:-1])
analyst_folder = current_folder + "\\" + str(year) + " analyst predictions\\"

# to start, we'll have to process the analyst prediction spreadsheets
player_positions = ['dst', 'k', 'qb', 'rb', 'te', 'wr']
analysts = []

for position in ['te']:
	compiled_path = analyst_folder + 'compiled_' + position + 's.csv'
	compiled_file = open(compiled_path, 'r')

	processed_path = analyst_folder + 'processed_' + position + 's.csv'
	processed_file = open(processed_path, 'w')

	lines = compiled_file.readlines()

	if len(lines) < 2:
		print('Insufficient data lines')
		continue
	
	# extract our analysts from the header
	header = lines[0]
	header_cols = header.split(',')

	# cheeky start from 2 because we expect there to be a 'rank, player' column
	# that'll mess up our splitting
	for col in header_cols[2:]:
		if "AVG" not in col and col not in analysts:
			analysts.append(col)
	new_header = 'Player,' + (',').join(header_cols[2:])
	processed_file.write(new_header)

	# now copy down the rankings
	for line in lines[1:]:
		#"""
		try:
			player_cols = line.split(',')

			pre_name = player_cols[0] # technically this is the first half of the first column
			city = player_cols[1] # grossly, this is the player's city and still in the first column

			letters = [letter for letter in pre_name if letter.isalpha()]
			print(letters[0] + " | " + str(ord(letters[0])))

			processed_file.write(pre_name + ',' + (',').join(player_cols[2:]))
		except IndexError:
			continue
		#"""
	
	compiled_file.close()
	processed_file.close()