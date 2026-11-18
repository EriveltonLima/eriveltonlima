# Dados dos dois programas (valores de pesquisa web, nov/2026; 's' = visto em fonte, 'e' = estimado)
import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','aegean','build'))
from countries import C
AP={}
for en,pt,r,aps in C:
    for code,city,lat,lon in aps: AP[code]=dict(c=code,n=city,country=pt,lat=lat,lon=lon)
EXTRA={'DMM':('Dammam','Arábia Saudita',26.47,49.80),'EDI':('Edimburgo','Reino Unido',55.95,-3.37),'BLR':('Bangalore','Índia',13.20,77.71),
'MAA':('Chennai','Índia',12.99,80.17),'COK':('Kochi','Índia',10.15,76.40),'HYD':('Hyderabad','Índia',17.23,78.43),'LHE':('Lahore','Paquistão',31.52,74.40),
'DUR':('Durban','África do Sul',-29.61,31.12),'DFW':('Dallas','Estados Unidos',32.90,-97.04),'ATL':('Atlanta','Estados Unidos',33.64,-84.43),
'PHL':('Filadélfia','Estados Unidos',39.87,-75.24),'SEA':('Seattle','Estados Unidos',47.45,-122.31),'BNE':('Brisbane','Austrália',-27.38,153.12),
'ADL':('Adelaide','Austrália',-34.95,138.53),'PMI':('Palma de Maiorca','Espanha',39.55,2.74),'AGP':('Málaga','Espanha',36.67,-4.49),
'SVQ':('Sevilha','Espanha',37.42,-5.89),'VLC':('Valência','Espanha',39.49,-0.48),'BIO':('Bilbao','Espanha',43.30,-2.91),'VCE':('Veneza','Itália',45.50,12.35)}
for k,(n,c,la,lo) in EXTRA.items(): AP[k]=dict(c=k,n=n,country=c,lat=la,lon=lo)

QATAR=dict(
 key='qatar',cabins=['Econômica','Executiva'],cabinsLong=['Econômica','Executiva'],title='Radar Qatar Avios',name='Qatar Airways Privilege Club',accent='#8c1d40',accent2='#c9a46a',hub='DOH',
 hubAp=dict(c='DOH',n='Doha',country='Catar',lat=25.27,lon=51.61),
 mode='zone',
 intro='Preço por local: cada destino da Qatar cai numa faixa de preço a partir de Doha. O mapa pinta cada destino pelo valor em Avios.',
 rows=[ # label, desc, [Yoff,Ypeak,Coff,Cpeak], flags
  ('Faixa 1','Golfo (GCC)',[5000,6500,10000,13500],'eeee'),
  ('Faixa 2','Oriente Médio, Cáucaso, Norte da África próximo',[10000,12500,20000,27000],'eeee'),
  ('Faixa 3','Europa, Sul da Ásia, Tailândia, África Oriental, Marrocos',[20000,25000,42500,57500],'sese'),
  ('Faixa 4','Leste e Sudeste Asiático, África Ocidental e Austral',[27500,34500,50000,67500],'esse'.replace('s','e',1) if False else 'eese'),
  ('Faixa 5','América do Norte, Austrália e Nova Zelândia',[35000,43500,70000,94500],'eess'),
  ('Faixa 6','América do Sul',[40000,50000,90000,121500],'sese'),
 ],
 zones={1:'DXB AUH MCT KWI BAH RUH JED DMM',2:'AMM BEY CAI BGW EBL IKA TBS GYD TUN ALG',
  3:'LHR MAN EDI DUB CDG NCE FRA MUC BER DUS ZRH GVA VIE FCO MXP VCE BCN MAD LIS AMS BRU CPH OSL ARN HEL WAW PRG BUD ATH SKG IST SOF OTP BEG ZAG CMN RAK DEL BOM BLR MAA COK HYD KHI ISB LHE DAC KTM CMB MLE BKK HKT NBO ADD DAR ZNZ EBB KGL',
  4:'SIN KUL CGK DPS MNL SGN HAN PNH HKG PVG PEK CAN ICN NRT HND KIX TPE JNB CPT DUR LOS ABV ACC LAD MPM',
  5:'JFK IAD ORD LAX MIA BOS DFW ATL PHL SFO SEA YUL SYD MEL PER BNE ADL AKL',6:'GRU'},
 rule='Voo direto de/para Doha: vale a faixa do destino. Entre duas cidades fora de Doha (ex.: GRU → DOH → BKK) o site soma os dois trechos como estimativa; a Qatar costuma cobrar o bilhete inteiro por origem e destino, às vezes por menos. Confira na calculadora oficial.',
 peakNote='Alta temporada costuma custar 20% a 36% a mais. Os valores da alta aqui são estimados quando não há fonte.',
 sources=[('awardtravelfinder.com — Qatar Airways Award Chart 2026','https://awardtravelfinder.com/award-charts/qatar-airways'),
  ('aviosintelligence.com — Avios Zone Map','https://www.aviosintelligence.com/zones'),
  ('awardfares.com — Qatar Airways Privilege Club Guide 2026','https://awardfares.com/blog/qatar-airways-privilege-club-guide/'),
  ('insideflyer.com — Qatar award chart offers value on select routes','https://www.insideflyer.com/posts/qatar-award-chart-offers-value-on-select-routes/'),
  ('Calculadora oficial — qatarairways.com Privilege Club','https://www.qatarairways.com/en/Privilege-Club/avios-calculator.html')],
)
QATAR['rows'][3]=('Faixa 4','Leste e Sudeste Asiático, África Ocidental e Austral',[27500,34500,50000,67500],'eese')

