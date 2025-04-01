import sys
sys.path.append("clm//")
import mian

def write():    
    print("\033c", end="")
    context=''
    i=0

    print('kl code editor\n')
    while True:
        i+=1
        text=input('['+str(i)+'] ')
        if text=='/exit':
            break
        context+=text+';'
    
    mian.add_fl(context,'tex',input('name: '))
    mian.log.append('write file')
    print("\033c", end="")