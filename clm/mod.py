import language as lg
import mian
import os
from mods import kl
def start_mod():
    mod=input('mod: ')
    
    try:
        if mod=='kl':
            kl.write()
        else:
            os.system(f'python clm\mods\{mod}.py')
        

        
    
    except:
        print('mod error!\n',lg.inthes(mian.lang,5))