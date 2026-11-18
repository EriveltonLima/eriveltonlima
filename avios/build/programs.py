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
 key='qatar',title='Radar Qatar Avios',name='Qatar Airways Privilege Club',accent='#8c1d40',accent2='#c9a46a',hub='DOH',
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

IBERIA=dict(
 key='iberia',title='Radar Iberia Avios',name='Iberia Club (Iberia Plus)',accent='#d7192d',accent2='#f6b800',hub='MAD',
 hubAp=None,
 mode='distance',
 intro='Zonas de distância: cada voo da Iberia é cobrado pela distância do trecho. Com conexão em Madri, somam-se os trechos.',
 rows=[ # label (milhas), desc, values, flags, [min,max] miles
  ('Zona 1','0 – 650 milhas',[5000,6500,10000,13000],'seee',[0,650]),
  ('Zona 2','651 – 1.150 milhas',[7500,9500,15000,19500],'eeee',[651,1150]),
  ('Zona 3','1.151 – 2.000 milhas',[10000,12500,20000,26000],'eeee',[1151,2000]),
  ('Zona 4','2.001 – 3.000 milhas',[13000,16500,30000,43500],'eeee',[2001,3000]),
  ('Zona 5','3.001 – 4.000 milhas',[17000,25000,40500,59000],'sess',[3001,4000]),
  ('Zona 6','4.001 – 5.500 milhas',[21250,31000,50500,74000],'eess',[4001,5500]),
  ('Zona 7','5.501 – 6.500 milhas',[25500,37000,60500,88500],'eess',[5501,6500]),
  ('Zona 8','6.501 – 7.000 milhas',[29750,43500,70500,103000],'eeee',[6501,7000]),
  ('Zona 9','7.001+ milhas',[34000,50000,80500,118000],'eeee',[7001,99999]),
 ],
 routes='LHR CDG FRA MUC ZRH GVA FCO MXP VCE LIS OPO BCN AMS BRU CPH ARN DUB ATH IST NCE DUS BER PMI AGP SVQ VLC BIO LPA TFS CMN RAK TLV DOH DSS NRT JFK BOS ORD MIA LAX IAD DFW SFO SJU MEX CUN HAV SDQ PUJ PTY SJO GUA SAL BOG MDE UIO GYE LIM SCL EZE MVD GRU GIG',
 rule='Cada voo é cobrado pela sua distância. GRU → MAD → ATH = trecho GRU–MAD (zona 6) + trecho MAD–ATH (zona 3).',
 peakNote='Alta temporada: em geral meados de junho a fim de setembro, Natal e Páscoa. Confira o calendário oficial da Iberia.',
 sources=[('awardtravelfinder.com — Iberia Award Chart 2026','https://awardtravelfinder.com/award-charts/iberia'),
  ('mightytravels.com — Iberia business to Madrid: 40,500 Avios off-peak (2026)','https://www.mightytravels.com/2026/10/iberia-business-to-madrid-40500-avios-off-peak-one-way-in-2026/?year=2026&month=10&slug=iberia-business-to-madrid-40500-avios-off-peak-one-way-in-2026'),
  ('awardlocker.com — Iberia Plus Award Chart','https://awardlocker.com/award-charts/iberia-plus'),
  ('aviosintelligence.com — Avios Zone Map','https://www.aviosintelligence.com/zones'),
  ('Calculadora oficial — iberia.com Avios','https://www.iberia.com/')],
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
        routes=P['routes'].split(); dz={}
        for c in routes: aps[c]=AP[c]
    out={k:v for k,v in P.items() if k not in('zones','routes','hubAp')}
    out['airports']=list(aps.values()); out['spokes']=routes; out['zoneOf']=dz
    return out
