import mian
import uex_tex_change as utc

mian.read_date()
mian.runcode(mian.find('start.tex'))
mian.lang='english'

cts=True

while cts:
    p=utc.context_run(input('<=> '))
    if p=='stop':
        print('save date')
        mian.save_date()
        print('complet!')
        cts=False