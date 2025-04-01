import language as lg
import mian
from mods import kl
def start_mod():
    mod=input('mod: ')
    
    try:
        if mod=='kl':
            kl.write()

        
    
    except:
        print('mod error!\n',lg.inthes(mian.lang,5))