import main
import uex_tex_change as utc
import json
try:
    file=open("clm\date\config\config.json", 'r')
    config_data = json.load(file)

except:
    print(f"config error!")
    main.log.append('config error')
try:
    main.read_date()
except FileNotFoundError:
    if config_data['auto_fix_dw']:
        print('dw error')
        main.log.append('dw error')
        with open('clm\date\dw.txt','w') as f:
            f.write('\n')
        main.add_fl('pt];pt]#error#;','tex','error,retrun')
        main.add_fl('pt]------------;[os];pt]------------;','tex','start')
        main.read_date()

print('read date complet')
main.log.append('read date complet')
main.runcode(main.find('start.tex'))
main.lang=config_data['language']
file.close()

while main.cts:
    utc.context_run(input('<=> '))

print('save date')
main.save_date()
print('complit') 