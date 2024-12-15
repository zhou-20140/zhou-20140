import mian
import language as lg

def register(name,set_text,path):
    if_n=True
    for i in mian.tg:
        if i.name==name:
            if_n=False

    if if_n:
        mian.add_fl(set_text,'set',name)
        r=open(path,'r')
        text=r.read()
        mian.add_fl(text,'tex',mian.tg[mian.find(name+'.set')].name)
    else:
        print('install error!\n',lg.inthes(mian.lang,0))
        return 'error'

def rem_app(name):
    mian.tg.pop(mian.find(name))