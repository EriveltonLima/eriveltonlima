import json,os,sys
here=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,here)
import programs as p
world=open(os.path.join(here,'..','..','aegean','build','countries-110m.json')).read()
t=open(os.path.join(here,'template.html')).read()
for P,short in ((p.QATAR,'Qatar'),(p.IBERIA,'Iberia')):
    d=p.build(P)
    s=t.replace('/*TITLE*/',P['title']).replace('/*SHORT*/',short).replace('/*ACC*/',P['accent']).replace('/*ACC2*/',P['accent2'])
    s=s.replace('/*WORLD*/null',world).replace('/*PROGRAM*/{}',json.dumps(d,ensure_ascii=False))
    out=os.path.join(here,'..',P['key']);os.makedirs(out,exist_ok=True);open(os.path.join(out,'index.html'),'w').write(s)
print('ok')
