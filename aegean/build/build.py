# Gera ../index.html e ../paises_aeroportos.csv a partir de template.html + countries.py
import json, csv, os, sys
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
from countries import C
REGN={'EU':'Europa & Norte da África','ME':'Oriente Médio','AF':'África Central & Sul','NC':'Oriente Próximo & Ásia Central','FE':'Extremo Oriente','OC':'Oceania','NA':'América do Norte','SA':'América Central & Sul','HI':'Havaí'}
data=[{'en':en,'pt':pt,'r':r,'ap':[list(a) for a in ap]} for en,pt,r,ap in C]
s=open(os.path.join(here,'template.html')).read()
s=s.replace('/*WORLD*/null',open(os.path.join(here,'countries-110m.json')).read()).replace('/*COUNTRIES*/[]',json.dumps(data,ensure_ascii=False,separators=(',',':')))
open(os.path.join(here,'..','index.html'),'w').write(s)
with open(os.path.join(here,'..','paises_aeroportos.csv'),'w',newline='') as f:
    w=csv.writer(f); w.writerow(['País','Região Aegean','Código região','Aeroporto (IATA)','Cidade','Latitude','Longitude'])
    for en,pt,r,ap in sorted(C,key=lambda c:(list(REGN).index(c[2]) if c[2] else 99,c[1])):
        if not r: continue
        for a in ap or [('','',None,None)]: w.writerow([pt,REGN[r],r,a[0],a[1],a[2],a[3]])
print('ok')
