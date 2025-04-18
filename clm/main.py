import uex_tex_change as utc
import language as lg

cts=True

class Cl:
    def __init__(self,context,hj,name):
        self.context=context
        self.hj=hj
        self.name=name
        pass
    pass
tg=[]
log=[]
lang=''

def add_fl(context,hj,name):
    tg.append(Cl(context,hj,name))

def del_fl(name):
    del tg[find(name)]

def find(file):
    try:
        name,hj=file.split('.')
    except:
        print('item error!\n',lg.inthes(lang,1))
        log.append('item error')
        return 0
    n=0
    ifn=False
    for i in tg:
        if i.name==name and i.hj==hj:
            ifn=True
            return n
        n+=1

    if ifn==False:
        print('find error!\n',lg.inthes(lang,2))
        log.append('find error')
        return find('error,retrun.tex')

def runcode(n):
    if tg[n].hj=='tex' or tg[n].hj=='uex':
        print(utc.context_run(tg[n].context))
    else:
        print('run_code error!\n',lg.inthes(lang,5))
        log.append('run_code error')

def save_date():
    file=open('clm\\date\\dw.txt','w')
    file.write(str(len(tg))+'\n')
    for i in tg:
        file.write(' clm\\date\\'+i.name+'.txt'+'#'+i.name+'#'+i.hj)
    for i in tg:
        file=open('clm\\date\\'+i.name+'.txt','w')
        file.write(i.context)
    file.close()
    import json
    config_flag=json.load(open('clm\\date\\config\\config.json','r'))
    if config_flag['auto_save_logs']:
        with open('clm\\date\\logs\\log1','a+') as file:
            file.write('\n')
            file.write('\n'.join(log))

def read_date():
    ed=open('clm\\date\\dw.txt','r')
    text=ed.readlines()[-1].split(' ')
    del text[0]
    hj=[]
    path=[]
    name=[]
    for i in text:
        hj.append(i.split('#')[-1])
        name.append(i.split('#')[-2])
        path.append(i.split('#')[-3])
    for i in range(len(text)):
        file=open(path[i],'r')
        add_fl(file.read(),hj[i],name[i])
        file.close()
    ed.close()