IBERIA_EXTRA={'ALC':('Alicante',38.28,-0.56),'LEI':('Almería',36.84,-2.37),'OVD':('Astúrias',43.56,-6.03),'BJZ':('Badajoz',38.89,-6.82),
'GRX':('Granada-Jaén',37.19,-3.78),'IBZ':('Ibiza',38.87,1.37),'XRY':('Jerez',36.74,-6.06),'LCG':('A Corunha',43.30,-8.38),'RJL':('Logroño',42.46,-2.32),
'MLN':('Melilla',35.28,-2.96),'MAH':('Menorca',39.86,4.22),'RMU':('Múrcia',37.80,-1.13),'PNA':('Pamplona',42.77,-1.65),'SLM':('Salamanca',40.95,-5.50),
'EAS':('San Sebastián',43.36,-1.79),'SDR':('Santander',43.43,-3.82),'SCQ':('Santiago de Compostela',42.90,-8.42),'VLL':('Valladolid',41.71,-4.85),
'VGO':('Vigo',42.23,-8.63),'BOD':('Bordéus',44.83,-0.72),'LDE':('Lourdes',43.18,-0.01),'LYS':('Lyon',45.73,5.08),'MRS':('Marselha',43.44,5.22),
'MPL':('Montpellier',43.58,3.96),'NTE':('Nantes',47.16,-1.61),'ORN':('Orã',35.62,-0.62),'PGF':('Perpignan',42.74,2.87),'RNS':('Rennes',48.07,-1.73),
'TNG':('Tânger',35.73,-5.92),'TLS':('Toulouse',43.63,1.37),'FUE':('Fuerteventura',28.45,-13.86),'ACE':('Lanzarote',28.95,-13.61),
'SPC':('Santa Cruz de la Palma',28.63,-17.76),'TFN':('Tenerife Norte',28.48,-16.34),'BHX':('Birmingham',52.45,-1.75),'CTA':('Catânia',37.47,15.07),
'ORK':('Cork',51.84,-8.49),'SXB':('Estrasburgo',48.54,7.63),'FLR':('Florença',43.81,11.21),'GOA':('Gênova',44.41,8.84),'GLA':('Glasgow',55.87,-4.43),
'HAM':('Hamburgo',53.63,9.99),'NAP':('Nápoles',40.89,14.29),'PMO':('Palermo',38.18,13.10),'TRN':('Turim',45.20,7.65),'GOT':('Gotemburgo',57.66,12.28),
'CLO':('Cali',3.54,-76.38)}
CTRY={'BOD':'França','LDE':'França','LYS':'França','MRS':'França','MPL':'França','NTE':'França','PGF':'França','RNS':'França','TLS':'França','SXB':'França',
 'ORN':'Argélia','TNG':'Marrocos','BHX':'Reino Unido','GLA':'Reino Unido','ORK':'Irlanda','CTA':'Itália','FLR':'Itália','GOA':'Itália','NAP':'Itália','PMO':'Itália','TRN':'Itália',
 'HAM':'Alemanha','GOT':'Suécia','CLO':'Colômbia'}
for k,(n,la,lo) in IBERIA_EXTRA.items():
    if k not in AP: AP[k]=dict(c=k,n=n,country=CTRY.get(k,'Espanha'),lat=la,lon=lo)
