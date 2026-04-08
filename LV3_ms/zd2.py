import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars=pd.read_csv('mtcars.csv')
print("\n")

print("1. Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara.")
print("\n")

avg_mpg = cars.groupby('cyl')['mpg'].mean()

plt.figure(figsize=(8, 6))
plt.bar(avg_mpg.index.astype(str), avg_mpg.values, color=['blue', 'green', 'red'])
plt.xlabel('Broj cilindara')
plt.ylabel('Prosječna potrošnja (mpg)')
plt.title('Potrošnja automobila prema broju cilindara')
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n")

print("2. Pomoću boxplot-a prikažite na istoj slici distribuciju težine automobila s 4, 6 i 8 cilindara.")
print("\n")


data_4cyl = cars[cars['cyl'] == 4]['wt']
data_6cyl = cars[cars['cyl'] == 6]['wt']
data_8cyl = cars[cars['cyl'] == 8]['wt']

plt.figure(figsize=(8, 6))
plt.boxplot([data_4cyl, data_6cyl, data_8cyl], labels=['4 cilindara', '6 cilindara', '8 cilindara'])
plt.xlabel('Broj cilindara')
plt.ylabel('Težina automobila (1000 lbs)')
plt.title('Distribucija težine automobila prema broju cilindara')
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n")

print("3. Pomoću odgovarajućeg grafa pokušajte odgovoriti na pitanje imaju li automobili s ručnim mjenjačem veću potrošnju od automobila s automatskim mjenjačem?")

print("\n")
rucni_mpg = cars[cars['am'] == 0]['mpg']
automatski_mpg = cars[cars['am'] == 1]['mpg']

plt.figure(figsize=(8,6))
plt.bar([0, 1], [rucni_mpg.mean(), automatski_mpg.mean()], tick_label=['Ručni', 'Automatski'], color=("pink", "cyan"))
plt.xlabel('Vrsta mjenjača')
plt.ylabel('Potrošnja (mpg)')
plt.title('Potrošnja automobila prema vrsti mjenjača')
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n")

print("4. Prikažite na istoj slici odnos ubrzanja i snage automobila za automobile s ručnim odnosno automatskim mjenjačem.")

print("\n")

rucni = cars[cars['am'] == 0]
automatski = cars[cars['am'] == 1]


automatski['qsec']
automatski['hp']

rucni['qsec']  
rucni['qsec']

plt.figure(figsize=(8,6))
plt.scatter(rucni['hp'], rucni['qsec'], color='blue', label='Ručni mjenjač')
plt.scatter(automatski['hp'], automatski['qsec'], color='red', label='Automatski mjenjač')
plt.xlabel('Snaga (hp)')
plt.ylabel('Ubrzanje (qsec)')
plt.title('Odnos ubrzanja i snage automobila prema vrsti mjenjača')
plt.legend()
plt.show()
print("\n")
