import mods.game
import mods.kl

import language as lg
import mian

def open():
    mod=input('mod: ')
    
    try:

        if mod=='kl':
            mods.kl.write()
        if mod=='game':
            mods.game.main()
    
    except:
        print('mod error!\n',lg.inthes(mian.lang,5))