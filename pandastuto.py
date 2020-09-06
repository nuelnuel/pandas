import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df)

# df.head is useful.

headers = df.columns
somenames = df['Name']
# print(somenames)

scmmec = df[['Name', 'Type 1', 'Attack']]

# print(scmmec)

# A way to get rows
rows = df.iloc[0:2]
specrow = df.iloc[1, 2]

# Specific data in df.
sssr = df.loc[df['Type 1'] == 'Fire']
# print(sssr)

# Describe your df stadistics
xx = df.describe()
# print(xx)

# Sort values

sorrr = df.sort_values('Name', ascending=False)

df['Total'] = df['HP'] + df['Attack']  # Set a new column

# Another way to sum columns

df['Tollla'] = df.iloc[:, 4:10].sum(axis=1)

# print(df.head(5))

# Saving our data

# df.to_csv('modnew')

# print(df)


### Filtering Data

fl1 = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]

# Contain something specific in the words. This is useful.

mega = df.loc[df['Name'].str.contains('Mega')]
# print(mega)

nomega = [df.loc[~df['Name'].str.contains('Mega')]]
# print(nomega)

### Conditional Changes


df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
 # print(df)


#Group by

dt = pd.read_csv('pokemon_data.csv')
wowo = dt.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)
 # print(wowo)


haas = dt.groupby(['Type 1', 'Type 2'])
# print(haas)
# print(dt)




























