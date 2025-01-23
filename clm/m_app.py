import mian
import language as lg

def register(name,set_text,path):
    
    print(set_text)
    
    if_n=True
    for i in mian.tg:
        if i.name==name:
            if_n=False

    if if_n:
        r=open(path,'r')
        text=r.read()
        mian.add_fl(text,'tex',name)
    else:
        print('install error!\n',lg.inthes(mian.lang,0))
        return 'error'

def rem_app(name):
    mian.tg.pop(mian.find(name))