IBERIA=dict(
 key='iberia',title='Radar Iberia Avios',name='Iberia Club (Iberia Plus)',accent='#d7192d',accent2='#f6b800',hub='MAD',
 hubAp=None,mode='distance',
 cabins=['Básica','Confort','Premium','Business'],
 cabinsLong=['Económica Básica','Económica Confort','Turista Premium Confort','Business Confort'],
 intro='Tabela oficial da Iberia: cada voo é cobrado pela banda de distância do destino a partir de Madri. Com conexão em Madri, somam-se os trechos.',
 rows=[ # label, desc, off[Bas,Conf,Prem,Bus], peak[...], flags
  ('Banda 1','0 – 650 milhas',[3500,7000,None,9750],[4750,8750,None,11500]),
  ('Banda 2','651 – 1.150 milhas',[6500,12500,None,16500],[8000,14000,None,18250]),
  ('Banda 3','1.151 – 2.000 milhas',[9500,16000,None,22000],[10750,18750,None,24000]),
  ('Banda 4','2.001 – 3.000 milhas',[10500,17000,None,23000],[12000,20750,None,31000]),
  ('Banda 5','3.001 – 4.000 milhas',[16000,25000,29500,40500],[19500,31500,40250,59000]),
  ('Banda 6','4.001 – 5.500 milhas',[20000,31250,36750,50500],[24250,39000,50500,74000]),
  ('Banda 7','5.501 – 6.500 milhas',[24000,37250,44000,60500],[29250,46500,60500,88500]),
  ('Banda 8','6.501 – 7.000 milhas',[28250,42750,51000,70500],[34250,54000,70500,103500]),
  ('Banda 9','mais de 7.000 milhas',[41000,60000,71000,97000],[49250,75000,97000,140000]),
  ('Ponte Aérea','Madri – Barcelona',[None,6250,None,13500],[None,6250,None,13500]),
 ],
 upgrades=dict(cols=['Economy → Premium','Premium → Business','Economy → Business'],
  off=[[None,None,6250],[None,None,10000],[None,None,12500],[None,None,12500],[13500,11000,24500],[16750,13750,30500],[20000,16500,36500],[22750,19500,42250],[30000,26000,56000]],
  peak=[[None,None,6750],[None,None,10250],[None,None,13250],[None,None,19000],[20750,18750,39500],[26250,23500,49750],[31250,28000,59250],[36250,33000,69250],[47750,43000,90750]]),
 bands={1:'ALC LEI OVD BJZ BCN BIO GRX IBZ XRY LCG RJL AGP MLN MAH RMU PMI PNA SLM EAS SDR SCQ SVQ VLC VLL VGO ALG BOD CMN GVA LIS LDE LYS MRS MPL NTE NCE OPO ORN PGF RNS TNG TLS',
  2:'FUE LPA ACE SPC TFN RAK BRU AMS BER BHX CTA ORK DUB DBV DUS MUC SXB FLR FRA FNC GOA GLA HAM LHR MLA MAN MXP NAP PMO CDG PRG FCO TRN VCE VIE ZAG ZRH',
  3:'ATH OTP BUD KRK CPH CFU IST ARN GOT HER JMK SVO OSL KEF LED WAW DSS',4:'CAI LOS SSG TLV',5:'BOS ORD LAD JFK SJU',
  6:'BOG CCS CLO SAL GUA GYE JNB HAV LIM LAX MDE MEX MIA PTY UIO GIG SJO SDQ GRU',7:'EZE MVD SCL',8:'NRT PVG'},
 special={'BCN':9},
 rule='Cada voo é cobrado pela banda oficial do destino a partir de Madri (lista da Iberia), não pela distância exata. Com conexão em Madri, os trechos somam: GRU → MAD → ATH = banda 6 + banda 3. Madri–Barcelona usa a tarifa da Ponte Aérea (só Confort e Business). Turista Premium só existe nas bandas 5 a 9.',
 peakNote='Valores oficiais da Iberia, por trajeto (só ida). Época alta e baixa seguem o calendário da Iberia.',
 sources=[('Tabela oficial de utilização de Avios da Iberia (enviada por você)','https://www.iberia.com/')],
)
def build(P):
    hub=P['hub']; aps={}
    if P['hubAp']: aps[hub]=P['hubAp']
    else: aps[hub]=AP[hub]
    if P['mode']=='zone':
        dz={}
        for z,l in P['zones'].items():
            for c in l.split(): dz[c]=z
        for c in dz: aps[c]=AP[c]
        routes=list(dz)
    else:
        dz={}
        for b,l in P['bands'].items():
            for c in l.split(): dz[c]=b
        routes=list(dz)
        for c in routes: aps[c]=AP[c]
    out={k:v for k,v in P.items() if k not in('zones','routes','hubAp','bands')}
    rows=[]
    for r in P['rows']:
        if len(r[2])==4 and P['mode']=='zone':
            v=r[2];f=r[3];rows.append(dict(l=r[0],d=r[1],off=[v[0],v[2]],peak=[v[1],v[3]],foff=[f[0],f[2]],fpeak=[f[1],f[3]]))
        else:
            rows.append(dict(l=r[0],d=r[1],off=r[2],peak=r[3],foff=['s']*len(r[2]),fpeak=['s']*len(r[3]),mi=None))
    if P['mode']=='distance':
        lim=[(0,650),(651,1150),(1151,2000),(2001,3000),(3001,4000),(4001,5500),(5501,6500),(6501,7000),(7001,99999)]
        for i,x in enumerate(lim): rows[i]['mi']=x
    out['rows']=rows
    out['airports']=list(aps.values()); out['spokes']=routes; out['zoneOf']=dz
    return out
