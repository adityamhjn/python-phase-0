import pandas as pd 
print("Loading data...")
df=pd.read_csv('anime.csv')
print("First 5 rows \n")
print(df.head())
print("Available columns \n")
print(df.columns)
top_tv_shows=df[(df['type']=='TV') & (df['rating']>=8.5)]
print("Top TV shows with rating >= 8.5 \n")
print(top_tv_shows[['name','rating','episodes']].head(10))
specific_show=df[df['name']== 'One Piece']
print("Specific show details for One Piece \n")
print(specific_show[['name','rating','episodes','genre']])