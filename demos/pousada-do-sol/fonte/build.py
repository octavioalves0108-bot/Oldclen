import base64, os, re, sys
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'template.html'),encoding='utf-8').read()
BLANK='data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
def uri(name):
    b=open(os.path.join(here,'img',name+'.webp'),'rb').read()
    return 'data:image/webp;base64,'+base64.b64encode(b).decode()
seen=set()
def img_src(m):
    k=m.group(1)
    if k in seen: return 'src="%s" data-img="%s"'%(BLANK,k)
    seen.add(k); return 'src="%s" data-img-src="%s"'%(uri(k),k)
out=re.sub(r'src="\{\{([a-z0-9-]+)\}\}"',img_src,src)
out=re.sub(r'\{\{([a-z0-9-]+)\}\}',lambda m:uri(m.group(1)),out)
dst=sys.argv[1] if len(sys.argv)>1 else os.path.join(here,'..','index.html')
open(dst,'w',encoding='utf-8').write(out)
print(dst, len(out.encode())//1024,'KB')
