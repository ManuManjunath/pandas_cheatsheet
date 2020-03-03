# Index
df.loc[row_index, col_index]
# row_index is by default --> 0, 1, 2, ..
# To specify a particular column as Index:
df = read_csv("this_file.csv", index='this_column')
# col_index is the column name
# If column_index = ":" --> Get all columns
# Gets rows 10 to 20 and columns # 1 and 4
df.iloc[10:10, [0,3]]
