from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)
soup = bs(page.text, "html.parser")

tempList = []
starTable = soup.find_all("table")
tableRows = starTable[7].find_all("tr")

for tr in tableRows:
    td = tr.find_all("td")
    row = [i.text.strip() for i in td]
    tempList.append(row)

starName = []
radius = []
mass = []
distance = []

for i in range(1, len(tempList)):
    starName.append(tempList[i][2])
    radius.append(tempList[i][9])
    mass.append(tempList[i][8])
    distance.append(tempList[i][5])

df2 = pd.DataFrame(list(zip(starName, distance, mass, radius)), columns = ["Star Namea", "Distance", "Mass", "Radius"])
df2.to_csv("dwarfStars.csv")