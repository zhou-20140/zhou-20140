import mian
import uex_tex_change as utc
import json
try:
    file=open("clm\date\config\config.json", 'r', encoding='utf-8')
    config_data = json.load(file)

except:
    print(f"config error!")
    mian.log.append('config error')
try:
    mian.read_date()
except FileNotFoundError:
    if config_data['auto_fix_dw']:
        print('dw error')
        mian.log.append('dw error')
        with open('clm\date\dw.txt','w') as f:
            f.write('\n')
        mian.add_fl('pt];pt]#error#;','tex','error,retrun')
        mian.add_fl('pt]------------;[os];pt]------------;','tex','start')
        mian.read_date()

print('read date complet')
mian.log.append('read date complet')
mian.runcode(mian.find('start.tex'))
mian.lang=config_data['language']
file.close()

while mian.cts:
    utc.context_run(input('<=> '))

print('save date')
mian.save_date()
print('complit') 