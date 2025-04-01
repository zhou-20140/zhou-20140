import mian
import m_app as mp
import language as lg
import mod

def context_run(text):
    put=''
    for i in text:
        put+=i
        if put[-1]==';' or put[-1]=='\n':
            dm=''
            if 'pt]' in put:
                print(put[3:-1])
            if '[os]' in put:
                print('clm v2.2.3')
            if 'st]' in put:
                try:mian.runcode(mian.find(put[3:-1]))
                except TypeError:print('start error!\n',lg.inthes(mian.lang,3));mian.log.append('start error!')
            if 'nt]' in put:
                dm=open(put[3:-1],'r').readline()
                dm=dm.split(',')
                dm[-1][-1]=='\n'
                dm[-1]=dm[-1][0:-1]
                mp.register(dm[0],dm[1],dm[2])
                mian.log.append('add app')
            if 'lg]' in put:
                mian.lang=put[3:-1]
            if '[dir]' in put:
                for i in mian.tg:print(i.name,i.hj,sep='.')
            if 'dl]' in put:
                mian.del_fl(put[3:-1])
                mian.log.append('delete file')
            if '[mod]' in put:
                mod.start_mod()
            if '[svd]' in put:
                mian.cts=False
                mian.log.append('shutdown')
            if '[cln]' in put:
                    print("\033c", end="")
            if '[log]' in put:
                    for i in mian.log:print(i)                
            put=''