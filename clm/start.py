import mian
import uex_tex_change as utc

mian.read_date()
print('read date complet')
mian.runcode(mian.find('start.tex'))
mian.lang='english'

while mian.cts:
    utc.context_run(input('<=> '))

print('save date')
mian.save_date()
print('complit')