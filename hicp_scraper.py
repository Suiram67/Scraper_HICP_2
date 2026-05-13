import requests
URL = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_midx?format=JSON&geo=EA&unit=I15&coicop=TOT_X_TBC&lang=EN"
reponse = requests.get(URL)
#print(reponse.status_code)
#print(reponse.text[:500])

data = reponse.json()
#print(data)
valeurs = data["value"]
#print(valeurs)
mois = data["dimension"]["time"]["category"]["index"]

#print("Nombre de mois :", len(mois))
#print("Nombre de valeurs :", len(valeurs))
#print("Premier mois :", list(mois.keys())[0])
#print("Dernier mois :", list(mois.keys())[-1])

serie ={}

for nom_mois,position in mois.items():
    
    if nom_mois < "2020-11":
            continue
    cle = str(position)
    if cle in valeurs:

        serie[nom_mois] = valeurs[cle]
print(len(serie))

print(list(serie.items())[0])
print(list(serie.values())[0])

"""
with open("hicp_history.csv","w",encoding = "utf-8") as s:
     for moi_nom,valeurs in serie.items():
          ligne = f"{moi_nom};{str(valeurs).replace('.',',')}\n"
          s.write(ligne)
"""


URL_2 = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/teicp240?format=JSON&geo=EA&unit=I25&lang=EN"

rep = requests.get(URL_2)
REBASE_FACTOR = 1.28128


rep_dic = rep.json()
#print(rep_dic)
valeurs2 = rep_dic["value"]
mois2 = rep_dic["dimension"]["time"]["category"]["index"]

#print(mois2)
for mois,keys in mois2.items():
     if mois <= "2025-12":
          continue
     clé = str(keys)
     if clé in valeurs2:
          serie[mois] = valeurs2[clé]*REBASE_FACTOR





with open("hicp_history.csv","a",encoding ="utf-8") as s:
    for x,y in serie.items():
        ligne2 = f"{x};{str(round(y,2)).replace(".",",")}\n"
        s.write(ligne2)


