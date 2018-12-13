import pandas as pd
weather = pd.read_csv("book1.csv")
weather.info()
for i in weather.iterrows():
    print(i)
#print(weather["c1"])
