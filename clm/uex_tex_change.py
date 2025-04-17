import main
import m_app as mp
import language as lg
import mod
import picture as pic

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
                try:main.runcode(main.find(put[3:-1]))
                except TypeError:print('start error!\n',lg.inthes(main.lang,3));main.log.append('start error!')
            if 'nt]' in put:
                dm=open(put[3:-1],'r').readline()
                dm=dm.split(',')
                dm[-1][-1]=='\n'
                dm[-1]=dm[-1][0:-1]
                mp.register(dm[0],dm[1],dm[2])
                main.log.append('add app')
            if 'lg]' in put:
                main.lang=put[3:-1]
            if '[dir]' in put:
                for i in main.tg:print(i.name,i.hj,sep='.')
            if 'dl]' in put:
                main.del_fl(put[3:-1])
                main.log.append('delete file')
            if '[mod]' in put:
                mod.start_mod()
            if '[svd]' in put:
                main.cts=False
                main.log.append('shutdown')
            if '[cln]' in put:
                    print("\033c", end="")
            if '[log]' in put:
                    for i in main.log:print(i)
            if '[inf]' in put:
                pic.pic1()
                print('system_vision: clm-2.2.7') 
                print('sytem_kernel: ttl-1.1.0')
                print('file_block: ',len(main.tg))
                print('mod quantity: 1')
                print('\n#github#  zhou-20140')
                print('#email#   3991885506@qq.com')              
            put=''