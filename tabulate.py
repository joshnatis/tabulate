import sys
import csv

def get_max_col_lengths(df):
	lengths = []
	num_cols = len(df[0])
	for i in range(num_cols):
		lengths.append(max([len(row[i]) for row in df]))
	return lengths

def print_table(df):
	num_cols = len(df[0])
	col_widths = get_max_col_lengths(df)
	df_width = sum(col_widths) + 1 + num_cols

	header = True

	print_border(df_width, col_widths)
	for row in df:
		print('|', end='')
		for i in range(len(row)):
			print(row[i].ljust(col_widths[i]) + '|', end="")
		print('')

		if header:
			print_border(df_width, col_widths)
			header = False
	print_border(df_width, col_widths)

def print_border(df_width, col_widths):
	border = '-' * (df_width - 1)
	elapsed = 0
	for length in col_widths:
		elapsed += length
		border = border[:elapsed] + '+' + border[elapsed + 1:]
		elapsed += 1
	print('+' + border)

def pad_missing_columns(df):
	max_cols = len(df[0])
	for i in range(len(df)):
		if len(df[i]) < max_cols:
			df[i] += [''] * (max_cols - len(df[i]))
		elif len(df[i]) > max_cols:
			df[i] = df[i][:max_cols]

def tabulate(lines, delim=','):
	df = []
	reader = csv.reader(lines)
	for row in reader:
		row = [(' ' + col.strip() + ' ') for col in row]
		df.append(row)

	if not df:
		return ''

	pad_missing_columns(df)
	print_table(df)

def main():
	tabulate(sys.stdin.readlines())

if __name__ == '__main__':
	try: main()
	except IndexError: pass
