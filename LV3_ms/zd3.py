import pandas as pd
import json
import matplotlib.pyplot as plt
from datetime import datetime

print("Analiza kvalitete zraka - PM10 koncentracija za Osijek, 2017\n")


with open(r'c:\Users\student\Desktop\LV3_ms\modify-.json', 'r', encoding='utf-8') as file:
    data = json.load(file)   


df = pd.DataFrame(data)


df['datum'] = pd.to_datetime(df['vrijeme'], unit='ms')


df = df.rename(columns={'vrijednost': 'PM10_koncentracija'})

print(f"Ukupno mjerenja: {len(df)}\n")
print("Osnovne statistike PM10 koncentracije:")
print(df['PM10_koncentracija'].describe())
print("\n")


print("Tri datuma u 2017. godini kada je koncentracija PM10 bila najveća:\n")
top_3 = df.nlargest(3, 'PM10_koncentracija')

for i, (idx, row) in enumerate(top_3.iterrows(), 1):
    print(f"{i}. {row['datum'].strftime('%d.%m.%Y')} - {row['PM10_koncentracija']:.2f} {row['mjernaJedinica']}")

print("\n")


plt.figure(figsize=(12, 6))
plt.plot(df['datum'], df['PM10_koncentracija'], linewidth=0.8)
plt.axhline(y=50, color='r', linestyle='--', label='Granična vrijednost (50 µg/m³)')
plt.xlabel('Datum')
plt.ylabel('PM10 koncentracija (µg/m³)')
plt.title('Dnevna koncentracija PM10 čestica - Osijek, 2017')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()