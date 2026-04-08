import urllib.request
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.subplots_adjust(wspace=0.4, hspace=0.4)

# url koji sadrzi xml datoteku s mjerenjima:
# naglasiti da treba odabrati xml file, ne json
url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.3.2017'

airQualityHR = urllib.request.urlopen(url).read()
root = ET.fromstring(airQualityHR)

# tree = ET.parse('airquality.xml')
# root = tree.getroot()


df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))

children = list(root)
i = 0
while True:
    
    try:
        obj = list(children[i])
    except:
        break
    
    row = dict(zip(['mjerenje', 'vrijeme'], [obj[0].text, obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = pd.concat([df, row_s])
    df.mjerenje[i] = float(df.mjerenje[i])
    i = i + 1

df.vrijeme = pd.to_datetime(df.vrijeme, utc=True)
df.plot(y='mjerenje', x='vrijeme')
plt.show()

# add date month and day designator
df['month'] = df['vrijeme'].dt.month
df['dayOfweek'] = df['vrijeme'].dt.dayofweek


print(df.sort_values(['mjerenje']).tail(3))