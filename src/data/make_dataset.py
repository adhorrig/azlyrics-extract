import pandas as pd

url="https://gist.githubusercontent.com/mbejda/9912f7a366c62c1f296c/raw/dd94a25492b3062f4ca0dc2bb2cdf23fec0896ea/10000-MTV-Music-Artists-page-1.csv"

c=pd.read_csv(url)
c=c.dropna() #Remove rows with empty genres
df=c[['name','genre']]
df.to_csv('/Users/adamhorrigan/Documents/Dev/azlyrics-extract/data/mtv_dataset.csv', encoding='utf-8', index=False)


