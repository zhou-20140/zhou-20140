import mian
import uex_tex_change as utc

mian.add_fl('pt];pt]#error#;','tex','error,retrun')
mian.add_fl('pt]------------;[os];pt]------------;','tex','start')
mian.runcode(mian.find('start.tex'))
mian.lang='english'

while True:
    p=utc.context_run(input('<=> '))