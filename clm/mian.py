import uex_tex_change as utc
import language as lg

class Cl:
    def __init__(self,context,hj,name):
        self.context=context
        self.hj=hj
        self.name=name
        pass
    pass
tg=[]

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
        return 0

def runcode(n):
    if tg[n].hj=='tex' or tg[n].hj=='uex':
        print(utc.context_run(tg[n].context))
    else:
        print('run_code error!\n')

