# Gera ../mapa_regioes_A3.pdf (vetorial) e .png de prévia
import json,os,sys,subprocess
here=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,here)
from countries import C
d3,topo=sys.argv[1],sys.argv[2]
s=open(os.path.join(here,'print_template.html')).read()
s=s.replace('/*WORLD*/null',open(os.path.join(here,'countries-110m.json')).read()).replace('/*COUNTRIES*/[]',json.dumps([{'en':a,'pt':b,'r':r,'ap':ap} for a,b,r,ap in C],ensure_ascii=False))
s=s.replace('D3SRC','file://'+d3).replace('TOPOSRC','file://'+topo)
open('/tmp/claude-0/-home-user-eriveltonlima/bdf8dbeb-92d5-5db0-a6e1-c937dd241dd2/scratchpad/print.html','w').write(s)
