import clm.main as main
import language as lg

def register(name,set_text,path):
    
    print(set_text)
    
    if_n=True
    for i in main.tg:
        if i.name==name:
            if_n=False

    if if_n:
        r=open(path,'r')
        text=r.read()
        main.add_fl(text,'tex',name)
    else:
        print('install error!\n',lg.inthes(main.lang,0))
        return 'error'

def rem_app(name):
    main.tg.pop(main.find(name))