import mian
import uex_tex_change as utc
try:
    mian.read_date()
except FileNotFoundError:
    print('dw error')
    with open('clm\date\dw.txt','w') as f:
        f.write('\n')
    mian.add_fl('pt];pt]#error#;','tex','error,retrun')
    mian.add_fl('pt]------------;[os];pt]------------;','tex','start')
    mian.read_date()

print('read date complet')
mian.runcode(mian.find('start.tex'))
mian.lang='english'

while mian.cts:
    utc.context_run(input('<=> '))

print('save date')
mian.save_date()
print('complit')